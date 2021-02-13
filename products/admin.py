from django.contrib import admin
from .models import Product, Category

# Register your models here.
# Used the code from the Code Institute Project - Boutique Ado -


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
© 2021 GitHub, Inc.
Terms
Privacy
Security
