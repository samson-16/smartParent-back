from django.contrib import admin
from .models import Parent , Student, User 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

class ParentAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_children_names']

    def get_children_names(self, obj):
        return ", ".join([child.first_name for child in obj.children.all()]) 

    get_children_names.short_description = 'Children'  

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'role')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'first_name', 'last_name', 'email', 'phone_number', 'role' , 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(User, UserAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Student)

