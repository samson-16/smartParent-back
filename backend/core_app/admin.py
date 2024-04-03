from django.contrib import admin
from .models import Parent

# Define the admin class for the Parent model
class ParentAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_children_names']  # Customize the display fields

    def get_children_names(self, obj):
        return ", ".join([child.fisrt_name for child in obj.children.all()])  # Display children names

    get_children_names.short_description = 'Children'  # Set column header name

# Register the Parent model with its admin class
admin.site.register(Parent, ParentAdmin)