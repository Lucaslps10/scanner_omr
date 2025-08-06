from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('uploads/', views.listar_uploads, name='listar_uploads'),
    path('excluir/<int:pk>/', views.excluir_upload, name='excluir_upload'),
]
