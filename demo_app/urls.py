from django.urls import path, include
from . import views

# localhost:8000/demo_app
# localhost:8000/demo_app/explore
urlpatterns = [
    path('', views.all_demo_app, name='all_demo_app'),
    path('<int:demo_app_id>/', views.demo_app_detail, name='demo_app_detail'),
    path('demo_app_stores/', views.demo_app_store_view,  name='demo_app_stores'),

]
