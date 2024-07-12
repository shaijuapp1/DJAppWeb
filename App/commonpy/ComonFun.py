from django.http import JsonResponse

def GettPostVal(request, key, errlst, chkNull ):
    val = None
    try:
        val =  request.POST[key]
    except:
        val = ''

    if chkNull :
        CheckNullEmptyError(val, errlst, key)

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
