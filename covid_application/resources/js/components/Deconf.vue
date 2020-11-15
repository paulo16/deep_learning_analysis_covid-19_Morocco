<template>
    <div class="container">
        <div class="row justify-content-center">

            <div class="col-md-12">
                            <br>
                <div class="alert alert-info p-2">
                    <strong> <h2> MODELE DE DECONFINEMENT </h2></strong> 
                </div>
                <div class="card">
                    <div class="card-header text-white" style="background-color: #00AA9E;"><h3 style="color:white;"> ETAPES DE PREDICTION COVID 19</h3></div>

                    <div class="card-body">

                          <form  @submit.prevent="send_testset">
                            <div class="form-row">
                                  <!-- CHOISISSEZ LE MODELE -->
                                  <div class="col-md-6">
                                      <fieldset class="border p-2">
                                          <legend  class="w-auto"><h4><b>Choisissez votre modèle</b></h4> </legend>
                                          
                                          <table>
                                              <tr>
                                                  <td>
                                                    <div class="form-check form-check-inline">
                                                        <input class="form-check-input" v-model="modele" type="radio" name="modele" id="cnn" value="cnn">
                                                        <label class="form-check-label" for="inlineRadio1">Convolutional neural network (CNN) </label>
                                                    </div>
                                                  </td>
                                              </tr>
                                              <tr>
                                                  <td>
                                                    <div class="form-check form-check-inline">
                                                      <input class="form-check-input" v-model="modele" type="radio" name="modele" id="gru" value="gru">
                                                      <label class="form-check-label" for="inlineRadio2">Gated recurrent units (GRU) </label>
                                                    </div>
                                                  </td>
                                              </tr>
                                              <tr>
                                                  <td>                                             
                                                    <div class="form-check form-check-inline">
                                                      <input class="form-check-input" v-model="modele" type="radio" name="modele" id="lstm" value="lstm">
                                                      <label class="form-check-label" for="inlineRadio3">Long short-term memory (LSTM) </label>
                                                    </div>
                                                  </td>
                                              </tr>
                                              <tr>
                                                  <td>
                                                    <div class="form-check form-check-inline">
                                                      <input class="form-check-input" v-model="modele" type="radio" name="modele" id="mlp" value="mlp">
                                                      <label class="form-check-label" for="inlineRadio3">Multilayer perceptron (MLP) </label>
                                                    </div>
                                                  </td>
                                              </tr>
                                          </table>
                                      </fieldset>                         
                                  </div>
                                  <!-- FIN CHOIX MODELE -->

                                  <!-- CHOIX M-LAGS -> M-STEPS -->
                                  <div class="col-md-6">
                                      <fieldset class="border p-2">
                                          <legend  class="w-auto"><h4><b>Choisissez m-lags -> n-steps</b></h4> </legend>
                                          
                                          <table>
                                            <tr>
                                              <td>
                                                  <div class="form-check form-check-inline">
                                                    <input class="form-check-input"  v-model="lag_steps" type="radio" name="lag_steps" id="lag_steps_1_7" value="1">
                                                    <label class="form-check-label" for="lag_steps_1_7">1 jour pour prédire 7 devant </label>
                                                  </div>
                                              </td>
                                            </tr>
                                            <tr>
                                              <td>
                                                <div class="form-check form-check-inline">
                                                  <input class="form-check-input" v-model="lag_steps"  type="radio" name="lag_steps" id="lag_steps_2_7" value="2">
                                                  <label class="form-check-label" for="lag_steps_2_7">2 jours pour prédire 7</label>
                                                </div>
                                              </td>
                                            </tr>
                                            <tr>
                                              <td>
                                                <div class="form-check form-check-inline">
                                                  <input class="form-check-input" v-model="lag_steps"  type="radio" name="lag_steps" id="lag_steps_4_7" value="4">
                                                  <label class="form-check-label" for="lag_steps_4_7">4 jour pour prédire 7</label>
                                                </div>
                                              </td>
                                            </tr>
                                            <tr>
                                              <td>
                                                <div class="form-check form-check-inline">
                                                  <input class="form-check-input" v-model="lag_steps"  type="radio" name="lag_steps" id="lag_steps_7_7" value="7">
                                                  <label class="form-check-label" for="lag_steps_7_7">7 jour pour prédire 7</label>
                                                </div>
                                              </td>
                                            </tr>
                                          </table>
                                      </fieldset>                         
                                  </div>
                                  <!-- FIN CHOIX LAGS-->

                                  <!-- CHOIX FICHIER DE TEST -->
                                  <div class="col-md-12">
                                      <br>
                                      <fieldset class="border p-2">
                                          <legend  class="w-auto"><h4><b>Inserer les données pour prédiction (CSV)</b></h4></legend>
                                          <div class="alert alert-info" role="alert">
                                            <ul class="list-group">
                                                <li class="list-group-item"><h3>Important à savoir</h3></li>
                                                <li class="list-group-item list-group-item-success">Si 1 -> 7 choisit, le fichier de données doit contenir une ligne </li>
                                                <li class="list-group-item list-group-item-success">Si 2 -> 7 choisit, le fichier de données doit contenir 2 lignes</li>
                                                <li class="list-group-item list-group-item-success">Si 4 -> 7 choisit, le fichier de données doit contenir 4 lignes</li>
                                                <li class="list-group-item list-group-item-success">Si 7 -> 7 choisit, le fichier de données doit contenir 7 lignes</li>
                                              </ul>
                                          </div>
                                          <div class="form-row">
                                              <div class="col-md-3">
                                                <label  for="excel_file"><h5> Données du Passé  </h5></label>
                                              </div>
                                              <div class="col-md-5">
                                                <input  type="file" class="form-control" id="test_set_csv"  ref="test_set_csv"  @change="getfile()" placeholder="E:\Scans\excel_de_control.xls">
                                              </div>
                                              <div class="col-md-4 ">
                                                <button class="form-control btn btn-primary waves-effect waves-light"  type="submit">Soumettre les données </button>
                                              </div>
                                          </div>
                                      </fieldset> 
                                  </div>
                                  <!-- FIN CHOIX TEST -->
                            </div>
                          </form>
                          <br>
                          <div v-if="after_submit" class="alert alert-success" role="alert"><p>{{after_submit}}</p> </div>
                    </div>
                </div>

                <!-- EFFECTUER DES PREDICTIONS -->
                <div class="card">
                    <div class="card-header text-white" style="background-color: #00AA9E;"><h3 style="color:white;">EFFECTUER LA PREDICTION </h3></div>

                    <div class="card-body">
                        <div class="col-md-4 ">
                                <label  for="nom_de_dossiers">Lancer la prediction </label>
                                <button class="form-control btn btn-primary waves-effect waves-light" v-on:click="predict_conf_7_7"  id="predict" > Commencer </button>
                        </div>
                        <div v-if="loader_predict" class="d-flex align-items-center">
                            <strong>Prédiction en cours , veuillez patienter ...</strong>
                            <div class="spinner-border ml-auto" role="status" aria-hidden="true"></div>
                        </div>
                    </div>
                </div>
                <!-- FIN PREDICTIONS --> 

                <!-- AFFICHAGE DES STATISTIQUES-->
                <div class="card">
                    <div class="card-header text-white" style="background-color: #00AA9E;"><h3 style="color:white;">STATISTIQUES</h3></div>

                    <div class="card-body">
                      <div class="form-row">

                          <div class="col-md-6">
                            <h4>Affichage des Résultats de prédiction </h4>
                            <table class="table">
                              <thead class="thead-dark">
                                <tr>
                                  <th scope="col">#</th>
                                  <th>Cas de covid Predict</th>
                                </tr>
                              </thead>
                              <tbody id="prediction_7_jours">
                              
                                <tr v-for="jour_predit, num in predict_7_jours" v-bind:key="jour_predit">
                                  <td>{{num + 1}}</td><td>{{jour_predit}}</td>
                                </tr>
                              
                              </tbody>
                            </table>
                          </div>

                          <div class="col-md-6">
                            <h4>Métriques sur le train</h4>
                            <table class="table">
                              <thead class="thead-dark">
                                <tr>
                                  <th>Métriques <button type="button" v-on:click="metriques" class="btn btn-primary">Affichage de métriques</button></th>
                                </tr>
                              </thead>
                              <tbody id="prediction_7_jours">
                              
                                <tr>
                                  <td>MSE</td><td>{{mse}}</td>
                                </tr>
                                <tr>
                                  <td>RMSE</td><td>{{rmse}}</td>
                                </tr>
                                <tr>
                                  <td>MAE</td><td>{{mae}}</td>
                                </tr>
                                <tr>
                                  <td>R2</td><td>{{r2}}</td>
                                </tr>
                                <tr>
                                  <td>Maxerror</td><td>{{maxerror}}</td>
                                </tr>
                              
                              </tbody>
                            </table>

                          </div>


                      </div>
                    </div>
                </div>
                <!-- FIN STATS-->
            </div>
        </div>
    </div>
