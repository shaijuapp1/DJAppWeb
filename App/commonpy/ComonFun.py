from django.http import JsonResponse
from django.contrib.auth.models import Group

def GettPostVal(request, key, errlst, chkNull, ToNum = 'string' ):
    val = None
    try:
        val =  request.POST[key]
    except:
        val = ''

    if chkNull :
        CheckNullEmptyError(val, errlst, key)
    
    if ToNum == 'int':
        try:
            val =  int(val)
        except:
            if chkNull:
                UpdateError(errlst, "Invlaid integer value for " + key)
            val = 0
    
    if ToNum == 'float':
        try:
            val =  float(val)
        except:
            if chkNull:
                UpdateError(errlst, "Invlaid float value for " + key)
            val = 0
    
    if ToNum == 'bool':
        if val.lower() == 'true':
            val = True
        elif val.lower() == 'false':
            val = False
        else:
            if chkNull:
                UpdateError(errlst, "Invlaid bool value(True/False) for " + key)

    return val
    
def GettObjVal(item, attribute, errlst, chkNull ):
    val = None
    try:
        val = item[attribute]
    except:
        val = None

    if chkNull :
        CheckNullEmptyError(val, errlst, attribute)

    return val

def UpdateError(errlst, err):
    if errlst['msg'] is None or errlst['msg'] == '':
        errlst['msg'] = err
    else:
        errlst['msg'] +=  ", " + err
 
def CheckNullEmptyError(val, errlst, title):
    if val is None or val == '':
        return UpdateError(errlst, "Empty/Invlaid " + title)
    else:
        return None
    
def HasUniqueAttribute(objects, attribute):
    seen = set()
    for obj in objects:
        value = obj[attribute]
        if value in seen:
            return False
        seen.add(value)
    return True

def CheckItemExitsInObjArray(objects, attribute, val):
    for obj in objects:
        value = obj[attribute]
        if value == val:
            return False
    return True

def api_responce(id, status, error_essage = None, details = None):
    data = {
        'id': id,
        'status' : status,
        'error_essage' : error_essage,
        'details' : details
    }
    response = JsonResponse(data, safe=False)
    response.status_code = 200 
    return response

def save_model_and_api_responce(item, id = None):
    try: 
        item.save()
        return api_responce(item.id, 0)
    except Exception as e:
        return api_responce(id, 1, str(e))
    
def is_float(value):
    if isinstance(value, str):
        # Remove leading/trailing whitespace and check if it's a digit or a float
        value = value.strip()
        if value.count('.') == 1:
            left, right = value.split('.')
            return (left.isdigit() or left == '') and right.isdigit()
        return value.isdigit() or (value.count('.') == 1 and value.replace('.', '', 1).isdigit())
    return False
    
def check_user_in_group(request, group_id, err ):
    if request.user.is_authenticated:
        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            err['msg'] = "User not exists in group " + str(group_id)
            return False
        return request.user.groups.filter(id=group.id).exists()
    return False