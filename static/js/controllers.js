var userControllers = angular.module('userControllers', []);

userControllers.controller('UserDetailController', ['$scope', '$routeParams', '$http',
    function ($scope, $routeParams, $http) {
        $http.get('/api/is-auth/').success(function (data) {
            $scope.user = Object();
            $scope.user.username = data.user;
        });
    }
]);

userControllers.controller('authController', function ($scope, $routeParams, $http, $window, api) {
    // Angular does not detect auto-fill or auto-complete. If the browser
    // autofills "username", Angular will be unaware of this and think
    // the $scope.username is blank. To workaround this we use the
    // autofill-event polyfill [4][5]
    $('#id_auth_form input').checkAndTriggerAutoFillEvent();
    $http.get('/api/is-auth/').success(function (data) {
        $scope.user = Object();
        $scope.user.username = data.user;
    });
    $scope.getCredentials = function () {
        return {username: $scope.username, password: $scope.password};
    };
    $scope.getRegisterCredentials = function () {
        return {
            username: $scope.username,
            password: $scope.password,
            first_name: $scope.first_name,
            last_name: $scope.last_name,
            email: $scope.email
        };
    };

    $scope.login = function () {
        api.auth.login($scope.getCredentials()).$promise.then(function (data) {
            // on good username and password
            $scope.user = Object();
            $scope.user.username = data.username;
            // if signing in on the register page
            if (/register/.test(window.location.href)) {
                $window.location.replace('/');
            }
        }).catch(function (data) {
            // on incorrect username and password
            alert(data.data.detail);
        });
    };

    $scope.logout = function () {
        api.auth.logout(function () {
            $scope.user = undefined;
        });
    };

    $scope.register = function () {
        $scope.data = Object();
        api.users.create($scope.getRegisterCredentials()).$promise.then(function () {
            $scope.data.success = 'registration success';
        }).catch(function (data) {
            $scope.data.success = null;
            // Error message
            alert(Object.values(data.data));
        });
    };
});

userControllers.controller('scheduleParser', ['$scope', '$routeParams', '$http',
    function ($scope, $routeParams, $http) {
        $http.get('/api/schedule/').success(function (data) {
            $scope.schedule = Object();
            $scope.schedule = data.schedule;
            $scope.week = {1: 'MON', 2: 'TUE', 3: 'WEN', 4: 'THU', 5: 'FRI', 6: 'SAT', 7: 'SUN'};

            var date = new Date();
            var today = date.getDay(); // function is returnin 0 for Sunday, 1 for Monday  and etc.
            if (today === 0)
                today = 7;  // kludge
            var time = date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds();
            var is_open = false;
            data.schedule.schedule_records.forEach(function (record) {
                if (record.day_of_week_id === today){
                    if (Date.parse(moment(time, 'HH:mm:ss')) > Date.parse(moment(record.time_open, 'HH:mm:ss'))
                        && Date.parse(moment(time, 'HH:mm:ss')) < Date.parse(moment(record.time_close, 'HH:mm:ss'))){
                        is_open = true;
                        if (record.breaks){
                            record.breaks.forEach(function (pause) {
                                if (Date.parse(moment(time, 'HH:mm:ss')) > Date.parse(moment(pause.time_start, 'HH:mm:ss'))
                                    && Date.parse(moment(time, 'HH:mm:ss')) < Date.parse(moment(pause.time_end, 'HH:mm:ss'))){
                                    is_open = false;
                                }
                            })
                        }
                    }
                }
            });
            $scope.is_open = is_open;
            // for (var i = 0; i < data.schedule.length; i++){
            //     alert(i);
            // }

        });
    }
]);