</template>

<script>
  import axios from "axios";
  export default {
    data() {
      return {
          api_url : process.env.MIX_DEEPLEARNING_API_URL,
          lag_steps : '',
          modele : '',
          test_csv : '',
          after_submit: '',
          loader_predict: false,
          predict_7_jours: [],
          rmse: 0,
          mse: 0 ,
          mae : 0,
          r2 : 0 ,
          maxerror : 0 ,

      };
    },

    methods: {

      getfile(){
          this.test_csv = document.getElementById('test_set_csv').files[0]
      },

      predict_conf_7_7(){
          this.loader_predict = true ;
          console.log(this.api_url);

          let Data = {
            'lags' : this.lag_steps ,
            'modele' : this.modele
          }

          console.log(Data);
          
          axios({ 
            method: "POST",
            url : this.api_url+"/predit_cnn_7_7_confinement" ,
            data: JSON.stringify(Data)
            }).then(result => {
              this.loader_predict = false ;
              //this.after_submit = result.data;
              this.predict_7_jours = [].concat.apply([], result.data);
              console.log(result.data)
          }, error => {
            console.error(error);
          });
          
      },
    
      send_testset(e){
          //e.preventDefault()
          console.log(this.api_url);

          let Data = new FormData();
          let fichiercsv = this.test_csv;

          Data.append('file', fichiercsv );
         
          axios({ 
            method: "POST",
            url : this.api_url+"/upload_test_set_confinement" ,
            data : Data
            }).then(result => {
            this.after_submit = "Données bien envoyées";
            console.log(result.data)
          }, error => {
            console.error(error);
          });
    },
    
      metriques(e){
        //e.preventDefault()
        console.log(this.api_url);
        let Data = {
            'lags' : this.lag_steps ,
            'modele' : this.modele
          }
        axios({ 
          method: "POST",
          url : this.api_url+"/metriques" ,
          data: JSON.stringify(Data)
          }).then(result => {
            this.mse= result.data.mse
            this.rmse= result.data.rmse
            this.mae= result.data.mae
            this.r2= result.data.r2
            this.maxerror= result.data.maxerror
          console.log(result.data)
        }, error => {
          console.error(error);
        });
      }
  }
  };
</script>
