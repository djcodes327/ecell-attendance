from django.contrib import admin
from ecommerce.models import *


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    # Setting how will admin site displays products data
    list_display = ('id','name', 'price', 'quantity', 'created_at', 'updated_at')
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at')

    # Setting up slug name genertaed from product name
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    # sets up values for how admin site lists categories
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)

    # sets up slug to be generated from category name
    prepopulated_fields = {'slug': ('name',)}


class CustomerAdmin(admin.ModelAdmin):
    # sets up values for how admin site lists categories
    list_display = ('first_name', 'last_name', 'email','phone_number')
    list_display_links = ('first_name',)
    list_per_page = 50
    ordering = ['first_name']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date')
    list_display_links = ('customer', )
    list_per_page = 50
    ordering = ['customer']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Orders, OrderAdmin)
