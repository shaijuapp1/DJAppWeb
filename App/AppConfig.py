from django.db import models
from django.urls import reverse  

class AppConfig(models.Model):
  id = models.AutoField(primary_key=True)
  type = models.CharField(max_length=200)
  title = models.CharField(max_length=200)
  value = models.TextField()
  
  def __str__(self):
        return str(self.id) + " : " + self.title
  
  def get_absolute_url(self):  
     return reverse('AppStatus_edit', kwargs={'pk': self.pk})