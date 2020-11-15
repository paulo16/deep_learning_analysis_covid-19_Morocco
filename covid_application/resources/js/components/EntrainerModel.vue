<template>
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-12">
                  <br />
          <div class="alert alert-info p-2">
              <strong> <h2>ENTRAINNER VOTRE MODELE (DONNEES GLOBALES)</h2></strong>
          </div>
        </div>
        <div class="col-md-12">
            <div class="card">
                <div class="card-header text-white" style="background-color: #00aa9e;"><h3 style="color: white;">ETAPES DE PREDICTION COVID 19</h3></div>

                <div class="card-body">
                    <form @submit.prevent="send_testset">
                        <div class="form-row">
                            <!-- CHOISISSEZ LE MODELE -->
                            <div class="col-md-6">
                                <fieldset class="border p-2">
                                    <legend class="w-auto">
                                        <h4><b>Choisissez votre modèle</b></h4>
                                    </legend>

                                    <table>
                                        <tr>
                                            <td>
                                                <div class="form-check form-check-inline">
                                                    <input class="form-check-input" v-model="modele" type="radio" name="modele" id="cnn" value="cnn" />
                                                    <label class="form-check-label" for="inlineRadio1">Convolutional neural network (CNN) </label>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <div class="form-check form-check-inline">
                                                    <input class="form-check-input" v-model="modele" type="radio" name="modele" id="gru" value="gru" />
                                                    <label class="form-check-label" for="inlineRadio2">Gated recurrent units (GRU) </label>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <div class="form-check form-check-inline">
                                                    <input class="form-check-input" v-model="modele" type="radio" name="modele" id="lstm" value="lstm" />
                                                    <label class="form-check-label" for="inlineRadio3">Long short-term memory (LSTM) </label>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <div class="form-check form-check-inline">
                                                    <input class="form-check-input" v-model="modele" type="radio" name="modele" id="mlp" value="mlp" />
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
                                    <legend class="w-auto">
                                        <h4><b>Choisissez m-lags -> n-steps</b></h4>
                                    </legend>

                                    <table>
                                        <tr>
                                            <td>
                                                <div class="form-check form-check-inline">
                                                    <input class="form-check-input" v-model="lag_steps" type="radio" name="lag_steps" id="lag_steps_1_7" value="1" />
                                                    <label class="form-check-label" for="lag_steps_1_7">1 jour pour prédire 7 devant </label>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <div class="form-check form-check-inline">
                                                    <input class="form-check-input" v-model="lag_steps" type="radio" name="lag_steps" id="lag_steps_2_7" value="2" />
                                                    <label class="form-check-label" for="lag_steps_2_7">2 jours pour prédire 7</label>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <div class="form-check form-check-inline">
                                                    <input class="form-check-input" v-model="lag_steps" type="radio" name="lag_steps" id="lag_steps_4_7" value="4" />
                                                    <label class="form-check-label" for="lag_steps_4_7">4 jour pour prédire 7</label>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <div class="form-check form-check-inline">
                                                    <input class="form-check-input" v-model="lag_steps" type="radio" name="lag_steps" id="lag_steps_7_7" value="7" />
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
                                <br />
                                <fieldset class="border p-2">
                                    <legend class="w-auto">
                                        <h4><b>Ajouter des données aux données existantes (CSV)</b></h4>
                                    </legend>
                                    <div class="form-row">
                                        <div class="col-md-3">
                                            <label for="excel_file"><h5>Données à ajouter</h5></label>
                                        </div>
                                        <div class="col-md-5">
                                            <input type="file" class="form-control" id="test_set_csv" ref="test_set_csv" @change="getfile()" placeholder="E:\Scans\excel_de_control.xls" />
                                        </div>
                                        <div class="col-md-4">
                                            <button class="form-control btn btn-primary waves-effect waves-light" type="submit">Soumettre les données</button>
                                        </div>
                                    </div>
                                </fieldset>
                            </div>
                            <!-- FIN CHOIX TEST -->
                        </div>
                    </form>
                    <br />
                    <div v-if="after_submit" class="alert alert-success" role="alert"><p>{{after_submit}}</p></div>
                </div>
            </div>
        </div>
        <!-- EFFECTUER ENTRAINNEMENT-->
        <div class="col-md-12">
            <div class="card">
                <div class="card-header text-white" style="background-color: #00aa9e;"><h3 style="color: white;">LANCER L'ENTRAINNEMENT</h3></div>

                <div class="card-body">
                    <div class="col-md-12">
                        <label for="entrainner">entrainement du modèle </label>
                        <button class="form-control btn btn-primary waves-effect waves-light" v-on:click="entrainner" id="entrainner">Commencer</button>
                    </div>
                    <div v-if="loader_predict" class="col-md-12 d-flex align-items-center">
                        <strong>Entrainement en cours , veuillez patienter ...</strong>
                        <div class="spinner-border ml-auto" role="status" aria-hidden="true"></div>
                    </div>
                </div>
            </div>
        </div>
        <!-- FIN ENTRAINNEMENT -->

        <!-- AFFICHAGE DES STATISTIQUES-->
        <div class="col-md-12">
            <div class="card">
                <div class="card-header text-white" style="background-color: #00aa9e;"><h3 style="color: white;">STATISTIQUES</h3></div>

                <div class="card-body">
                    <div class="col-md-12">
                        <h4>Métriques d'entrainnement</h4>
                        <br />
                        <br />
                        <table class="table">
                            <thead class="thead-dark">
                                <tr>
                                    <th>Métriques</th>
                                    <th>Valeurs</th>
                                </tr>
                            </thead>
                            <tbody id="prediction_7_jours">
                                <tr>
                                    <td>MSE</td>
                                    <td>{{mse}}</td>
                                </tr>
                                <tr>
                                    <td>RMSE</td>
                                    <td>{{rmse}}</td>
                                </tr>
                                <tr>
                                    <td>MAE</td>
                                    <td>{{mae}}</td>
                                </tr>
                                <tr>
                                    <td>R2</td>
                                    <td>{{r2}}</td>
                                </tr>
                                <tr>
                                    <td>Maxerror</td>
                                    <td>{{maxerror}}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        <!-- FIN STATS-->

        <!-- EFFECTUER DES PREDICTIONS -->
        <div class="col-md-12">
            <div class="card">
                <div class="card-header text-white" style="background-color: #00aa9e;"><h3 style="color: white;">LANCER PREDICTION SUR TEST</h3></div>
                
                <!-- Note Importante -->
                <div class="card-body">
                  <div class="alert alert-info" role="alert">
                    <ul class="list-group">
                        <li class="list-group-item"><h3>Important à savoir</h3></li>
                        <li class="list-group-item list-group-item-success">Si 1 -> 7 choisit, le fichier de données doit contenir une ligne </li>
                        <li class="list-group-item list-group-item-success">Si 2 -> 7 choisit, le fichier de données doit contenir 2 lignes</li>
                        <li class="list-group-item list-group-item-success">Si 4 -> 7 choisit, le fichier de données doit contenir 4 lignes</li>
                        <li class="list-group-item list-group-item-success">Si 7 -> 7 choisit, le fichier de données doit contenir 7 lignes</li>
                      </ul>
                    </div>
                    <!-- CHOIX FICHIER DE TEST -->
                    <div class="col-md-12">
                        <br />
                        <fieldset class="border p-2">
                            <legend class="w-auto">
                                <h4><b>Insérer les données de Test (CSV)</b></h4>
                            </legend>
                            <div class="form-row">
                                <div class="col-md-3">
                                    <label for="excel_file"><h5>Données de Test</h5></label>
                                </div>
                                <div class="col-md-5">
                                    <input type="file" class="form-control" id="test_set_csv" ref="test_set_csv" @change="getfile()" placeholder="" />
                                </div>
                                <div class="col-md-4">
                                    <button class="form-control btn btn-primary waves-effect waves-light" type="submit">Soumettre les données</button>
                                </div>
                            </div>
                        </fieldset>
                    </div>
                    <!-- FIN CHOIX TEST -->
                    <div class="col-md-12">
                        <fieldset class="border p-2">
                            <legend class="w-auto">
                                <h4><b>Prédiction</b></h4>
                            </legend>

                            <label for="entrainner">PREDICTION SUR TEST SET</label>
                            <button class="form-control btn btn-primary waves-effect waves-light" v-on:click="prediction_test_after_train" id="entrainner">Commencer</button>
                        </fieldset>
                    </div>
                    <div v-if="loader_predict" class="col-md-12 d-flex align-items-center">
                        <strong>Prédiction en cours , veuillez patienter ...</strong>
                        <div class="spinner-border ml-auto" role="status" aria-hidden="true"></div>
                    </div>
                </div>
            </div>
        </div>
        <!-- FIN PREDICTIONS -->

        <!--AFFICHAGE DES RESULTATS TEST -->
        <div class="col-md-12">
            <div class="card">
                <div class="card-header text-white" style="background-color: #00AA9E;"><h3 style="color:white;">STATISTIQUES SUR 7 JOURS</h3></div>
                <div class="card-body">
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
            </div>
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
    
      entrainner(e){
        //e.preventDefault()
        this.loader_predict = true ;
        console.log(this.api_url);
        let Data = {
            'lags' : this.lag_steps ,
            'modele' : this.modele
          }
        axios({ 
          method: "POST",
          url : this.api_url+"/entrainermodel" ,
          data: JSON.stringify(Data)
          }).then(result => {
            this.loader_predict = false ;
            this.mse= result.data.mse
            this.rmse= result.data.rmse
            this.mae= result.data.mae
            this.r2= result.data.r2
            this.maxerror= result.data.maxerror
          console.log(result.data)
        }, error => {
          this.loader_predict = false ;
          console.error(error);
        });
      }
  }
  };
</script>
