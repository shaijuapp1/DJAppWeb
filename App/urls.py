from django.urls import path
from . import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.home, name="home"),


    #applist
    path("applist/", views.applist, name="applist"), #Listing Screen
    path("applistdetails", views.applistDetails, name="applistdetails"), #Details Screen - new
    path("applistdetails/<str:id>", views.applistDetails, name="applistdetails"), #Details Screen
    path("applistdetailsajax", views.applistDetailsAjax, name="AppDetails"), #appdetails ajax
    path("applistupdateajax", views.AppListUpdateAjax, name="applistupdate"),


    path("about/", views.about, name="about"),
    path("test/", views.test, name="test"),

    path("getGroupList/", views.getGroupList, name="getGroupList"),


    #getStatusList
    path("appstatusupdate", views.app_status_update_ajax, name="appstatusupdate"),
    path("getstatuslist/", views.get_status_list_ajax, name="getstatuslist"),
    path("deleteappstatus", views.app_status_delete_ajax, name="deleteappstatus"),
    #app_status_delete_ajax

    path("appsfieldupdate", views.app_field_update_ajax, name="appsfieldupdate"),
    path("getfieldlist", views.get_field_list_ajax, name="getfieldlist"),
    #path("deleteappfield", views.app_status_delete_ajax, name="deleteappfield"),

    #path("getGroupLista", views.applistDetailsAjax, name="AppDetails"), #appdetails ajax



    #path("appnew/", views.addAppList, name="appnew"),

    
    #path("appdetails/<str:id>", views.AppDetails, name="AppDetails"),


    #path('updateJson/<int:id>', views.updateJson, name='updateJson'),

    # path("todos/", views.todos, name="Todos"),
    # path("about/", views.about, name="about"),
    # path('execute/', views.execute_code, name='execute_code'),
]
