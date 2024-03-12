from django.contrib import admin

# Register your models here.
from .models import paciente, medico, especialidade, medico_especialidade

admin.site.register(paciente)
admin.site.register(medico)
admin.site.register(especialidade)
admin.site.register(medico_especialidade)
