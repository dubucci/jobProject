from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('project_1/', views.project_1, name='project_1'),
    path('tab_view/', views.tab_view, name='tab_view'),
    path('ajaxtest/', views.ajaxtest, name='ajaxtest'),
    path('chartf/', views.chartf, name='chartf'),
    path('charts/', views.charts, name='charts'),
    path('chartm/', views.chartm, name='chartm'),
    path('chartff/', views.chartff, name='chartff'),
    path('chartss/', views.chartss, name='chartss'),
    # path('map_folium/', views.map_folium, name='map_folium')
]