from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Add custom fields to your user model
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    user_limit = models.IntegerField(default=1000)


    def some_custom_method(self):
        """A basic custom method for the CustomUser model."""
        # Replace this with your custom logic
        return f"Hello, {self.username}! This is a custom method."

