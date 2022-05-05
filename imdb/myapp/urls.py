from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authadd/',views.auadd, name="authadd"),
    path('authedit/<int:pk>', views.auedit, name="authedit"),
    path('authdelete/<int:pk>', views.authdel, name="authdelete"),
    path('custadd/', views.cusadd, name="custadd"),
    path('custedit/<int:pk>', views.cusedit, name="custedit"),
    path('custdelete/<int:pk>', views.cusdel, name="custdelete"),
    path('pubadd/', views.pubadd, name="pubadd"),
    path('pubedit/<int:pk>', views.pubedit, name="pubedit"),
    path('pubdelete/<int:pk>', views.pubdel, name="pubdelete"),
    path('subadd/', views.subadd, name="subadd"),
    path('subdit/<str:pk>', views.subedit, name="subedit"),
    path('subdelete/<str:pk>', views.subdel, name="subdelete"),
    path('titleadd/', views.titleadd, name="titleadd"),
    path('titleedit/<int:pk>', views.titleedit, name="titleedit"),
    path('titleelete/<int:pk>', views.titledel, name="titledelete"),
    path('titleauthoradd/', views.titleauthoradd, name="titleauthoradd"),
    path('titleauthoredit/<int:pk>', views.titleauthoredit, name="titleauthoredit"),
    path('titleauthordelete/<int:pk>', views.titleauthordel, name="titleauthordelete"),
]