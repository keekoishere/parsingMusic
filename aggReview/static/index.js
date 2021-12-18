// var kek = JSON.parse(document.getElementById("mydiv").dataset.kek);

const app = Vue.createApp({
    data() {
        return {
          test : kek,  
        }
    },
    methods: {
        
    },
    computed :{
        
    },
    compilerOptions: {
      delimiters: ["*_","_*"],
    }
    

});

app.mount('#scores');
