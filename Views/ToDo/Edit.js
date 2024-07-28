var viewApp = angular.module("viewApp", []);

var viewApp = angular.module("viewApp", []);

viewApp.controller("viewCtrl", function($scope, $timeout) {

    $scope.init = function(){

        $scope.item_title = item_title
        $scope.item = {}
        $scope.item.title = "Test 1"
        $scope.item.description = "Test desc"

    }

    $scope.btn_calcel = function() {
        window.location.href = '/view/' + list_view_id;
    }

    $scope.take_cation = function(){
        save_pro()

        // $.confirm({
        //     title: 'Confirm!',
        //     content: 'Do yo want to submit!',
        //     buttons: {
        //         Cancel: function () {
        //         },
        //         OK: function () {
        //             $timeout(function() {
        //                 try{
        //                     save_pro();
        //                 }catch(err){}
        //             }, 10)
        //         }
        //     }
        // })
    }

    function save_pro(){

        // app_id = GettPostVal(request, 'app_id', err, True, 'int' )
        // flow_id = GettPostVal(request, 'flow_id', err, True, 'int' )
        // item_id = GettPostVal(request, 'item_id', err, False, 'int' )
        // data_json = GettPostVal(request, 'data_json', err, True )
        url = "/appaction"

        var req = {}
        req.app_id = 13
        req.flow_id = 4
        req.item_id = ''
        req.data_json = angular.toJson($scope.item)
        req.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

        

        $.ajax({
            url : url, 
            type : "POST",
            data : req,
            async:false,
            success : function(res) {
                debugger
                if(res.status == 0){
                    $.alert('Saved.')                    
                }
                else{
                    $.alert(res.error_essage)
                }
                $('#post-text').val(''); 
                console.log(res);                 
            },
    
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                alert('Error' + err)
                debugger
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }
}) 