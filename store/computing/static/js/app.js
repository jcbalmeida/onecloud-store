"use strict;"
app = angular.module('app', ['app.filters'])

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
})

app.controller('AppController', ['$scope', '$http', function($scope, $http){
    $scope.filters = {
        cpu: [],
        memory: [],
        disk: [],
        os: [],
        provider: []
    };

    $http.get('api/instances').then(function(result){
        angular.forEach(result.data, function(item){
            if (!$scope.filters.cpu.some(function(cpu){
                return cpu.value == item.v_cpu;
            })){
                $scope.filters.cpu.push({
                    value:item.v_cpu,
                    checked: false
                });
            }
            if (!$scope.filters.memory.some(function(ram){
                return ram.value == item.memory;
            })){
                $scope.filters.memory.push({
                    value:item.memory,
                    checked:false
                });
            }
            if (!$scope.filters.disk.some(function(disk){
                return disk.value == item.disk_space;
            })) {
                $scope.filters.disk.push({
                    value:item.disk_space,
                    checked: false
                });
            }
            angular.forEach(item.operating_system, function(os) {
                if (!$scope.filters.os.some(function(option){
                    return option.value == os.family.id;
                })){
                    $scope.filters.os.push({
                        label:os.family.name,
                        value:os.family.id,
                        checked: false
                    });
                }
            });
        });
    });

    $scope.plans = [];
    $http.get('api/plans').then(function(result){
        angular.forEach(result.data, function(item){
            $scope.plans.push(item);
            if (!$scope.filters.provider.some(function(option){
                return option.value == item.provider.id;
            })) {
                $scope.filters.provider.push({
                    label:item.provider.name,
                    value: item.provider.id,
                    checked: false
                });
            }
        });
    });
}]);

angular.module('app.filters', []).filter('planFilter', [function (){
    return function(plans, filters) {
        var os_filter = filters.os.filter(function(os) {
            return os.checked;
        });
        var cpu_filter = filters.cpu.filter(function(cpu) {
            return cpu.checked;
        });
        var ram_filter = filters.memory.filter(function(ram){
            return ram.checked;
        });
        var disk_filter = filters.disk.filter(function(disk){
            return disk.checked;
        });
        var provider_filter = filters.provider.filter(function(provider){
            return provider.checked;
        });
        var result = plans.filter(function(plan){
            if (os_filter.length > 0) {
                if (!os_filter.some(function(os) {
                    return plan.instance.operating_system.some(function(p_os){
                        return p_os.family.id == os.value;
                    });
                })) return false;
            }
            if (cpu_filter.length > 0) {
                if (!cpu_filter.some(function(cpu){
                    return cpu.value == plan.instance.v_cpu;
                })) return false;
            }
            if (ram_filter.length > 0) {
                if (!ram_filter.some(function(ram){
                    return ram.value == plan.instance.memory;
                })) return false;
            }
            if (disk_filter.length > 0) {
                if (!disk_filter.some(function(disk){
                    return disk.value == plan.instance.disk_space;
                })) return false;
            }
            if (provider_filter.length > 0) {
                if (!provider_filter.some(function(provider){
                    return provider.value == plan.provider.id;
                })) return false;
            }
            return true;
        });
        console.log('filtered ' + result.length);
        return result;
    }
}]);