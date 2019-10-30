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
        fields = ['filename','picture']
    '''
    #using as arguments serializers.Serializer
    id = serializers.IntegerField(read_only=True)
    id_user = serializers.CharField(required=True, allow_blank=False,max_length = 100)
    password = serializers.CharField(required=True, allow_blank=False,max_length=100)

    def create(self, validated_data):
        return Usuario.objects.create(**validated_data)
    def update(self, validated_data):
        instance.id_user = validated_data.get('id_user',instance.id_user)
        instance.password = validated_data.get('password',instance.password)
        instance.save()
        return instance
    '''
