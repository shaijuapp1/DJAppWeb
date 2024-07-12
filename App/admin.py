from django.contrib import admin
from .AppList import AppList
from .AppStatus import AppStatus
from .AppData import AppData
from .AppFlow import AppFlow
from .AppConfig import AppConfig
from .AppFileds import AppFileds


admin.site.register(AppList) 
admin.site.register(AppStatus) 
admin.site.register(AppData) 
admin.site.register(AppFlow) 
admin.site.register(AppConfig) 
admin.site.register(AppFileds)
