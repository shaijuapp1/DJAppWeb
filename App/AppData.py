from django.db import models
from django.urls import reverse  

class AppData(models.Model):
  id = models.AutoField(primary_key=True)
  app_id = models.IntegerField(default=0)
  status_id = models.IntegerField(default=0)
  created = models.DateTimeField(auto_now=True)
  created_by = models.IntegerField(default=0)
  modified = models.DateTimeField(auto_now=True)
  modified_by = models.DateTimeField(auto_now=True)

  s1 = models.TextField()
  s2 = models.TextField()
  s3 = models.TextField()
  s4 = models.TextField()
  s5 = models.TextField()
  s6 = models.TextField()
  s7 = models.TextField()
  s8 = models.TextField()
  s9 = models.TextField()
  s10 = models.TextField()
  s11 = models.TextField()
  s12 = models.TextField()
  s13 = models.TextField()
  s14 = models.TextField()
  s15 = models.TextField()
  s16 = models.TextField()
  s17 = models.TextField()
  s18 = models.TextField()
  s19 = models.TextField()
  s20 = models.DateTimeField(auto_now=True)
  d1 = models.DateTimeField(auto_now=True)
  d2 = models.DateTimeField(auto_now=True)
  d3 = models.DateTimeField(auto_now=True)
  d4 = models.DateTimeField(auto_now=True)
  d5 = models.DateTimeField(auto_now=True)
  d6 = models.DateTimeField(auto_now=True)
  d7 = models.DateTimeField(auto_now=True)
  d8 = models.DateTimeField(auto_now=True)
  d9 = models.DateTimeField(auto_now=True)
  d10 = models.DateTimeField(auto_now=True)
  u1 = models.IntegerField(default=0)
  u2 = models.IntegerField(default=0)
  u3 = models.IntegerField(default=0)
  u4 = models.IntegerField(default=0)
  u5 = models.IntegerField(default=0)
  g1 = models.IntegerField(default=0)
  g2 = models.IntegerField(default=0)
  g3 = models.IntegerField(default=0)
  g4 = models.IntegerField(default=0)
  g5 = models.IntegerField(default=0)
  n1 = models.FloatField(default=0.0)
  n2 = models.FloatField(default=0.0)
  n3 = models.FloatField(default=0.0)
  n4 = models.FloatField(default=0.0)
  n5 = models.FloatField(default=0.0)
  n6 = models.FloatField(default=0.0)
  n7 = models.FloatField(default=0.0)
  n8 = models.FloatField(default=0.0)
  n9 = models.FloatField(default=0.0)
  n10 = models.FloatField(default=0.0)

  def __str__(self):
        return str(self.id) + " : " + str(self.app_id) + " : " + str(self.status_id)
  
  def get_absolute_url(self):  
     return reverse('AppStatus_edit', kwargs={'pk': self.pk})