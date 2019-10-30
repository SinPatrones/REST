import json
import io
from collections import namedtuple
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from userConfirmation.models import Usuario,ImgUpload
from userConfirmation.serializers import UsuarioSerializer, FileSerializer, ImgUploadSerializer

@csrf_exempt
def usuario_list(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serialize.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def usuario_detail(request,pk):
    try:
        user = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UsuarioSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status = 204)
        
@api_view(['GET','POST'])
def user_list(request,format = None):
    if request.method == 'GET':
        user = Usuario.objects.all()
        serializer = UsuarioSerializer(user, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsuarioSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_detail(request,pk, format = None):
    try:
        user = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UsuarioSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsuarioSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def confirmPass(request, format = None):
    if request.method == 'POST':
        found = False
        foundPass = False
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid()#permite el uso del dato de serializer
        contentJ = JSONRenderer().render(serializer.data) #render para el paso final del json
        userConfirmation = json.loads(contentJ, object_hook=lambda d: namedtuple('X', d.keys())(*d.values())) #funcion para acceder a las variables de json
        serializerAll = UsuarioSerializer(Usuario.objects.all(),many=True) #serializer para tener todos los objetos
        contentAll = JSONRenderer().render(serializerAll.data)
        userConfirmationAll = json.loads(contentAll, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        for i in userConfirmationAll:
            if userConfirmation.id_user == i.id_user:
                found = True
                if userConfirmation.password == i.password:
                    foundPass = True
                break
        
        if found and foundPass:
            contentData = {'id_user':'True', 'password':'True'}
            return Response(contentData, status=status.HTTP_200_OK)
        contentData = {'id_user':'False', 'password':'False'}
        return Response(contentData,status=status.HTTP_406_NOT_ACCEPTABLE)

def uploadImg(request):
    #serializer = ImgUploadSerializer(data=request.data)
    #serializer.is_valid()
    #content = JSONRenderer().render(serializer.data)
    #img = json.loads(content, object_hook=lambda d: namedtuple('X',d.keys())(*d.values()))#this image es la tupla del objeto
    #falta el verdadero objeto
    img = ImgUpload.objects.all()
    img = img[0]
    uploadImg = request.FILES['filename']
    img.picture.save("image.jpg",uploadImg)
    img.save()
    return JsonResponse({'result':'Success'})

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



