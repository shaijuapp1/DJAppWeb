from django.db import models
from django.urls import reverse  
import json

from App.commonpy.ComonFun import GettPostVal, api_responce, UpdateError
from .AppList import AppList
from .AppFileds import AppFileds
from .AppFlow import AppFlow

class AppStatus(models.Model):
  id = models.AutoField(primary_key=True)
  app_id = models.IntegerField(default=0)
  status = models.CharField(max_length=200)
  order = models.IntegerField(default=0)
  
  def __str__(self):
        return str(self.id) + " : " + str(self.app_id) + " : " + self.status + " : " + str(self.order)
  
  def get_absolute_url(self):  
     return reverse('AppStatus_edit', kwargs={'pk': self.pk})
  
  def app_status_update_ajax(request):    
      err = {'msg': ''}
      id = GettPostVal(request, 'id', err, False )
      app_id = GettPostVal(request, 'app_id', err, True  )
      status = GettPostVal(request, 'status', err, True  )
      order = GettPostVal(request, 'order', err, False, 'int'  )

      if not id: #New item
            if not err['msg']:
                  item = AppStatus(status = status, app_id = app_id, order = order)
                  item.save()
                  return api_responce(item.id, 0)     
            else:
                  return api_responce(None, 1,err['msg'])       
      else:
            item = AppStatus.objects.get(id=id)
            item.status = status
            item.order = order
            item.save()
            return api_responce(item.id, 0)
      
  def app_status_delete_ajax(request):
      err = {'msg': ''}
      id = GettPostVal(request, 'id', err, True )
      if id: #New item
            valErr = {'msg': ''}
            item = AppStatus.objects.get(id=id)

            #Access
            app_list = AppList.objects.get(id=item.app_id)
            access = app_list.access
            access_lst = json.loads(access)
            for asl in access_lst: 
                 for ac in asl['status']: 
                      if ac == id:
                           UpdateError(valErr, "Status is using in access " + asl['name'] )
                           break
                                              
            #Flow
            app_flows = AppFlow.objects.filter(app_id=item.app_id)
            for flow in app_flows:
                  if str(flow.from_status) == id:
                        UpdateError(valErr, "Status is using in Flow From Status  for action " + flow.action )
                        break
                  if str(flow.to_status) == id:
                        UpdateError(valErr, "Status is using in Flow To Status for action " + flow.action )
                        break
                 
            if valErr['msg']: return api_responce(None, 1, valErr['msg'])                                             
            item.delete()
            return api_responce(item.id, 0)
      else:
            return api_responce(None, 1,err['msg'])
  
