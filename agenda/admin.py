from django.contrib import admin
from agenda.models import Category, Contact


@admin.register(Category)
class CategoryAdimin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdimin(admin.ModelAdmin):
    pass
