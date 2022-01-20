function sendRequest(url, method, data){
    var r = axios({
        method:method,
        url: url,
        data: data,
        xsrfCookieName:'csrftoken',
        xsrfHeaderName:'X-CSRFToken',
        headers:{
            'X-Requested-With':'XMLHttpRequest'
        }
    })
    return r
}


var app = new Vue({
  el: '#app',
  delimiters:['[[', ']]'],
  data: {
    carName:null,
    reports: [],
    positions:'',
  },
  created(){
    var url = '/api/reports';
    var vm = this;
    var r = sendRequest(url, 'get')
        .then(function(response){
            console.log(response.data);
            vm.reports = response.data;
        })
  },
  filters: {
    capitalize: function (value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)

    },    
  },
  methods: {
    carPosition(id){
        console.log(id)
        var data = {
            "assignment_id": id
        }
        vm = this;
        var url = '/api/tracking'
        sendRequest(url, 'post', data)
            .then(function(response){
                console.log(response.data);
                vm.positions = response.data;
            })

    },

  }
})
