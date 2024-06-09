from django.apps import AppConfig


class TasksConfig(AppConfig):
    """
    Configuration for the tasks app.
    
    This class contains the default configurations for the tasks app,
    including the app name and the default primary key field type.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "tasks"
    
    def ready(self):
        """
        Override this method to include any application-specific initialization.
        This method is called when the application is ready.
        """
        # Import and register signals here if needed
        # from . import signals
        pass
