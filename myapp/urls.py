from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='homepage'),
    
    # township
    path('township/', views.township, name="township_page"),
    path('township_detail/<int:pk>/detail', views.township_detail, name="township_detail_page"),
    
    # towns
    path('town/', views.towns, name='towns_page'),
    path('create_township/', views.create_township, name='create_township_page'),
    
    path('town_detail/<int:pk>/detail', views.town_detail, name="town_detail_page"),
    
    
    # village
    path('create_village/', views.create_village, name="create_village_page"),
    
]
