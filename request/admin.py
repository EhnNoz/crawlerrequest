from django.contrib import admin
from .models import Request
# Register your models here.
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['keyword', 'res_id']
    list_filter = ['keyword',]
    search_fields = ['keyword']

