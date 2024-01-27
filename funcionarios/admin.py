from django.contrib import admin
from .models import Cargo, Especialidade, Funcionarios, ProfissionalSaude

admin.site.register(Cargo)
admin.site.register(Especialidade)
admin.site.register(Funcionarios)
admin.site.register(ProfissionalSaude)