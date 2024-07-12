from django.db import models
from django.urls import reverse  
from django.contrib.auth.models import Group
from App.commonpy.ComonFun import GettPostVal, api_responce
class AppFlow(models.Model):
  id = models.AutoField(primary_key=True)
  from_status = models.IntegerField(default=0)
  action_by_type = models.CharField(max_length=200)
  action_by = models.IntegerField(default=0)
  action = models.CharField(max_length=200)
  to_status = models.IntegerField(default=0)
  custom_action = models.TextField()
  
  def __str__(self):
        return str(self.id) + " - " + self.action
  
  def get_absolute_url(self):  
     return reverse('AppList_edit', kwargs={'pk': self.pk})
  

  def app_flow_update_ajax(request):
      err = {'msg': ''}
      id = GettPostVal(request, 'id', err, False )
      from_status = GettPostVal(request, 'from_status', err, True  )
      action_by_type = GettPostVal(request, 'action_by_type', err, True  )
      action = GettPostVal(request, 'action', err, True  )
      to_status = GettPostVal(request, 'to_status', err, True  )
      custom_action = GettPostVal(request, 'custom_action', err, False  )

      if err['msg']:
            return api_responce(None, 1, err['msg'])
                 

      if not id: #New item
            item = AppFlow(from_status = from_status, action_by_type = action_by_type, action = action, to_status = to_status, custom_action = custom_action)
            try:
                  item.save()
            except Exception as e:
                  return api_responce(id, 1, str(e))            
            return api_responce(item.id, 0)                        
      else:
            item = AppFlow.objects.get(id=id)
            item.from_status = from_status
            item.action_by_type = action_by_type
            item.action = action
            item.to_status = to_status
            item.custom_action = custom_action
            item.save()
            return api_responce(item.id, 0)