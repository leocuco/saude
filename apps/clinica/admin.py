from django.contrib import admin

# Register your models here.
from .models import paciente, medico

admin.site.register(paciente) # Registramos el modelo paciente en el administrador de Django
admin.site.register(medico) # Registramos el modelo consulta en el administrador de Django