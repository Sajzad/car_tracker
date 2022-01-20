function sendRequest(url, method, data){
    var r = axios({
        method:method,
        url: url,
        data: data,
        xsrfCookieName:'csrftoken',
        xsrfHeaderName:'X-CSRFToken',
        headers:{
        	"Content-Type": "application/json",
        	'X-Requested-With':'XMLHttpRequest'
        }
    })
    return r
}

var app = new Vue({
  el: '#app',
  delimiters:['[[', ']]'],
  data: {
  	cityName:null,
    cities: [],
    users : [],
  	city:null,
  	operators:[],
  	cars:[],
  	file: null,
  	OperatorId: null,
  	CarId :null,
  	CityId :null,
    assign_resp:null
  },
  created(){
    var url = '/api/cities';
    var vm = this;
    sendRequest(url, 'get')
        .then(function(response){
            vm.cities = response.data.cities;
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
  	handlingFile(e){
  		console.log(e.target.files[0])
  		this.file = e.target.files[0];
  	},
  	assignmentData(){
  		console.log("assign")
  		var url = '/api/users';
  		var vm = this;
        sendRequest(url, 'get')
            .then(function(response){
                vm.users = response.data.users;
        })
		var url = '/api/cars';
        sendRequest(url, 'get')
            .then(function(response){
                vm.cars = response.data.cars;
            })
  	},
  	assignOperator(){
  		var data = new FormData()
  		data.set('operator_id', this.OperatorId);
  		data.set('car_id', this.CarId);
  		data.set('city_id', this.CityId);
  		var url = 'api/assignment';
        var vm = this;
  		sendRequest(url, 'post', data)
        .then(function(response){
            vm.assign_resp = response.data
        })
  	},
    createCity(){
    	var data = new FormData();
    	data.set('name', this.cityName)
    	data.set('file', this.file)
        vm = this;
        var url = '/api/cities'
        sendRequest(url, 'post', data)
            .then(function(response){
            var url = '/api/cities';
            sendRequest(url, 'get')
                .then(function(response){
                    vm.cities = response.data.cities;
                })
            })
        this.cityName = null;

    },
    preData(id){
        vm = this
        var url = '/api/city/'+id
        var r = sendRequest(url, 'get')
            .then(function(response){
                vm.city = response.data.city;
                console.log(response.data.city);
                // vm.cities = [...vm.cities, ...response.data.cities]
            })
    },
    updateCity(id){
    	var data = {
            "city": this.city.name
        }
        vm = this
        var url = '/api/city/'+id
        sendRequest(url, 'put', data)
        .then(function(response){
            var url = '/api/cities';
            sendRequest(url, 'get')
                .then(function(response){
                    vm.cities = response.data.cities;
                })
        })


    },    
    deleteCity(id){
    	var url = '/api/city/'+id
        var vm=this
        sendRequest(url, 'delete')
        .then(function(response){
            console.log(response.data);
            var url = '/api/cities';
            sendRequest(url, 'get')
                .then(function(response){
                    vm.cities = response.data.cities;
                })

        })
    },

  }
})
