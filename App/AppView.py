from django.db import models
from django.urls import reverse  
from App.commonpy.ComonFun import GettPostVal, api_responce

class AppView(models.Model):
  id = models.AutoField(primary_key=True)
  order = models.IntegerField(default=0)
  app_id = models.IntegerField(default=0)
  title = models.CharField(max_length=200)
  html = models.TextField()
  js = models.TextField()
  
  def __str__(self):
        return str(self.id) + " : " + str(self.app_id) + " : " + self.title + " : " + str(self.order)
  
  def get_absolute_url(self):  
     return reverse('AppStatus_edit', kwargs={'pk': self.pk})
  
  def app_view_update_ajax(request):    
      err = {'msg': ''}
      id = GettPostVal(request, 'id', err, False )
      app_id = GettPostVal(request, 'app_id', err, True  )
      title = GettPostVal(request, 'title', err, True  )
      order = GettPostVal(request, 'order', err, False, 'int'  )
      html = GettPostVal(request, 'html', err, True  )
      js = GettPostVal(request, 'js', err, False  )

      if err['msg']:
            return api_responce(None, 1, err['msg'])

      if not id: #New item
            if not err['msg']:
                  item = AppView(app_id = app_id, order = order, title = title, html = html, js = js )
                  item.save()
                  return api_responce(item.id, 0)     
            else:
                  return api_responce(None, 1,err['msg'])       
      else:
            item = AppView.objects.get(id=id)
            item.order = order
            item.html = html
            item.title = title
            item.js = js
            item.save()
            return api_responce(item.id, 0)
      
  def app_view_delete_ajax(request):
      err = {'msg': ''}
      id = GettPostVal(request, 'id', err, True )
      if id: #New item
            valErr = {'msg': ''}
            item = AppView.objects.get(id=id)
                             
            if valErr['msg']: return api_responce(None, 1, valErr['msg'])                                             
            item.delete()
            return api_responce(item.id, 0)
      else:
            return api_responce(None, 1,err['msg'])
  
  def app_view_ajax(request):
      err = {'msg': ''}
      id = GettPostVal(request, 'id', err, True )
       
