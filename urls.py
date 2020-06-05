from django.urls import path,include
from To_do_list_app import views

urlpatterns = [
    path('',views.index,name='To_do_list_app'),
    path('delete\<list_id>',views.delete,name='delete'),
    path('cross_off\<list_id>',views.cross_off,name='cross_off'),
    path('un_cross\<list_id>',views.un_cross,name='un_cross'),
]
