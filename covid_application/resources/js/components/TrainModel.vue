<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <br>
                <div class="card">
                    <div class="card-header text-white" style="background-color: #00AA9E;">Training Model</div>

                    <div class="card-body">
                      <p id="bonjour">{{contenu_p}}</p>
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
        contenu_p : ''
      };
    },
    mounted() {
      axios({ 
        method: "GET",
        url : "https://47d46478273b.ngrok.io" ,
       }).then(result => {
        this.contenu_p= result.data;
        console.log(result.data)
      }, error => {
        console.error(error);
      });

      
    }
  };
</script>
