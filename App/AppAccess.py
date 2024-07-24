from django.db import models
from django.urls import reverse  
from django.contrib.auth.models import Group
from App.commonpy.ComonFun import GettPostVal, api_responce, save_model_and_api_responce, UpdateError
from .AppFileds import AppFileds

class AppAccess(models.Model):
  id = models.AutoField(primary_key=True)
  app_id = models.IntegerField(default=0)
  order = models.IntegerField(default=0)
  name = models.CharField(max_length=600)
  status = models.CharField(max_length=600)
  type = models.CharField(max_length=600)
  group = models.CharField(max_length=600, null = True)
  action_by_filed = models.CharField(max_length=600, null = True)
  field = models.IntegerField(default=0, null = True)
  access = models.CharField(max_length=600)
  
  
  def __str__(self):
        return str(self.app_id) + " - " + str(self.order) + " - " + self.name
  
  def get_absolute_url(self):  
     return reverse('AppList_edit', kwargs={'pk': self.pk})
  

  def app_access_update_ajax(request):
      err = {'msg': ''}
      id = GettPostVal(request, 'id', err, False, 'int' )
      app_id = GettPostVal(request, 'app_id', err, True, 'int' )
      order = GettPostVal(request, 'order', err, False, 'int'  )
      name = GettPostVal(request, 'name', err, True  )
      status = GettPostVal(request, 'status', err, True  )
      type = GettPostVal(request, 'type', err, True  )            
      field = GettPostVal(request, 'group', err, True  )
      access = GettPostVal(request, 'access', err, True  )

      if type == 'Text' :
            field = GettPostVal(request, 'field', err, True  )
      else:
           field = None

      if type == 'UserGroup' :
            group = GettPostVal(request, 'group', err, True  )    
            action_by_filed = None        
      else:
            action_by_filed = GettPostVal(request, 'action_by_filed', err, True , 'int' )
            group = None
           

      if err['msg']:
            return api_responce(None, 1, err['msg'])
                 
      if not id:
            item = AppAccess(
                        app_id = app_id,                         
                        order = order,
                        name = name, 
                        status = status, 
                        type = type, 
                        group = group, 
                        action_by_filed = action_by_filed, 
                        field = field, 
                        access = access, 
                  )
            return save_model_and_api_responce(item)
      else:
            item = AppAccess.objects.get(id=id)
            item.order = order
            item.name = name
            item.status = status
            item.type = type
            item.group = group            
            item.action_by_filed = action_by_filed
            item.field = field
            item.access = access            
            return save_model_and_api_responce(item)
  
  def app_access_delete_ajax(request):
      err = {'msg': ''}
      id = GettPostVal(request, 'id', err, True )
      if id: #New item
            valErr = {'msg': ''}
            item = AppAccess.objects.get(id=id)            
                                              
            #AppFileds
            fld = AppFileds.objects.filter(access=id)
            if fld:
                  UpdateError(valErr, "Access is using in field"  )     
            if valErr['msg']: return api_responce(None, 1, valErr['msg'])    

            item.delete()
            return api_responce(item.id, 0)
      else:
            return api_responce(None, 1,err['msg'])
  