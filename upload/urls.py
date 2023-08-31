from django.urls import path
from .views import ImageView, ImageInfoView, ImageViewView

urlpatterns = [
    path('upload/image', ImageView.as_view(), name='upload-image'),
    path('get/image/info/<str:name>/', ImageInfoView.as_view(), name='get-image-info'),
    path('get/image/<str:name>/', ImageViewView.as_view(), name='get-image'),
]