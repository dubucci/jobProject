from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('project_1/', views.project_1, name='project_1'),
    path('tab_view/', views.tab_view, name='tab_view'),
    path('ajaxtest/', views.ajaxtest, name='ajaxtest')
]