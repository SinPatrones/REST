from rest_framework import serializers
from imageupload.models import MyImage

class imageSerializer(serializers.ModelSerializer):
   class Meta:
      model = MyImage
      fields = [
         'model_pic'
      ]
