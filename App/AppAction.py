from django.db import models
from App.commonpy.ComonFun import GettPostVal, api_responce

from .AppFileds import AppFileds
from .AppFlow import AppFlow
from .AppAccess import AppAccess

def take_action(request):
    err = {'msg': ''}
    app_id = GettPostVal(request, 'app_id', err, True, 'int' )
    flow_id = GettPostVal(request, 'flow_id', err, True, 'int' )
    item_id = GettPostVal(request, 'item_id', err, False, 'int' )
    data_json = GettPostVal(request, 'data_json', err, True )

    if err['msg']:
            return api_responce(None, 1, err['msg'])

    #1. Get appdatails a. Access   b. Filed c. Flow
    flw_lst = AppFlow.objects.filter(id=flow_id)
    

    acc_lst = AppAccess.objects.filter(app_id=app_id)
    
    fld_lst = AppFileds.objects.filter(app_id=app_id)


    

    