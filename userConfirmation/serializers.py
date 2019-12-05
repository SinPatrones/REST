from rest_framework import serializers
from userConfirmation.models import Usuario, File, ImgUpload, Inventario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','id_user','password']
    
class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ['codigo','denominacion','marca','modelo','tipo','color','serie','e','id_inventario','filename']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

class ImgUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgUpload
        fields = '__all__'
