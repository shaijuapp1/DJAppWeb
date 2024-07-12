docApp.controller("AppListCtrl", function($scope) {

    $scope.init = function(){

        
        $scope.grps = GetUserGroups()
        $('.CreateGrpId').select2();

        $scope.item = {}
        $scope.newItem = true
        var id = window.location.pathname.split('/')[2]
        var data = {};
        if(id){
            $scope.statusList = GetStatusList(id)
            

            $scope.newItem = false
            data.id = id
            data.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val() 
            url = "/applistdetailsajax"
            $.ajax({
                url : url, 
                type : "POST", // http method
                data : data,
                async : false,
                success : function(json) {
                    //debugger                    
                    $scope.item = json.details
                    console.log(json); // log the returned json to the console
                    console.log("success"); // another sanity check
                },
                error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }
            });
        }
        else{
            $scope.item = {}
            $scope.item.table = "AppData"
            $scope.item.title = ""
        }


        if(!$scope.item.create_goup_id){
            $scope.CreateGrpId = []
        }
        else{
            $scope.CreateGrpId = angular.fromJson($scope.item.create_goup_id);
        } 

        if(!$scope.item.access){
            $scope.Access = []
        }
        else{
            $scope.Access = angular.fromJson($scope.item.access);
            setTimeout(function(){ 
                for(i=0; i<$scope.Access.length; i++){
                    id =  i + "";
                    $('.Status' + id ).select2();
                    $('.Access' + id ).select2();
                    $('.AccessGrpId' + id ).select2();                                        
                }
            })
        }
        $('.NewAccessStatus' ).select2()
        $('.NewAccess' ).select2()
        $('.NewAccessGrpId' ).select2()
        
        if(!$scope.item.filelds){
            $scope.Filelds = []
        }
        else{
            $scope.Filelds = angular.fromJson($scope.item.filelds); 
        } 

        $scope.InitStatus()
        $scope.InitField(true)

        scopeApply()
    }

    $scope.brnCacel = function() {
        window.location.href = '/applist ';
    };
    

    $scope.Save = function(){
debugger
        url = "/applistupdateajax"
        var req = $scope.item
        req.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

        req.create_goup_id = angular.toJson($scope.CreateGrpId);
        req.filelds = angular.toJson($scope.Filelds);
        req.access = angular.toJson($scope.Access);

        $.ajax({
            url : url, 
            type : "POST",
            data : req,
            async:false,
            success : function(res) {
                debugger
                if(res.status == 0){
                    if($scope.newItem){
                        window.location.href = '/applistdetails/' + res.id
                    }
                    else{

                    }
                    //window.location.href = '/applist ';
                    alert('done')
                }
                else{
                    $.alert(res.ErrorMessage)
                    $('#post-text').val(res.ErrorMessage);
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

    $scope.AddNewAccess = function(){

        var ac = {}
        ac.Status = ''
        ac.Type = 'Group'
        ac.Field = ''
        ac.Group = ''
        ac.Access = ''

        $scope.Access.push(ac)

        setTimeout(function(){ 		
            id =  $scope.Access.length-1 + "";
            $('.Status' + id ).select2();
            $('.Access' + id ).select2();
            $('.AccessGrpId' + id ).select2();
    	}, 50);

        //$scope.$apply()
    }

    $scope.RemoveAccess = function(id){        
        $scope.Access.splice(id,1)
    }

    $scope.RemoveField = function(id){        
        $scope.Filelds.splice(id,1)
    }

    $scope.EditStatus = function(stItem){
        debugger
        $scope.editStatus = stItem
    }

    $scope.InitStatus = function(){
        $scope.editStatus = {}
        $scope.editStatus.id = null
        $scope.editStatus.app_id = $scope.item.id
        $scope.editStatus.status = ''
        scopeApply()
    }

    $scope.AddUpateStatus = function(stItem, remove){

        debugger
        url = "/appstatusupdate"
        if(remove){
            url = "/deleteappstatus"
        }

        stItem.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

        $.ajax({
            url : url, 
            type : "POST",
            data : stItem,
            async:false,
            success : function(res) {
                debugger
                if(res.status == 0){
                    $scope.statusList = GetStatusList($scope.item.id)
                    $scope.InitStatus()
                }
                else{
                    $.alert(res.ErrorMessage)
                }
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                alert('Error' + err)
                debugger
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }

    // $scope.AddUpdateAccess = function(stItem, remove){
    //     $('#AccessModal').modal('show')
    //     //$('#mypopup').modal('show');

    // }

    $scope.InitField = function(refreshList, fld){
        debugger
        if(fld){
            $scope.NewFld = fld
        }
        else{
            $scope.NewFld = {}
            $scope.NewFld.app_id = $scope.item.id
            $scope.NewFld.title = ''
            $scope.NewFld.type = ''
            $scope.NewFld.tequired = false
        }
        
        if(refreshList){
            $scope.filedsList = GetFiledsList($scope.item.id)
        }
        scopeApply()
    }

    function GetFiledsList(appid){
        var res = {}
        var data = {};
        data.appid = appid
        data.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val() 
        url = "/getfieldlist"
        $.ajax({
            url : url, 
            type : "POST", 
            data : data,
            async : false,
            success : function(json) {
                res = json.items
            },
            error : function(xhr,errmsg,err) {
                //debugger
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
        return res;
    }

    $scope.AddNewField = function(fld){
        $scope.InitField(false, fld)
        $('#FieldModal').modal('show')
    }

    $scope.AddUpateField = function(stItem, remove){

        debugger
        url = "/appsfieldupdate"
        if(remove){
            url = "/deleteappfield"
        }

        stItem.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

        $.ajax({
            url : url, 
            type : "POST",
            data : stItem,
            async:false,
            success : function(res) {
                debugger
                if(res.status == 0){
                    $scope.InitField(true)
                    $('#FieldModal').modal('hide')
                }
                else{
                    $.alert(res.error_essage)
                }
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                alert('Error' + err)
                debugger
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }
});