from django.urls import path
from image import views

app_name = "image"

urlpatterns = [
    path('handler/', views.handler, name='get'),
    path('files/<int:folder_id>/', views.folder_detail, name="folders"),
    path('image/<int:image_id>/', views.image_detail, name="image_detail"),
    path('index/', views.index, name="index")
]
