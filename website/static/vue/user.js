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
  	userName:null,
    users: [],
    managers: [],
  	user:null,
  },
  created(){
    var url = '/api/users';
    var vm = this;
    var r = sendRequest(url, 'get')
        .then(function(response){
            vm.users = response.data.users;
        })    
    var url = '/api/managers';
    var vm = this;
    var r = sendRequest(url, 'get')
        .then(function(response){
            console.log(response.data)
            vm.managers = response.data;
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
    createUser(){
        var data = {
            "name": this.userName
        }
        vm = this;
        var url = '/api/users'
        sendRequest(url, 'post', data)
            .then(function(response){
            var url = '/api/users';
            sendRequest(url, 'get')
                .then(function(response){
                    vm.users = response.data.users;
                })
        })
        this.userName = null;

    },
    preData(id){
        vm = this
        var url = '/api/user/'+id
        var r = sendRequest(url, 'get')
            .then(function(response){
                vm.user = response.data.user;
                console.log(response.data.user);
                // vm.users = [...vm.users, ...response.data.users]
            })
    },
    updateUser(id){
    	var data = {
            "user": this.user.name
        }
        vm = this
        var url = '/api/user/'+id
        sendRequest(url, 'put', data)
        .then(function(response){
            var url = '/api/users';
            sendRequest(url, 'get')
                .then(function(response){
                    vm.users = response.data.users;
                })
        })


    },    
    deleteUser(id){
    	var url = '/api/user/'+id
        var vm=this
        sendRequest(url, 'delete')
        .then(function(response){
            console.log(response.data);
            var url = '/api/users';
            sendRequest(url, 'get')
                .then(function(response){
                    vm.users = response.data.users;
                })

        })
    },

  }
})
