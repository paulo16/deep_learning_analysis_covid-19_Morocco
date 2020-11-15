def metriques():
  global TESTSET_CONF_FILE_PATH , TRAIN_DATA_PATH , X_train_bis , Y_train_bis

  scaler = MinMaxScaler(feature_range=(0, 1))
  scaler2 = MinMaxScaler(feature_range=(0, 1))

  rf=request.form
  print(rf)
  for key in rf.keys():
    data=key
  print(data)
  data_dic=json.loads(data)
  print(data_dic.keys())
  m_lags = data_dic['lags']
  modele = data_dic['modele']
  print(m_lags)
  print(modele)
  nb_seq = int(m_lags)
  m_steps=7
  m_lags = int(m_lags)

  #prediction= np.empty(7)
  if modele=="cnn" and m_lags == 7:
    nb_seq =7
    n_out = 7
    X_train_bis=X_train
    Y_train_bis=Y_train

    # ensure all data is float
    X_train_bis = X_train_bis.astype('float32')
    # ensure all data is float
    Y_train_bis = Y_train_bis.astype('float32')

    # normalize features

    X_train_bis= scaler.fit_transform(X_train_bis)
    Y_train_bis= scaler2.fit_transform(Y_train_bis)

    # reframe as supervised learning
    # on doit toujours vers une conversion vers n_out ensuite con choisit le nombre de colonnes dont nous avons besoins
    X_train_bis = series_to_supervised(X_train_bis, nb_seq, n_out)
    Y_train_bis = series_to_supervised(Y_train_bis, nb_seq, n_out)
    col_take= 'var[1-j]\(t\-[1-i]\)$'
    col_take = col_take.replace("i", str(nb_seq))
    col_take = col_take.replace("j", str(n_out))
    regex_find = col_take
    col_x_need_train =X_train_bis.filter(regex=regex_find,axis=1).head(1)
    Y_train_bis = Y_train_bis.filter(regex='var[1-7](\(t\+\d{1}\)|(\(t\)))$',axis=1)
    X_train_bis = X_train_bis.filter(regex=regex_find,axis=1)
    X_train_bis=X_train_bis.values
    Y_train_bis=Y_train_bis.values
    # reshape input to be 3D [samples, timesteps, features]
    X_train_bis = X_train_bis.reshape(X_train_bis.shape[0], 1, X_train_bis.shape[1])


    path_cnn ='/content/drive/My Drive/Colab Notebooks/covidapp/model_cnn_7_7.h5'
    model_cnn_7_7_confinement = keras.models.load_model(path_cnn)
    print('** Model cnn_7_7_confinement Load *** ')


    prediction = model_cnn_7_7_confinement.predict(X_train_bis) 
    Y_train_bis_pred = prediction.reshape(-1, n_out)

    Y_train_bis_pred = Y_train_bis_pred.reshape(Y_train_bis_pred.shape[0], Y_train_bis_pred.shape[1])
    Y_train_bis_pred = scaler2.inverse_transform(Y_train_bis_pred)
    Y_train_bis_true = Y_train_bis.reshape((len(Y_train_bis), n_out))
    Y_train_bis_real = scaler2.inverse_transform(Y_train_bis_true )
    # Flatten for final errors
    Y_train_bis_pred_bis = Y_train_bis_pred.flatten()
    Y_train_bis_real_bis = Y_train_bis_real.flatten()
    filter_indices = [0,6,13,20,27,34,41,48,55,62,69]
    Y_train_bis_pred = Y_train_bis_pred [filter_indices ]

    Y_train_bis_real= Y_train_bis_real[filter_indices]
    Y_train_bis_pred = Y_train_bis_pred.flatten()
    Y_train_bis_real = Y_train_bis_real.flatten()
    mask = (df['date'] >= start_date) & (df['date'] <= end_date) &  (df['location'].isin(['Morocco']))
    date_train = df.loc[mask].date.sort_index(axis = 0)
    taille_x = date_train.shape[0] - nb_seq
    date_trainX = date_train[nb_seq:]
    prediction_train = pd.DataFrame(columns=['date_to_prediction','true_value','predict'])
    prediction_train['date_to_prediction'] = date_trainX[0:Y_train_bis_pred.shape[0]]
    prediction_train['predict'] = Y_train_bis_pred
    prediction_train['true_value'] = Y_train_bis_real 
    print(prediction_train.head(2))
    mse =  round(metrics.mean_squared_error(prediction_train['true_value'], prediction_train['predict']), 2)
    rmse = round( np.sqrt(metrics.mean_squared_error(Y_train_bis_real_bis, Y_train_bis_pred_bis)), 2)
    mae = round(metrics.mean_absolute_error(Y_train_bis_real_bis, Y_train_bis_pred_bis) , 2)
    r2 = round( r2_score(Y_train_bis_real_bis, Y_train_bis_pred_bis), 2)
    maxerror = round( max_error(Y_train_bis_real_bis, Y_train_bis_pred_bis), 2)