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
  	cars: [],
  	car:null,
  },
  created(){
    var url = '/api/cars';
    var vm = this;
    var r = sendRequest(url, 'get')
        .then(function(response){
            vm.cars = response.data.cars;
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
    createCar(){
        var data = {
            "car": this.carName
        }
        vm = this;
        var url = '/api/cars'
        sendRequest(url, 'post', data)
            .then(function(response){
            var url = '/api/cars';
            sendRequest(url, 'get')
                .then(function(response){
                    vm.cars = response.data.cars;
                })
            })
        this.carName = null;

    },
    preData(id){
        vm = this
        var url = '/api/car/'+id
        var r = sendRequest(url, 'get')
            .then(function(response){
                vm.car = response.data.car;
                console.log(response.data.car);
                // vm.cars = [...vm.cars, ...response.data.cars]
            })
    },
    updateCar(id){
    	var data = {
            "car": this.car.car
        }
        vm = this
        var url = '/api/car/'+id
        sendRequest(url, 'put', data)
        .then(function(response){
            var url = '/api/cars';
            sendRequest(url, 'get')
                .then(function(response){
                    vm.cars = response.data.cars;
                })
        })


    },    
    deleteCar(id){
    	var url = '/api/car/'+id
        var vm=this
        sendRequest(url, 'delete')
        .then(function(response){
            console.log(response.data);
            var url = '/api/cars';
            sendRequest(url, 'get')
                .then(function(response){
                    vm.cars = response.data.cars;
                })

        })
    },

  }
})
