from django.db import models
import json
from datetime import datetime

from App.commonpy.ComonFun import GettPostVal, api_responce, GettObjVal, save_model_and_api_responce, UpdateError, is_float, check_user_in_group
from .AppFileds import AppFileds
from .AppFlow import AppFlow
from .AppAccess import AppAccess
from .AppData import AppData


def _take_action(request): 
    err = {'msg': ''}
    app_id = GettPostVal(request, 'app_id', err, True, 'int' )
    flow_id = GettPostVal(request, 'flow_id', err, True, 'int' )
    item_id = GettPostVal(request, 'item_id', err, False, 'int' )
    data_json = GettPostVal(request, 'data_json', err, True )

    if err['msg']:
            return api_responce(None, 1, err['msg'])

    #1. Get appdatails a. Access   b. Filed c. Flow
    flw_lst = AppFlow.objects.filter(id=flow_id)
    if not (flw_lst and flw_lst[0].id):
        return  api_responce(None, 1, "Invalid flow")
    
    data_obj = None
    try:
        data_obj = json.loads(data_json)
    except Exception as e:
        return None
    
    #check user having flow access on current status
    acc_det = {
           'status' : flw_lst[0].from_status,
           'type' : flw_lst[0].action_by_type,
           'group' : flw_lst[0].action_by_grp,
           'action_by_filed' : flw_lst[0].action_by_filed
        }
#     x = flw_lst[0].from_status
#     acc_det.status = flw_lst[0].from_status
#     acc_det.type = flw_lst[0].action_by_type
#     acc_det.group = flw_lst[0].action_by_grp
#     acc_det.action_by_filed = flw_lst[0].action_by_filed

    vaid_flow_user = check_access(request, acc_det, data_obj, '' , err)

    #check user having flow access
    if not vaid_flow_user :
        return  api_responce(None, 1, err['msg'])
    
    acc_lst = AppAccess.objects.filter(app_id=app_id)
    
    err = {'msg': ''}
    item = AppData()
    fld_lst = AppFileds.objects.filter(app_id=app_id)
    for fldIem in fld_lst:
        acc_id = GettObjVal(data_obj, 'access', err, False)
        val = get_data_item(data_obj, fldIem, err)
        
        if err['msg'] :
                break
        else:
                if acc_id:
                        vaild_access = check_filed_access(request, acc_lst, acc_id, data_obj, fldIem, err)
                else:
                       vaild_access = True

                if vaild_access:               
                        setattr(item, fldIem.db_field, val)

    if err['msg'] :     
        return  api_responce(None, 1, err['msg'])
    else:
        if not item_id:
                return save_model_and_api_responce(item)
        
    
    #access
    #user id validation
    return  api_responce(None, 1, "Test")

def check_filed_access(request, acc_lst, acc_id, data_obj, fldIem, err):
        res = False
        for itm in acc_lst:
                if GettObjVal(itm, 'id', err, True ) == acc_id :
                        if hasattr(itm, 'access') :
                                res = itm.access
                        else:
                                res = check_access(request,itm, data_obj,fldIem, err )
                                setattr(itm, 'access', res)
                        break
        return res
       
def check_access(request, acc_det, data_obj, fldIem, err):
        # acc_det.status = flw_lst.from_status
        # acc_det.type = flw_lst.action_by_type
        # acc_det.group = flw_lst.action_by_grp
        # acc_det.action_by_filed = flw_lst.action_by_filed
        type = acc_det['type']
        if type == "Group":
                return check_user_in_group(request, acc_det['group'], err)
        elif type == "UserGroup":
                s=1
        elif type == "User":
                s=1
        elif type == "User":
                s=1
               
        return False
     
def get_data_item(data_obj, fldIem, err):
        val = GettObjVal(data_obj, fldIem.title, err, fldIem.required)
        type = fldIem.type
        if not err['msg'] and val: 
                if type == 'Date':
                        try:
                                format = '%d-%m-%Y'
                                datetime.strptime(type, format)
                                return True
                        except ValueError:
                                UpdateError(err, "Empty/Invlaid date " + fldIem.title)
                elif type == 'User':
                        prefix = "u"
                elif type == 'Number':
                        if not is_float(val):
                                UpdateError(err, "Empty/Invlaid Number " + fldIem.title)
                
        if not val:
               if type == 'User':
                      val = 0
               elif type == 'Number':
                      val = 0
        return val