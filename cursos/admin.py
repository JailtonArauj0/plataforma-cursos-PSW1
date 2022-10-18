from django.contrib import admin
from .models import Aulas, Comentarios, Cursos, NotasAulas
# Register your models here.

admin.site.register(Cursos)
admin.site.register(Aulas)
admin.site.register(Comentarios)
admin.site.register(NotasAulas)