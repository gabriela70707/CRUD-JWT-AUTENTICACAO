from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import UsuarioSerializer

@api_view(['POST'])
def registrar (request):
    nome = request.data.get('username')
    senha = request.data.get('senha')
    biografia = request.data.get('biografia')
    idade = request.data.get('idade')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    escolaridade = request.data.get('escolaridade')
    qnt_animais = request.data.get('qnt_animais')


    if not nome or not senha:
        return Response({'erro':'Você não preencheu todos os campos obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)
    
    if Usuario.objects.filter(username = nome).exists():
        return Response({'erro':'Esse usuário já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    usuario = Usuario.objects.create_user(
        username=nome,
        password=senha, 
        biografia = biografia,
        idade = idade,
        telefone = telefone,
        endereco = endereco,
        escolaridade = escolaridade, 
        qnt_animais = qnt_animais
    )

    return Response({'mensagem':'Usuario criado com sucesso!'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def logar(request):
    nome = request.data.get('username')
    senha = request.data.get('senha')

    user = authenticate(username = nome, password = senha)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'acesso': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_201_CREATED)


    else:
        return Response({'erro':'Digite o usuario e senha corretos!'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_protegida(request):
    return Response({"mensagem":"Opa usuario! :)"}, status=status.HTTP_200_OK)


#Mostrar todos os usuarios cadastrados 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def verUsuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

#Mostrar somente um usuario em especifico 
@api_view (['GET'])
@permission_classes([IsAuthenticated])
def ver_um_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except:
        return Response ({'erro':'Esse usuário não existe'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)




@api_view(['DELETE'])
@permission_classes ([IsAuthenticated])
def deletarUsuario(resquest, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)

    except Usuario.DoesNotExist:
        return Response("Esse usuario não existe!", status=status.HTTP_404_NOT_FOUND)
    
    usuario.delete()
    return Response({'mensagem': 'O usuario foi apagado com sucesso!'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes ([IsAuthenticated])
def alterarUsuario (resquest, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response({'erro': 'Esse usuário não existe'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UsuarioSerializer(usuario, data = resquest.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"mensagem":"Usuario atualizado com sucesso"}, status=status.HTTP_200_OK)
    return Response(serializer.errors)

