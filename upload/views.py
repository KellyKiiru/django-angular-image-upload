from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import Image
from .serializers import ImageSerializer

class ImageView(APIView):
    def post(self, request, format=None):
        file = request.FILES.get('image')
        img_data = file.read()

        image = Image(
            name=file.name,
            type=file.content_type,
            image=img_data
        )
        image.save()

        return Response({"message": f"Image uploaded successfully: {file.name}"}, status=status.HTTP_201_CREATED)

class ImageInfoView(APIView):
    def get(self, request, name, format=None):
        try:
            db_image = Image.objects.get(name=name)
            serializer = ImageSerializer(db_image)
            return Response(serializer.data)
        except Image.DoesNotExist:
            return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)

class ImageViewView(APIView):
    def get(self, request, name, format=None):
        try:
            db_image = Image.objects.get(name=name)
            response = HttpResponse(db_image.image, content_type=db_image.type)
            return response
        except Image.DoesNotExist:
            return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)