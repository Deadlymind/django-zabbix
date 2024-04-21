from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomerUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Customer Field Heading',
            {
                'fields':(
                    'is_customer',
                    'is_engineer',
                )
            }
        )
    )

admin.site.register(User, CustomerUserAdmin) #nom del table user