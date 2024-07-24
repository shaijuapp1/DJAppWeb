docApp.controller("AppListCtrl", function($scope) {

    $scope.init = function(){

        $scope.grps = GetUserGroups()
        $('.CreateGrpId').select2();

        $scope.item = {}
        $scope.newItem = true
        var id = window.location.pathname.split('/')[2]
        var data = {};
        if(id){                        
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

            $scope.InitStatus(true)
            $scope.InitAccess(true)
            $scope.InitField(true)
            $scope.InitFlow(true)
            $scope.InitView(true)

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
        
        if(!$scope.item.filelds){
            $scope.Filelds = []
        }
        else{
            $scope.Filelds = angular.fromJson($scope.item.filelds); 
        } 

        

        scopeApply($scope)
    }

    $scope.brnCacel = function() {
        window.location.href = '/applist ';
    };
    
    $scope.Save = function(){

        url = "/applistupdateajax"
        var req = $scope.item
        req.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

        req.create_goup_id = angular.toJson($scope.CreateGrpId)
        req.access = angular.toJson($scope.access_list);

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
                        $.alert('Saved.')
                    }
                    
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

    $scope.GetStatusText = function(id){
        res = ''
        for( i = 0;i< $scope.status_list.length;i++){
            if($scope.status_list[i].id == id ){
                res = $scope.status_list[i].status
                break
            }
        }
        return res
    }

    $scope.GetStatusListText = function(itmls){
        res = ''
        if(itmls){
            itms = angular.fromJson(itmls);
            itms.forEach(function(itm, index, array) {
    
                for( i = 0;i< $scope.status_list.length;i++){
                    if($scope.status_list[i].id == itm ){
                        if(res)
                            res += ", "
                        res += $scope.status_list[i].status
                        break
                    }
                }
            });
        }
        
        
        return res
    }

    $scope.GetGroupListText = function(grp){
        res = ''
        if(grp){
            grps = angular.fromJson(grp);
            grps.forEach(function(grp, index, array) {
    
                for( i = 0;i< $scope.grps.length;i++){
                    if($scope.grps[i].id == grp ){
                        if(res)
                            res += ", "
                        res += $scope.grps[i].name
                        break
                    }
                }
            });
        }
        
        
        return res
    }

    $scope.GetAccessText = function(id){
        res = ''
        for( i = 0;i< $scope.access_list.length;i++){
            if($scope.access_list[i].id == id ){
                res = $scope.access_list[i].name
                break
            }
        }
        return res
    }

    $scope.GetAccessListText = function(itmls){
        res = ''
        if(itmls){
            itms = angular.fromJson(itmls)
            itms.forEach(function(itm, index, array) {
                if(res)
                    res += ", "
                res += itm               
            });
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

    $scope.GetFiledText = function(id){
        res = ''
        if(id){ 
            for( i = 0;i< $scope.filedsList.length;i++){
                if($scope.filedsList[i].id == id ){
                    res = $scope.filedsList[i].title
                    break
                }
            }
        }   
        return res
    }

    //Filed functions - start

    $scope.InitField = function(refreshList, fld){
        //debugger
        if(fld && 'app_id' in fld){
            $scope.NewFld = fld
            $scope.NewFld.access = '' + $scope.NewFld.access
        }
        else{
            $scope.NewFld = {}
            $scope.NewFld.app_id = $scope.item.id
            $scope.NewFld.title = ''
            $scope.NewFld.type = ''
            $scope.NewFld.required = false
            $scope.NewFld.access = ''
            $scope.NewFld.order = 0
        }
        
        if(refreshList){
            $scope.filedsList = GetFiledsList($scope.item.id)
        }
        scopeApply($scope)
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
        scopeApply($scope)
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

    $scope.InitFlow = function(refreshList, obj){
        
        if(obj && 'app_id' in obj){

            flw = {...obj}
            flw.from_status = '' + flw.from_status
            flw.action_by_grp = '' + flw.action_by_grp
            flw.to_status = '' + flw.to_status
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
        scopeApply($scope)
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

    function GetAccessList(appid){
        var res = {}
        var data = {};
        data.appid = appid
        data.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val() 
        url = "/getaccesslist"
        $.ajax({
            url : url, 
            type : "POST", 
            data : data,
            async : false,
            success : function(json) {
                json.items.forEach(function(itm, index, array) {
                    itm.status = angular.fromJson(itm.status)
                    itm.group = angular.fromJson(itm.group)
                    itm.access = angular.fromJson(itm.access)
                })
                res = json.items
            },
            error : function(xhr,errmsg,err) {
                //debugger
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
        return res;
    }

    $scope.InitAccess = function(refreshList, obj){
        
        if(obj && 'app_id' in obj){
            $scope.new_acc = {...obj}
            $scope.new_acc.action_by_filed = '' + $scope.new_acc.action_by_filed
        }
        else{
            $scope.new_access = true
            $scope.new_acc = {}
            $scope.new_acc.app_id = $scope.item.id
            $scope.new_acc.order = 0
            $scope.new_acc.name = ''
            $scope.new_acc.status = ''
            $scope.new_acc.type = 'UserGroup'
            $scope.new_acc.group = ''
            $scope.new_acc.action_by_filed = ''
            $scope.new_acc.field = ''
            $scope.new_acc.access = ''
        }
        
        if(refreshList && $scope.item.id){
            $scope.access_list = GetAccessList($scope.item.id)
        }

        setTimeout(function(){ 		
            $('.new_acc_status' ).select2()
            $('.new_acc_group' ).select2()
            $('.new_acc_ccess' ).select2()  
        }, 50);

        scopeApply($scope)
    }

    $scope.AddNewAccess = function(acc){        
        obj = {...acc}
        $scope.InitAccess(false, obj)
        if(!$scope.access_list.order)
            $scope.new_acc.order = $scope.access_list.length + 1 
        $('#access_model').modal('show')        
    }

    $scope.DeleteAccess = function(stItem){
        $.confirm({
            title: 'Confirm!',
            content: 'Do yo want to delete!',
            buttons: {
                Cancel: function () {
                },
                Delete: function () {
                    $scope.AddUpateAccess(stItem, true)
                }
            }
        });
    }

    $scope.AddUpateAccess = function(stItem, remove){

        debugger
        url = "/appsaccessupdate"
        if(remove){
            url = "/deleteappaccess"
        }
        stItem.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
        var obj = {...stItem}
        obj.status =  angular.toJson(obj.status)
        obj.group =  angular.toJson(obj.group)
        obj.access =  angular.toJson(obj.access)

        $.ajax({
            url : url, 
            type : "POST",
            data : obj,
            async:false,
            success : function(res) {
                debugger
                if(res.status == 0){
                    $scope.InitAccess(true)
                    $('#access_model').modal('hide')
                }
                else{
                    $.alert(res.error_essage)
                }
            },
            error : function(xhr,errmsg,err) {
                alert('Error' + err)
                debugger
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }

    //Access functions - end

    //Status functions - start
    
    $scope.InitStatus = function(refreshList, obj){
        
        if(obj && 'app_id' in obj){

            $scope.new_st = {...obj}
        }
        else{
            $scope.new_st = {}
            $scope.new_st.app_id = $scope.item.id
            $scope.new_st.status = ''
            $scope.new_st.order = 0
        }
        
        if(refreshList && $scope.item.id){
            $scope.status_list = GetStatusList($scope.item.id)
        }
        scopeApply($scope)
    }

    $scope.AddNewStatus = function(itm){
        obj = {...itm}
        $scope.InitStatus(false, obj)
        if(!$scope.new_st.order)
            $scope.new_st.order = $scope.status_list.length + 1 
        $('#status_model').modal('show')
    }

    $scope.DeleteStatus = function(stItem){
        $.confirm({
            title: 'Confirm!',
            content: 'Do yo want to delete!',
            buttons: {
                Cancel: function () {
                },
                Delete: function () {
                    $scope.AddUpateStatus(stItem, true)
                }
            }
        });
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
                    $scope.InitStatus(true)
                    $('#status_model').modal('hide')
                }
                else{
                    $.alert(res.error_essage)
                }
            },
            error : function(xhr,errmsg,err) {
                alert('Error' + err)
                debugger
            }
        });
    }


     //Status functions - end

     //View functions - start

    $scope.InitView = function(refreshList, view){
        //debugger
        if(view && 'app_id' in view){
            $scope.new_v = view
        }
        else{
            $scope.new_v = {}
            $scope.new_v.app_id = $scope.item.id
            $scope.new_v.title = ''
            $scope.new_v.html = ''
            $scope.new_v.js = ''
            $scope.new_v.order = 0
        }
        
        if(refreshList){
            $scope.view_list = GetViewList($scope.item.id)
        }
        scopeApply($scope)
    }

    function GetViewList(appid){
        var res = {}
        var data = {};
        data.appid = appid
        data.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val() 
        url = "/getviewlist"
        $.ajax({
            url : url, 
            type : "POST", 
            data : data,
            async : false,
            success : function(json) {
                res = json.items
            },
            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText)
            }
        });
        return res;
    }

    $scope.AddNewView = function(view){
        obj = {...view}
        $scope.InitView(false, obj)
        if(!$scope.new_v.order)
            $scope.new_v.order = $scope.view_list.length + 1 
        $('#view_model').modal('show')
        scopeApply($scope)
    }
    
    $scope.AddUpateView = function(stItem, remove){

        debugger
        url = "/appsviewupdate"
        if(remove){
            url = "/deleteappview"
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
                    $scope.InitView(true)
                    $('#view_model').modal('hide')
                }
                else{
                    $.alert(res.error_essage)
                }
            },
            error : function(xhr,errmsg,err) {
                alert('Error' + err)
                debugger
            }
        });
    }

    $scope.DeleteView = function(stItem){
        $.confirm({
            title: 'Confirm!',
            content: 'Do yo want to delete!',
            buttons: {
                Cancel: function () {
                },
                Delete: function () {
                    $scope.AddUpateView(stItem, true)
                }
            }
        });
    }

    //View functions end

    
});