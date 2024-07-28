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

    path("appsflowupdate", views.app_flow_update_ajax, name="appsflowupdate"),
    path("getflowlist", views.get_flow_list_ajax, name="getflowlist"),
    #path("deleteappflow", views.app_flow_delete_ajax, name="deleteappflow"),

    path("appsaccessupdate", views.app_access_update_ajax, name="appsaccessupdate"),
    path("getaccesslist", views.get_access_list_ajax, name="getaccesslist"),
    path("deleteappaccess", views.app_access_delete_ajax, name="deleteappaccess"),

    path("appsviewupdate", views.app_view_update_ajax, name="appsviewupdate"),
    path("getviewlist", views.get_view_list_ajax, name="getviewlist"),
    path("deleteappview", views.app_view_delete_ajax, name="deleteappview"),
     path("view/<str:viewid>/<str:appid>", views.app_view_ajax, name="view"), #without item id for new_req/custom_page
    path("view/<str:viewid>/<str:appid>/<str:itemid>", views.app_view_ajax, name="view"),

    path("appaction", views.take_action, name="takeactionabc"),
    path("getlist", views.get_list, name="getlist"),





    #path("appnew/", views.addAppList, name="appnew"),

    
    #path("appdetails/<str:id>", views.AppDetails, name="AppDetails"),


    #path('updateJson/<int:id>', views.updateJson, name='updateJson'),

    # path("todos/", views.todos, name="Todos"),
    # path("about/", views.about, name="about"),
    # path('execute/', views.execute_code, name='execute_code'),
]
