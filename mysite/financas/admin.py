from django.contrib import admin
from .models import Receita, Despesa, UserAccount, Balancete

# Register your models here.
admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(UserAccount)
admin.site.register(Balancete)