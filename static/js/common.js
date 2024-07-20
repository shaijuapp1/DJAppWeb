function Test(p){
    alert(p)
}

function scopeApply($scope){
    try {
        $scope.$apply()
    } catch (innerError) {
        console.error('Inner Error:', innerError.message);
    }
}

function GetUserGroups(){
    var res = {}
    var data = {};
    data.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val() 
    url = "/getGroupList/"
    $.ajax({
        url : url, 
        type : "POST",
        data : data,
        async : false,
        success : function(json) {
            res = json.grps
        },
        error : function(xhr,errmsg,err) {
            debugger
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });

    return res;
    
}

function GetStatusList(appid){

    var res = {}
    var data = {};
    data.appid = appid
    data.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val() 
    url = "/getstatuslist/"
    $.ajax({
        url : url, 
        type : "POST", 
        data : data,
        async : false,
        success : function(json) {
            res = json.status
        },
        error : function(xhr,errmsg,err) {
            //debugger
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
    return res;
}

