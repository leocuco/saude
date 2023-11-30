from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("clinica/", views.clinica, name="clinica"),
    path("clinica/pacientes/", views.pacientes_lista, name="lista_pacientes"),
    path("clinica/pacientes/nova_ficha/", views.pacientes_ficha, name="ficha_paciente"),
    path("clinica/pacientes/nova_ficha/adicionar_paciente/", views.adicionar_paciente, name="adicionar_paciente"),
    path("clinica/pacientes/editar_ficha_paciente/<int:paciente_id>/", views.editar_ficha_paciente, name="editar_ficha_paciente"),
    path("clinica/pacientes/editar_ficha_paciente/<int:paciente_id>/guardar_alteracoes/", views.guardar_alteracoes, name="guardar_alteracoes"),
    path("clinica/pacientes/eliminar_paciente/<int:paciente_id>", views.eliminar_paciente, name="eliminar_paciente"),
    
    
]