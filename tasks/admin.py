from django.contrib import admin
from .models import Task

# Register your models here for the tasks app.
# This will allow you to manage the Task model through the Django admin interface.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'due_date', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

# Customizing the admin interface for better user experience.
# list_display: Specifies the fields to display in the list view.
# list_filter: Adds filters in the right sidebar to filter the results.
# search_fields: Adds a search box to the admin interface.
