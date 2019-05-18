from django.contrib import admin

# Register your models here.
from app.models import Mascota, Persona

admin.site.register(Persona)
admin.site.register(Mascota)
