from django.urls import path
from . import views

app_name = 'detector'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('upload/', views.upload_view, name='upload'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
]
