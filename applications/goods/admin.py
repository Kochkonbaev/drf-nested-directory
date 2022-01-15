from django.contrib import admin
from .models import Category, Section, Group, Subgroup, Card, Product

admin.site.register(Category)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', )

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'section',)

@admin.register(Subgroup)
class SubgroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'group',)

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'subgroup',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'card',)
