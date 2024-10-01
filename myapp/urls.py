from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='homepage'),
    
    # township
    path('township/', views.township, name="township_page"),
    path('township_detail/<int:pk>/detail', views.township_detail, name="township_detail_page"),
    path('create_township/', views.create_township, name='create_township_page'),
    path('update_township/<str:pk>/update', views.update_township, name="township_update_page"),
    path('delete_township/<str:pk>/delete', views.delete_township, name="delete_township_page"),
    
    # towns
    path('town/', views.towns, name='towns_page'),
    path('town_detail/<str:pk>/detail', views.town_detail, name="town_detail_page"),
    path('create_town/', views.create_town, name="create_town_page"),
    path('update_town/<str:pk>/update', views.update_town, name="update_town_page"),
    path('delete_town/<str:pk>/update', views.delete_town, name="delete_town_page"),
    
    
    
    # village
    path('create_village/', views.create_village, name="create_village_page"),
    path('update_village/<str:pk>/update', views.update_village, name="update_village_page"),
    path('delete_village/<str:pk>/delete', views.delete_village, name="delete_village_page"),
    
    # ward
    path('create_ward/', views.create_ward, name='create_ward_page'),
    path('update_ward/<str:pk>/update', views.update_ward, name="update_ward_page"),
    path('delete_ward/<str:pk>/delete', views.delete_ward, name="delete_ward_page"),
    
    # school
    path('school/', views.school, name='school_page'),
    path('create_school_type/', views.create_school, name='create_school_page'),
    path('update_school_type/<str:pk>/update', views.update_school_type, name='update_school_typepage'),
    
]
