from django.db import models
from django.urls import reverse  
from App.commonpy.ComonFun import GettPostVal, api_responce
from django.http import JsonResponse


class AppFileds(models.Model):
  id = models.AutoField(primary_key=True)
  app_id = models.IntegerField(default=0)
  title = models.CharField(max_length=200)
  type = models.CharField(max_length=200)
  required = models.BooleanField (default=False)
  db_field = models.CharField(max_length=200, default='')
  order = models.IntegerField(default=0)
  
  def __str__(self):
        return str(self.id) + ' - ' + self.title + ' - ' + self.type + ' - ' + self.db_field+ ' - ' + str(self.app_id)
  
  def get_absolute_url(self):  
     return reverse('AppStatus_edit', kwargs={'pk': self.pk})
        
        
  def app_field_update_ajax(request):
      err = {'msg': ''}
      id = GettPostVal(request, 'id', err, False, 'int' )
      title = GettPostVal(request, 'title', err, True  )
      required = GettPostVal(request, 'required', err, False, 'bool'  )
      type = GettPostVal(request, 'type', err, True  )
      app_id = GettPostVal(request, 'app_id', err, True , 'int'  )
      order = GettPostVal(request, 'order', err, False, 'int'  )
      
      item = None
      apItms = None
      if id:
            item = AppFileds.objects.get(id=id)
            if app_id != item.app_id:
                  return api_responce(None, 1, "Diffrent app_id.")
            if type != item.type:
                  return api_responce(None, 1, "Diffrent type, cant update type.")
      
      if not err['msg']:
            if id:
                  
                  apItms = AppFileds.objects.exclude(id = id).filter(app_id = app_id).filter(title = title)
            else:
                  apItms = AppFileds.objects.filter(app_id = app_id).filter(title = title)
            
            if apItms:
                  return api_responce(None, 1, "Title already existing.")
      else:
            return api_responce(None, 1, err['msg'])
      
      if not id: #New item
            #get db_filed
            db_field = get_next_db_field(app_id, type)
            if db_field:
                  item = AppFileds(
                              app_id = app_id, 
                              title = title, 
                              required = required, 
                              db_filed = db_field, 
                              type = type,
                              order = order
                        )
                  try:
                        item.save()
                  except Exception as e:
                        return api_responce(id, 1, str(e))
                  
                  return api_responce(item.id, 0)    
            else:
                  return api_responce(None, 1, "Empty DB field")                   
      else:
            item.title = title
            item.required = required
            item.order = order
            item.save()
            return api_responce(item.id, 0)

def get_next_db_field(app_id, type):

      if type == 'Text':
            prefix = "s"
            count = 20
      elif type == 'Date':
            prefix = "d"
            count = 10
      elif type == 'User':
            prefix = "u"
            count = 5
      elif type == 'Number':
            prefix = "n"
            count = 10

      db_field = ''
      try:
            apItms = AppFileds.objects.filter(app_id = app_id).filter(type = type)
            for c in range(1, count):
                  fn = prefix + str(c)
                  newFiled = True
                  if apItms :
                        for ap in apItms:
                              if ap.db_field == fn:
                                    newFiled = False
                                    break
                        if newFiled:
                              db_field = fn
                              break
                  else:
                       db_field = fn 
                       break

            return db_field

      except Exception as e:
            return None
      
      
  
