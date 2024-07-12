from django.db import models
from django.urls import reverse  
from django.contrib.auth.models import Group

import json
from django.http import JsonResponse

from App.commonpy.ComonFun import GettPostVal, UpdateError, HasUniqueAttribute, GettObjVal, CheckItemExitsInObjArray,api_responce
from .AppFileds import AppFileds


class AppList(models.Model):

  id = models.AutoField(primary_key=True)
  table = models.CharField(max_length=200)
  title = models.CharField(max_length=200)
  Filelds = models.TextField(default='')
  #filelds = models.ManyToManyField(AppFileds, related_name='appFileds')
  create_goup_id = models.CharField(max_length=200)
  access = models.TextField(default='')
  comment = models.TextField(default='')
  #CreateAccess = models.ManyToManyField(Group, related_name='my_models')

  def __str__(self):
        return str(self.id) + " - " + self.title + " - " + str(self.create_goup_id)  
  
  def get_absolute_url(self):  
     return reverse('AppList_edit', kwargs={'pk': self.pk})    
  
  def app_list_update_ajax(request):
    err = {'msg': ''}
    id = GettPostVal(request, 'id', err, False )
    table = GettPostVal(request, 'table', err, True ) 
    title = GettPostVal(request, 'title', err, True  )
    create_goup_id = GettPostVal(request, 'create_goup_id', err, False  )

    if not id: #New item
      if not err['msg']:
        item = AppList(table = table, title = title, create_goup_id = create_goup_id)
        item.save()
        return api_responce(item.id, 0)
      else:
        return api_responce(None, 1, err['msg'])
    else:
      return
      
    # get AppList id from request
    id = None
    try:
      id = request.POST['id']
    except Exception as e:
      return api_responce(id, 1, str(e))
    
    return ''
  
  def applist_details_ajax(request): #appdetails ajax
    err = {'msg': ''}
    id = GettPostVal(request, 'id', err, False )
    if id:
      try:
        item = AppList.objects.get(id=id)
        context = {
            'id': item.id,
            'table': item.table,
            'title': item.title,
            'create_goup_id': item.create_goup_id,
            'access': item.access,
            'comment': item.comment,
            'filelds': '',
        }
        
        response = json.dumps(context)
        #response = JsonResponse(context, safe=False)
        return api_responce(id, 0, None, context)

      except Exception as e:
        return api_responce(id, 1, str(e))
      
    else:
      return api_responce(None, 1, "Empty Id")



    # get AppList id from request
    id = None
    try:
      id = request.POST['id']
    except Exception as e:
      return api_responce(id, 1, str(e))
  
    #init context
    context = {
            'id': '',
            'table': '',
            'title': '',
            'filelds': [],
            'create_goup_id': '',
            'access': '',
            'comment': '',
        }
    
    try:
      item = AppList.objects.get(id=id)
      context = {
          'id': item.id,
          'table': item.table,
          'title': item.title,
          'create_goup_id': item.create_goup_id,
          'access': item.access,
          'comment': item.comment,
          'filelds': [],
      }

      flds = item.filelds.all()
      for fld in flds:
        fl = { 'id':0, 'title':'', type:f'', 'required':False }
        fl = { 'id':fld.id, 'title':fld.title, type:fld.type  }
        #context['filelds'].append(fl)

    except Exception as e:

      return api_responce(id, 1, "Error while getting data : " + str(e))

    try:
      response = JsonResponse(context, safe=False)
      return api_responce(id, 0, None, response)
    except Exception as e:
      return api_responce(id, 0, "Error while JsonResponse parsing : " + str(e))
      
  def app_list_update_ajax_old1(request):

    status = 0
    ErrorMessage = ''
    id = None
    err = {'msg': ''}

    id = None
    try:
        id = request.POST['id']
    except:
        id = None

    table = GettPostVal(request, 'table', err, True ) #request.POST['Table']
    title = GettPostVal(request, 'title', err, True  ) #request.POST['Title']
    create_goup_id = GettPostVal(request, 'create_goup_id', err, True  ) #request.POST['CreateGrpId']
    access = GettPostVal(request, 'access', err, True  ) #request.POST['Access']
    comment = GettPostVal(request, 'comment', err, False  ) #request.POST['Comment']
    filelds = GettPostVal(request, 'filelds', err, True  ) #request.POST['Filelds']
    fls =  json.loads(filelds)
     
    if id == None:
      item = AppList(table = table, title = title, create_goup_id = create_goup_id, access = access, comment = comment)
      item.save()

      flErr = {'msg': ''}
      for fldIem in fls:
        #fldId = GettObjVal(fldIem, 'id', flErr, False)
        title = GettObjVal(fldIem, 'Title', flErr, True)
        type = GettObjVal(fldIem, 'Type', flErr, True)
        required = GettObjVal(fldIem, 'Required', flErr, True)
        itmObj = AppFileds(title=title, type = type, required = required)
        itmObj.save()
        item.filelds.add(itmObj)

      try:
        item.save()
        id = item.id
      except Exception as e:
        ErrorMessage = str(e)
      
    else:
      item = AppList.objects.get(id=id)
      # item.Table = Table
      # item.Title = Title
      # #item.Filelds = flds
      # item.Filelds.add(flds)
      # item.CreateGrpId = CreateGrpId
      # item.Access = Access
      # item.Comment = Comment
      # item.save()

    return api_responce(id, 0, None)
  
    # data = {
    #     'id': id,
    #     'status' : status,
    #     'ErrorMessage' : ErrorMessage
    # }

    # response = JsonResponse(data)
    # response.status_code = 200
    # return response
    
  def AppListUpdateAjax_old(request): # Create/Update Ajax
    
    #status = 0
    err = {'msg': ''}
  
    id = None
    try:
        id = request.POST['id']
    except:
        id = None

    #v =  json.loads(item.Filelds)
    Table = GettPostVal(request, 'Table', err, True ) #request.POST['Table']
    Title = GettPostVal(request, 'Title', err, True  ) #request.POST['Title']
    Filelds = GettPostVal(request, 'Filelds', err, True  ) #request.POST['Filelds']
    CreateGrpId = GettPostVal(request, 'CreateGrpId', err, True  ) #request.POST['CreateGrpId']
    Access = GettPostVal(request, 'Access', err, True  ) #request.POST['Access']
    Comment = GettPostVal(request, 'Comment', err, False  ) #request.POST['Comment']

    NoErr = True

    try:
      fls =  json.loads(Filelds)
      unqTitle = HasUniqueAttribute(fls,'Title' )
      if not unqTitle:
         UpdateError(err, "Title shoud unique")
      else:
        dbFields = AppFileds.objects.filter(AppId=id)
        for item in fls:
          if id:
            #check item with same id exists in db
            flErr = {'msg': ''}
            fldId = GettObjVal(item, 'id', flErr, False)
            if fldId:
              itemExits = CheckItemExitsInObjArray(dbFields,'AppId',fldId)
              if not itemExits:
                UpdateError(err, "ID not exits")
              #else: #check data type is same or not

          
          
          #check anything removed

          #update if any Title/Required if changed

          # if new id 
          # Get new add into app filed
                 

          
          

          if flErr['msg'] is None:
            status = 0
          else:
            status = 1

          
          #if id:
          slMax = 20
      flds = []
      for item in fls:
        fldId = GettObjVal(item, 'id', flErr, False)
        title = GettObjVal(item, 'Title', flErr, True)
        type = GettObjVal(item, 'Type', flErr, True)
        required = GettObjVal(item, 'Required', flErr, True)
        fldItem = AppFileds(AppId = id, Title=title, Type = type, Required = required)
        flds.append(fldItem)



      if NoErr:
        if id == None:
          item = AppList(Table =Table, Title=Title,Filelds = flds, CreateGrpId=CreateGrpId, Access= Access, Comment = Comment)
          item.save()
          id = item.id
        else:
          item = AppList.objects.get(id=id)
          item.Table = Table
          item.Title = Title
          item.Filelds = flds
          item.CreateGrpId = CreateGrpId
          item.Access = Access
          item.Comment = Comment
          item.save()
        #  for item in fls:
        #     fldId = GettObjVal(item, 'id', flErr, False)
        #     title = GettObjVal(item, 'Title', flErr, True)
        #     type = GettObjVal(item, 'Type', flErr, True)
        #     required = GettObjVal(item, 'Required', flErr, True)

        #     if fldId == None:
        #         fldItem = AppFileds(AppId = id, Title=title, Type = type, Required = required)
        #         fldItem.save()
        #     else:
        #         fldItem = AppList.objects.get(id=fldId)
        #         item.AppId = id
        #         item.Title = title
        #         item.Type = type
        #         item.Required = required
        #         item.save()

      #if no error

    except Exception as e:
      UpdateError(err, "Invalid Filelds format {e}")


    #check title is unique

    status = 0
    if err['msg'] is None:
      status = 0
    else:
      status = 1
    
    data = {
        'id': id,
        'status' : status,
        'ErrorMessage' : err['msg']
    }
        
    response = JsonResponse(data)
    response.status_code = 200  # Setting a custom status code
    return response
  
    


    #Check unique title


