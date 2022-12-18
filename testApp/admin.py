from django.contrib import admin
from .models import *

# Register your models here.


class TovarsAdmin(admin.ModelAdmin):
    list_display = ('iddoc', 'kolvo', 'summa', 'name')
    search_fields = ('iddoc',)


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Tovars, TovarsAdmin)
