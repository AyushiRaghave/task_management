from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """
    Task model to store details about user tasks.
    
    Fields:
        title (str): The title of the task.
        description (str): A detailed description of the task.
        created_at (datetime): The date and time when the task was created.
        updated_at (datetime): The date and time when the task was last updated.
        due_date (datetime): The date and time by which the task should be completed.
        status (str): The current status of the task. Choices are 'to-do', 'in-progress', 'completed'.
        user (ForeignKey): Reference to the User model. Specifies which user the task belongs to.
    """
    STATUS_CHOICES = [
        ('to-do', 'To Do'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=200, help_text="Enter the task title (max 200 characters).")
    description = models.TextField(help_text="Enter a detailed description of the task.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time when the task was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The date and time when the task was last updated.")
    due_date = models.DateTimeField(null=True, blank=True, help_text="The date and time by which the task should be completed.")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to-do', help_text="The current status of the task.")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="The user to whom this task belongs.")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['due_date']
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        indexes = [
            models.Index(fields=['user', 'status']),
        ]
