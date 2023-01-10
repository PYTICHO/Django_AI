from django.contrib import admin
from .models import *

# Register your models here.


class TovarAdmin(admin.ModelAdmin):
    list_display = ("idtov",)
    search_fields = ('iddoc', "name")


class ChecksAdmin(admin.ModelAdmin):
    list_display = ('iddoc',)
    search_fields = ('iddoc',)


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Checks, ChecksAdmin)
admin.site.register(Tovar, TovarAdmin)
