from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .form import FormularioTareas
from .models import tareas
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.template import loader
from .form import LibroForm

from .models import Libro
from .models import cuentas_banco

import pandas as pd
import matplotlib.pyplot as plt


# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')


def registro(request):

    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tareas_vista')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': 'Contraseña no coinciden'
        })

@login_required
def tareas_vista(request):
    tarea = tareas.objects.filter(user=request.user, fechacompleto__isnull=True)
    return render(request, 'tareas_vista.html', {
        'tarea': tarea
    })

@login_required
def tareas_completas(request):
    tarea = tareas.objects.filter(user=request.user, fechacompleto__isnull=False).order_by('-fechacompleto')
    return render(request, 'tareas_vista.html', {
        'tarea': tarea
    })

@login_required
def crear_tareas(request):

    if request.method == 'GET':

        return render(request, 'crear_tareas.html', {
            'form': FormularioTareas
        })
    
    else:
        try:
            form = FormularioTareas(request.POST)
            nueva_tarea = form.save(commit=False)
            nueva_tarea.user = request.user
            nueva_tarea.save()
            return redirect('tareas_vista')
        except ValueError:
            return render(request, 'crear_tareas.html', {
                'form': FormularioTareas,
                'error': 'Por favor proporcione datos valida'
            })

@login_required      
def detalles_tarea(request, tarea_id):
    if request.method == 'GET':
        tarea = get_object_or_404(tareas, pk=tarea_id, user=request.user)
        form = FormularioTareas(instance=tarea)
        return render(request, 'detalles_tarea.html',{
            'tarea': tarea,
            'form': form
        })
    else:
        try:
            tarea = get_object_or_404(tareas, pk=tarea_id, user=request.user)
            form = FormularioTareas(request.POST, instance=tarea)
            form.save()
            return redirect('tareas_vista')
        except ValueError:
            return render(request, 'detalles_tarea.html',{
            'tarea': tarea,
            'form': form,
            'error': 'Error al actualizar los datos'
        })

@login_required
def tarea_completa(request, tarea_id):
    tarea = get_object_or_404(tareas, pk=tarea_id, user=request.user)
    if request.method == 'POST':
        tarea.fechacompleto = timezone.now()
        tarea.save()
        return redirect('tareas_vista')
    
@login_required
def borrar_tarea(request, tarea_id):
    tarea = get_object_or_404(tareas, pk=tarea_id, user=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tareas_vista')

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')


def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html', {
            'form': AuthenticationForm

        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'iniciar_sesion.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('tareas_vista')



import pandas as pd
import json
from django.shortcuts import render
from .models import cuentas_banco

import datetime

def bancos(request):
    # Recupera los datos necesarios para la gráfica desde tu base de datos
    queryset = cuentas_banco.objects.values('banco', 'valor', 'anio_mes')  # Filtra los campos necesarios
    df = pd.DataFrame.from_records(queryset)  # Crea un DataFrame de Pandas

    # Convierte el campo 'valor' a tipo numérico eliminando las comas y convirtiéndolo a float
    df['valor'] = df['valor'].str.replace(',', '.').astype(float)

    # Convierte el campo 'anio_mes' a tipo datetime
    df['anio_mes'] = pd.to_datetime(df['anio_mes'], format='%d/%m/%Y')

    # Filtra solo las fechas de los últimos dos años
    current_year = datetime.datetime.now().year
    two_years_ago = current_year - 2
    df = df[df['anio_mes'].dt.year >= two_years_ago]

    # Ordena el DataFrame por el campo 'anio_mes' en orden ascendente
    df.sort_values('anio_mes', inplace=True)

    # Obtiene las listas de bancos, valores y fechas para el gráfico
    bancos = df['banco'].unique().tolist()

    # Crear lista de fechas en formato legible por Highcharts
    anio_mes = df['anio_mes'].dt.strftime('%Y-%m-%d').tolist()

    data_series = []
    for banco in bancos:
        valores = df.loc[df['banco'] == banco, 'valor'].tolist()
        data_series.append({'name': banco, 'data': valores})

    # Retorna la plantilla con los datos como contexto
    return render(request, 'bancos/vista_bancos.html', {'bancos': json.dumps(bancos), 'data_series': json.dumps(data_series), 'anio_mes': json.dumps(anio_mes)})




def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html',{'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario':formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')