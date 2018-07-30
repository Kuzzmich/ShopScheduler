var myApp = angular.module('myApp', ['ngRoute', 'ngResource', 'ngCookies', 'userControllers']);

// myApp.config([
//     '$routeProvider',
//     function ($routeProvider) {
//         $routeProvider
//             .when('/', {
//             templateUrl: '/static/user-detail.html',
//             controller: 'UserDetailController'
//         });
//     }
// ]);

myApp.config([
    '$httpProvider',
    function ($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
]);

myApp.factory('api', function ($resource) {
    function add_auth_header(data, headersGetter) {
        // as per HTTP authentication spec [1], credentials must be
        // encoded in base64. Lets use window.btoa [2]
        var headers = headersGetter();
        headers['Authorization'] = ('Basic ' + btoa(data.username +
            ':' + data.password));
    }

    // defining the endpoints. Note we escape url trailing dashes: Angular
    // strips unescaped trailing slashes. Problem as Django redirects urls
    // not ending in slashes to url that ends in slash for SEO reasons, unless
    // we tell Django not to [3]. This is a problem as the POST data cannot
    // be sent with the redirect. So we want Angular to not strip the slashes!
    return {
        auth: $resource('/api/auth\\/', {}, {
            login: {method: 'POST', transformRequest: add_auth_header},
            logout: {method: 'DELETE'}
        }),
        users: $resource('/api/register\\/', {}, {
            create: {method: 'POST'}
        })
    };
});