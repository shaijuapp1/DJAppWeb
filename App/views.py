from django.shortcuts import render
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.template import loader
from django.http import JsonResponse
from rest_framework.response import Response

from django.core.serializers import serialize

from  App.commonpy.serializers import GroupSerializer, StatusSerializer, FieldSerializer, AppFlowSerializer, AppAccessSerializer, AppViewSerializer
from django.contrib.auth.decorators import login_required
from .AppList import AppList
from .AppStatus import AppStatus
from django.contrib.auth.models import Group
from App.commonpy.ComonFun import GettPostVal
from .AppFileds import AppFileds
from .AppFlow import AppFlow
from .AppAccess import AppAccess
from .AppView import AppView

@login_required(login_url="/accounts/login/")
def home(request):
    test = 123
    return render(request, "home.html", {"test": test})

def about1(request):
    list = AppList.objects.all()
    s = ""  
    for l in list:
        #d = l.CreateAccess.all
        for g in l.CreateAccess.all():
            s += g.name + ", "
    return render(request, "about.html", {'list': list, "sss" : s})

#about - start
def about(request):
    #objects = models.Manager()

    list = AppList.Manager
    s = ""  
    return render(request, "about.html", {'list': list, "sss" : s})
#about - end

def test(request):
    return render(request, "test.html", {})

#AppList - start

def applist(request): #Listing Screen
    list = AppList.objects.all()
    return render(request, "AppList.html", { "list" : list })

def applistDetails(request, id=None): #Details Screen
     template = loader.get_template('AppListDetails.html')
     return HttpResponse(template.render({}, request))

def applistDetailsAjax(request): #appdetails ajax
    return AppList.applist_details_ajax(request)

def AppListUpdateAjax(request): # Create/Update Ajax
    return AppList.app_list_update_ajax(request)

  
#AppList - end

#Group - start

def getGroupList(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    data = {
        'grps': serializer.data
    }
    response = JsonResponse(data)
    response.status_code = 200
    return response
       
#Group - end

#Status - start

def app_status_update_ajax(request):
    return AppStatus.app_status_update_ajax(request)

def get_status_list_ajax(request):
    #return AppStatus.get_status_list_ajax(request)
    appid = request.POST['appid']
    items = AppStatus.objects.filter(app_id=appid)
    serializer = StatusSerializer(items, many=True)

    data = {
        'status': serializer.data
    }
    response = JsonResponse(data)
    response.status_code = 200
    return response

def app_status_delete_ajax(request):
    return AppStatus.app_status_delete_ajax(request)
#Status - end


#DB Field
def app_field_update_ajax(request):
    return AppFileds.app_field_update_ajax(request)

def get_field_list_ajax(request):
    appid = request.POST['appid']
    items = AppFileds.objects.filter(app_id=appid)
    serializer = FieldSerializer(items, many=True)
    data = {
        'items': serializer.data
    }
    response = JsonResponse(data)
    response.status_code = 200
    return response

# Flow Start

def app_flow_update_ajax(request):
    return AppFlow.app_flow_update_ajax(request)

def get_flow_list_ajax(request):
    appid = request.POST['appid']
    items = AppFlow.objects.filter(app_id=appid)
    try:
        serializer = AppFlowSerializer(items, many=True)
        data = {
            'items': serializer.data
        }
        response = JsonResponse(data)
        response.status_code = 200
        return response

    except Exception as e:
        #return api_responce(id, 1, str(e))
        s = str(e)
    
# Flow end

# Access start
def app_access_update_ajax(request):
    return AppAccess.app_access_update_ajax(request)

def get_access_list_ajax(request):
    appid = request.POST['appid']
    items = AppAccess.objects.filter(app_id=appid)
    try:
        serializer = AppAccessSerializer(items, many=True)
        data = {
            'items': serializer.data
        }
        response = JsonResponse(data)
        response.status_code = 200
        return response

    except Exception as e:
        #return api_responce(id, 1, str(e))
        s = str(e)

def app_access_delete_ajax(request):
    return AppAccess.app_access_delete_ajax(request)
# Access end

# View start
def app_view_update_ajax(request):
    return AppView.app_view_update_ajax(request)

def get_view_list_ajax(request):
    appid = request.POST['appid']
    items = AppView.objects.filter(app_id=appid)
    try:
        serializer = AppViewSerializer(items, many=True)
        data = {
            'items': serializer.data
        }
        response = JsonResponse(data)
        response.status_code = 200
        return response

    except Exception as e:
        s = str(e)

def app_view_delete_ajax(request):
    return AppView.app_view_delete_ajax(request)

def app_view_ajax(request):
    return AppView.app_view_ajax(request)


# View end

#Data API

def take_action(request):
    err = {'msg': ''}
    list_id = GettPostVal(request, 'list_id', err, False )
    flow_id = GettPostVal(request, 'flow_id', err, False )
    app_id = GettPostVal(request, 'app_id', err, True  )
    item_json = GettPostVal(request, 'col_json', err, True ) 
    data_json = GettPostVal(request, 'filter_json', err, True  )

    
    return ''

def get_list(request):
    err = {'msg': ''}
    flow_id = GettPostVal(request, 'flow_id', err, False )
    app_id = GettPostVal(request, 'app_id', err, True  )
    col_json = GettPostVal(request, 'col_json', err, True ) 
    filter_json = GettPostVal(request, 'filter_json', err, True  )
    return ''

#Data API - end