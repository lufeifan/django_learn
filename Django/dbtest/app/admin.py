from django.contrib import admin

# Register your models here.
from .models import Test

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display=('id','name')
    search_fields=('name',)