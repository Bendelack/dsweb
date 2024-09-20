from django.contrib import admin
from .models import Receita, Despesa, Balancete

# Register your models here.
admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(Balancete)