from django.contrib import admin
from userConfirmation.models import TipoUsuario,Usuario,Inventario,BarCode

# Register your models here.
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Inventario)
admin.site.register(BarCode)