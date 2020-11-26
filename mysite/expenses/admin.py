from django.contrib import admin
from .models import Category, Item


# Register your models here.
class ItemInline(admin.TabularInline):
    model = Item
    extra = 4


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ItemInline]


admin.site.register(Category, CategoryAdmin)
