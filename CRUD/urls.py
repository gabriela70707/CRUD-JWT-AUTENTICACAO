from django.urls import path
from . import views

urlpatterns = [
    path('criar/', view=views.registrar, name='registrar'),
    path('logar/', view=views.logar, name='logar'),
    path('teste/', view=views.view_protegida, name='view_protegida'),
    path('usuarios/', view=views.verUsuarios, name='verUsuarios'),
    path('deletar/<int:pk>', view=views.deletarUsuario, name = "deletarUsuario"),
    path('alterarUsuario/<int:pk>', view=views.alterarUsuario, name="alterarUsuario"),
    path('usuario/<int:pk>', view=views.ver_um_usuario, name="ver_um_usuario"),
]


