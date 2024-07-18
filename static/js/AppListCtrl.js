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
        $scope.InitFlow(true)

        scopeApply()
    }

    $scope.brnCacel = function() {
        window.location.href = '/applist ';
    };
    
    $scope.Save = function(){

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

    $scope.GetStatusText = function(id){
        res = ''
        for( i = 0;i< $scope.statusList.length;i++){
            if($scope.statusList[i].id == id ){
                res = $scope.statusList[i].status
                break
            }
        }
        return res
    }

    $scope.GetGroupText = function(id){
        res = ''
        for( i = 0;i< $scope.grps.length;i++){
            if($scope.grps[i].id == id ){
                res = $scope.grps[i].name
                break
            }
        }
        return res
    }

    //Filed functions - start

    $scope.InitField = function(refreshList, fld){
        //debugger
        if(fld){
            $scope.NewFld = fld
        }
        else{
            $scope.NewFld = {}
            $scope.NewFld.app_id = $scope.item.id
            $scope.NewFld.title = ''
            $scope.NewFld.type = ''
            $scope.NewFld.tequired = false
            $scope.NewFld.order = 0
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
        obj = {...fld}
        $scope.InitField(false, obj)
        $('#FieldModal').modal('show')
        scopeApply()
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

    //Filed functions end

    //Flow functions

    function GetFlowsList(appid){
        debugger
        var res = {}
        var data = {};
        data.appid = appid
        data.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val() 
        url = "/getflowlist"
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

    $scope.InitFlow = function(refreshList, flw){
        
        if(flw && 'app_id' in obj){

            flw = {...obj}
            flw.from_status = '' + flw.from_status
            flw.action_by_grp = '' + flw.action_by_grp
            flw.to_status = '' + flw.from_status
            flw.action_by_filed = '' + flw.action_by_filed

            $scope.NewFlw = flw
        }
        else{
            $scope.NewFlw = {}
            $scope.NewFlw.app_id = $scope.item.id
            $scope.NewFlw.from_status = ''
            $scope.NewFlw.action_by_type = 'Group'
            $scope.NewFlw.action_by_grp = 0
            $scope.NewFlw.action_by_filed = ''
            $scope.NewFlw.action = ''
            $scope.NewFlw.to_status = 0
            $scope.NewFlw.custom_action = ''
            $scope.NewFlw.order = 0
        }
        
        if(refreshList){
            $scope.flowsList = GetFlowsList($scope.item.id)
        }
        scopeApply()
    }

    $scope.AddNewFlow = function(fld){
        obj = {...fld}
        $scope.InitFlow(false, obj)
        if(!$scope.NewFlw.order)
            $scope.NewFlw.order = $scope.flowsList.length + 1 
        $('#FlowModal').modal('show')
    }

    $scope.AddUpateFlow = function(stItem, remove){

        debugger
        url = "/appsflowupdate"
        if(remove){
            url = "/deleteappflow"
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
                    $scope.InitFlow(true)
                    $('#FlowModal').modal('hide')
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

    //Flow functions - end


    //Access functions - start

    $scope.AddNewAccess = function(){

        var ac = {}
        ac.Status = ''
        ac.Type = 'UserGroup'
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

    //Access functions - end
});