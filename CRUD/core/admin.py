from django.contrib import admin
from .models import mode
# Register your models here.
@admin.register(mode)
class admina(admin.ModelAdmin):
    list_display=['id','name','email','password']