from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import paciente, medico
from django.shortcuts import render

# Create your views here.

def index(request):
    template_name = 'main/dashboard.html'
    return render(request, template_name)

def clinica(request):
    return HttpResponse("estamos no separador clinica")

# Pacientes
def pacientes_lista(request):
    todos_pacientes = paciente.objects.all().values()
    template_name = loader.get_template('clinica/lista_pacientes.html')
    context = {
        'todos_pacientes': todos_pacientes,
    }
    return HttpResponse(template_name.render(context, request))

def pacientes_ficha(request):
    paciente_ficha = paciente.objects.all()
    template_name = loader.get_template('clinica/ficha_paciente.html')
    context = {
        'paciente_ficha': paciente_ficha,
    }
    return HttpResponse(template_name.render(context, request))

def adicionar_paciente(request):
    nome = request.POST['nome']
    apelido = request.POST['apelido']
    data_nascimento = request.POST['data_nascimento']
    sexo = request.POST['sexo']
    local_nascimento = request.POST['local_nascimento']
    numero_contribuinte = request.POST['numero_contribuinte']
    morada = request.POST['morada']
    telefone = request.POST['telefone']
    email = request.POST['email']
    profissao = request.POST['profissao']
    observacoes = request.POST['observacoes']
    tipo_documento = request.POST['tipo_documento']
    numero_documento = request.POST['numero_documento']
    data_emissao_documento = request.POST['data_emissao_documento']
    data_validade_documento = request.POST['data_validade_documento']
    nacionalidade = request.POST['nacionalidade']
    estado_civil = request.POST['estado_civil']
    nome_pai = request.POST['nome_pai']
    nome_mae = request.POST['nome_mae']
    inactivo = request.POST.get('inactivo', False)  # Use get() with a default value
    paciente.objects.create(nome=nome, apelido=apelido, data_nascimento=data_nascimento, sexo=sexo, local_nascimento=local_nascimento, numero_contribuinte=numero_contribuinte, morada=morada, telefone=telefone, email=email, profissao=profissao, tipo_documento=tipo_documento, numero_documento=numero_documento, data_emissao_documento=data_emissao_documento, data_validade_documento=data_validade_documento, nacionalidade=nacionalidade, estado_civil=estado_civil, nome_pai=nome_pai, nome_mae=nome_mae, observacoes=observacoes, inactivo=inactivo)
    return HttpResponseRedirect(reverse('lista_pacientes'))


def editar_ficha_paciente(request, paciente_id):
    editar_ficha_paciente = paciente.objects.get(pk=paciente_id)
    template_name = loader.get_template('clinica/editar_ficha_paciente.html')
    context = {
        'editar_ficha_paciente': editar_ficha_paciente,
    }
    return HttpResponse(template_name.render(context, request))


def guardar_alteracoes(request, paciente_id): 
     
    nome = request.POST['nome']
    apelido = request.POST['apelido']
    data_nascimento = request.POST['data_nascimento']
    sexo = request.POST['sexo']
    local_nascimento = request.POST['local_nascimento']
    numero_contribuinte = request.POST['numero_contribuinte']
    morada = request.POST['morada']
    telefone = request.POST['telefone']
    email = request.POST['email']
    profissao = request.POST['profissao']
    observacoes = request.POST['observacoes']
    tipo_documento = request.POST['tipo_documento']
    numero_documento = request.POST['numero_documento']
    data_emissao_documento = request.POST['data_emissao_documento']
    data_validade_documento = request.POST['data_validade_documento']
    nacionalidade = request.POST['nacionalidade']
    estado_civil = request.POST['estado_civil']
    nome_pai = request.POST['nome_pai']
    nome_mae = request.POST['nome_mae']
    inactivo = request.POST.get('inactivo', False)  # Use get() with a default value
    paciente.objects.filter(pk=paciente_id).update(nome=nome, apelido=apelido, data_nascimento=data_nascimento, 
                                                   sexo=sexo, local_nascimento=local_nascimento, numero_contribuinte=numero_contribuinte,
                                                    morada=morada, telefone=telefone, email=email, profissao=profissao, 
                                                    tipo_documento=tipo_documento, numero_documento=numero_documento, 
                                                    data_emissao_documento=data_emissao_documento, data_validade_documento=data_validade_documento, 
                                                    nacionalidade=nacionalidade, estado_civil=estado_civil, nome_pai=nome_pai, nome_mae=nome_mae, 
                                                    observacoes=observacoes, inactivo=inactivo)
    return HttpResponseRedirect(reverse('lista_pacientes'))

def eliminar_paciente(request, paciente_id):
    paciente.objects.filter(pk=paciente_id).delete()
    return HttpResponseRedirect(reverse('lista_pacientes'))

# Medicos
def lista_meidcos(request):
    todos_medicos = medico.objects.all().values()
    template_name = loader.get_template('clinica/lista_medicos.html')
    context = {
        'todos_medicos': todos_medicos,
    }
    return HttpResponse(template_name.render(context, request))
    