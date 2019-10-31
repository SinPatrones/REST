from rest_framework import serializers
from userConfirmation.models import Usuario, File, ImgUpload

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','id_user','password']
    
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class ImgUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgUpload
        fields = '__all__'
