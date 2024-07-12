var pageApp = angular.module("pageApp", []);
pageApp.controller("pageCtrl", function($scope) {
    
    $scope.ls = [];
    $scope.NewPos = [];
    $scope.edit = {};
    $scope.source = [];

   // Not ot close model on escape
    $('#editModal').modal({
        backdrop: 'static',
        keyboard: false
    })

    //$scope.NewPos = Position.length + 1;

    $scope.brnAdd = function() {
        $scope.AddNew = true;
        $scope.NewColums = "1"  
        $scope.NewType = "lead"  
        $scope.TextAlign = "left"  
        $scope.edit = {}
        $scope.UpdatePosList()
        $('#editModal').modal('show');
    }

    $scope.btnSave = function() {

        $scope.edit.cols = $scope.NewColums
        $scope.edit.NewType = $scope.NewType
        $scope.edit.TextAlign = $scope.TextAlign

        if($scope.AddNew ){
            $scope.source.push($scope.edit)
        }
        $('#editModal').modal('hide');
    }

    $scope.btnCose = function() {
        $('#editModal').modal('hide');
        return
debugger
        $.confirm({
            title: 'Confirm!',
            content: 'Do yo want to close!',
            buttons: {
                Close: function () {
                    $('#editModal').modal('hide');
                },
                cancel: function () {
                    //$.alert('Canceled!');
                }
            }
        });
    }

    $scope.UpdateStyle = function() {
        if($scope.edit.cl){
            for(i=0;i<$scope.edit.cl.length;i++){
                $scope.edit.cl[i].s = $scope.NewType
                $scope.edit.cl[i].ta = $scope.TextAlign

                if($scope.edit.cl[i].s == "List"){
                    $scope.edit.cl[i].lst = $scope.edit.cl[i].val.split('\n')
                }
            }
        }
    }
    
    $scope.txtOnChange = function(row) {
        if($scope.edit.cl[row].s == "List"){
            $scope.edit.cl[row].lst = $scope.edit.cl[row].val.split('\n')
        }
        debugger
    }

    $scope.btnEditItem = function(row) {

        $scope.edit = $scope.source[row]
        $scope.AddNew = false;

        $scope.NewColums = $scope.edit.cols
        $scope.NewType = $scope.edit.NewType
        $scope.TextAlign = $scope.edit.TextAlign 
        //$scope.UpdatePosList()
        $('#editModal').modal('show');
    }
    
    $scope.UpdatePosList = function() {

        var start = 0;
        var end = $scope.NewColums

        if( $scope.edit.cl  ){
            if($scope.edit.cl.length > $scope.NewColums){
                $scope.edit.cl.splice($scope.NewColums)
                end = 0
            }
            else if($scope.edit.cl.length < $scope.NewColums) {
                start = $scope.edit.cl.length
            }
        }
        else{
            $scope.edit = {}
            $scope.edit.cl = []
        }

        for(i=start;i<end;i++){
            var c = {}
            c.val = ""
            c.s = $scope.NewType
            c.ta = $scope.TextAlign
            $scope.edit.cl.push(c)
        }

        $scope.edit.colCls = "col-sm-" + 12/$scope.NewColums
    }

});

