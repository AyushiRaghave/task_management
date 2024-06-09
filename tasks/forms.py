from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    """
    Form for creating and updating Task instances.
    
    This form is built using the Task model and includes fields for title,
    description, due date, and status. The due_date field is rendered as a 
    date input widget for better user experience.
    """
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter task description', 'rows': 4}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Task Title',
            'description': 'Task Description',
            'due_date': 'Due Date',
            'status': 'Status',
        }
        help_texts = {
            'title': 'Enter a brief title for the task.',
            'description': 'Provide a detailed description of the task.',
            'due_date': 'Select the due date for the task.',
            'status': 'Choose the current status of the task.',
        }
