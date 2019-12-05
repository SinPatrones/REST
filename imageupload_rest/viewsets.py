from .serializers import imageSerializer
from rest_framework.generics import (CreateAPIView)
from imageupload.models import MyImage

class ImageCreateAPIView(CreateAPIView):
	serializer_class = imageSerializer
	queryset = MyImage.objects.all()
