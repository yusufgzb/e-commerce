from django.contrib import admin
from .models import Category,Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'gender',
        'status', 
        'updated_at',
    )
    list_filter = ('status','gender',)
    list_editable = (
        'title',
        'gender',
        'status', 
    )


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'price',
        'stock',
        'slug',
        'is_home',
        'status', 
        'updated_at',
    )
    list_filter = ('status', )
    list_editable = (
        'title',
        'is_home',
        'status', 
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product,ProductAdmin)