from django.db import models
from django.urls import reverse  
from App.commonpy.ComonFun import GettPostVal, UpdateError, HasUniqueAttribute, GettObjVal, CheckItemExitsInObjArray,api_responce
#from  App.commonpy.serializers import StatusSerializer
from django.http import JsonResponse


class AppStatus(models.Model):
  id = models.AutoField(primary_key=True)
  app_id = models.IntegerField(default=0)
  status = models.CharField(max_length=200)
  order = models.IntegerField(default=0)
  
  def __str__(self):
        return str(self.id) + " : " + str(self.app_id) + " : " + self.status
  
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
            item = AppStatus.objects.get(id=id)
            item.status = status
            item.order = order
            item.save()
            return api_responce(item.id, 0)
      
  def app_status_delete_ajax(request):
      err = {'msg': ''}
      id = GettPostVal(request, 'id', err, True )
      if id: #New item
           item = AppStatus.objects.get(id=id)
           item.delete()
           return api_responce(item.id, 0)
      else:
            return api_responce(None, 1,err['msg'])
  
#   def get_status_list_ajax(request):
#     appid = request.POST['appid']
#     items = AppStatus.objects.filter(app_id=appid)
#     serializer = StatusSerializer(items, many=True)

#     data = {
#         'status': serializer.data
#     }
#     response = JsonResponse(data)
#     response.status_code = 200
#     return response