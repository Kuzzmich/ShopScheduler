var userControllers = angular.module('userControllers', []);

// First controller as example
userControllers.controller('UserDetailController', ['$scope', '$routeParams', '$http',
    function ($scope, $routeParams, $http) {
        $http.get('/api/user/' + $routeParams.userId).success(function (data) {
            $scope.user = Object();
            $scope.user = data;
        });
    }
]);


// Login, logout, register
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
            console.log(data);
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


// get schedule and check is shop open now
userControllers.controller('scheduleParser', ['$scope', '$routeParams', '$http',
    function ($scope, $routeParams, $http) {
        $http.get('/api/shop/' + $routeParams.shopId).success(function (data) {
            $scope.shop = Object();
            $scope.shop = data;
            $scope.week = {1: 'MON', 2: 'TUE', 3: 'WEN', 4: 'THU', 5: 'FRI', 6: 'SAT', 7: 'SUN'};

            var date = new Date();
            var today = date.getDay(); // function is returnin 0 for Sunday, 1 for Monday  and etc.
            if (today === 0)
                today = 7;  // kludge
            var time = date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds();
            var is_open = false;
            var is_closed_by_owner = false;
            if ($scope.shop.is_open) {
                $scope.shop.schedule.schedule_records.forEach(function (record) {  // schedule[0] - kludge
                    if (record.day_of_week_id === today) {
                        if (Date.parse(moment(time, 'HH:mm:ss')) > Date.parse(moment(record.time_open, 'HH:mm:ss'))
                            && Date.parse(moment(time, 'HH:mm:ss')) < Date.parse(moment(record.time_close, 'HH:mm:ss'))) {
                            is_open = true;
                            if (record.breaks) {
                                record.breaks.forEach(function (pause) {
                                    if (Date.parse(moment(time, 'HH:mm:ss')) > Date.parse(moment(pause.time_start, 'HH:mm:ss'))
                                        && Date.parse(moment(time, 'HH:mm:ss')) < Date.parse(moment(pause.time_end, 'HH:mm:ss'))) {
                                        is_open = false;
                                    }
                                })
                            }
                        }
                    }
                });
            } else {
                is_closed_by_owner = true;
            }
            $scope.is_open = is_open;
            $scope.is_closed_by_owner = is_closed_by_owner;
        });
    }
]);


// Create shop and add default schedule
userControllers.controller('shopCreate', ['$scope', '$routeParams', '$http',
    function ($scope, $routeParams, $http) {
        $http.get('/api/is-auth/').success(function (data) {
            $scope.userid = data.id;
        });
        var getShopData = function () {
            var scheduleDefault = {
                'name': $scope.name + ' shop schedule',
                'schedule_records': [
                    {
                        'day_of_week_id': 1,
                        'time_open': null,
                        'time_close': null,
                        'breaks': []
                    },
                    {
                        'day_of_week_id': 2,
                        'time_open': null,
                        'time_close': null,
                        'breaks': []
                    },
                    {
                        'day_of_week_id': 3,
                        'time_open': null,
                        'time_close': null,
                        'breaks': []
                    },
                    {
                        'day_of_week_id': 4,
                        'time_open': null,
                        'time_close': null,
                        'breaks': []
                    },
                    {
                        'day_of_week_id': 5,
                        'time_open': null,
                        'time_close': null,
                        'breaks': []
                    },
                    {
                        'day_of_week_id': 6,
                        'time_open': null,
                        'time_close': null,
                        'breaks': []
                    },
                    {
                        'day_of_week_id': 7,
                        'time_open': null,
                        'time_close': null,
                        'breaks': []
                    }
                ]
            };
            return {
                name: $scope.name,
                shop_owner_id: $scope.userid,
                schedule: scheduleDefault
            };
        };
        $scope.create = function () {
            $http.post('/api/shop/', getShopData()).success(function (data) {
                $scope.success = 'registration success';
                $scope.name = data.name;
                $scope.id_shop = data.id;
            }).catch(function (data) {
                alert('It\'s a problem! Try again later');
                console.log(data);
            });
        }
    }
]);

userControllers.controller('shopDetailController', ['$scope', '$routeParams', '$http',
    function ($scope, $routeParams, $http) {
        $http.get('/api/shop/' + $routeParams.shopId).success(function (data) {
            $scope.shop = data;
        });
    }
]);

userControllers.controller('shopClose', ['$scope', '$routeParams', '$http',
    function ($scope, $routeParams, $http) {
        $http.get('/api/shop/' + $routeParams.shopId).success(function (data) {
            $scope.shop = data;
        });

        $scope.close = function (data) {
            $http.patch('/api/shop/' + $routeParams.shopId + '/', {'is_open': $scope.shop.is_open})
                .success(function (data) {
                    if (data.is_open)
                        alert('Your shop is open now');
                    else
                        alert('Your shop is closed now');
                })
                .catch(function (data) {
                    alert('It\'s a problem! Try again later');
                    console.log(data);
                });
        }
    }
]);


// Schedule updater doesn't work
userControllers.controller('shopScheduleUpdate', ['$scope', '$routeParams', '$http',
    function ($scope, $routeParams, $http) {
        $http.get('/api/shop/' + $routeParams.shopId).success(function (data) {
            $scope.shop = data;
            $scope.week = {1: 'MON', 2: 'TUE', 3: 'WEN', 4: 'THU', 5: 'FRI', 6: 'SAT', 7: 'SUN'};
        });

        $scope.sendSchedule = function (data) {
            $http.patch('/api/shop/' + $routeParams.shopId, data).success(function (data) {
                // $scope.success = 'registration success';
                // $scope.name = data.name;
                alert(data);
            }).catch(function (data) {
                alert('It\'s a problem! Try again later');
                console.log(data);
            });
        };

        $scope.addBreak = function () {
            $("#add-break-button").click(function (e) {
                e.preventDefault();
                $(this).parent().parent().after(
                    '<div class="form-row align-items-center">\n' +
                    '<div class="form-group col-auto">\n' +
                    '    <label for="time_start">Time open</label>\n' +
                    '    <input ng-model="time_end" type="text" class="form-control" id="time_open" placeholder="8:00">\n' +
                    '</div>\n' +
                    '<div class="form-group col-auto">\n' +
                    '    <label for="time_close">Time close</label>\n' +
                    '    <input ng-model="time_close" type="text" class="form-control" id="time_close" placeholder="17:00">\n' +
                    '</div>\n' +
                    '</div>'
                );
            });
        }
    }
]);