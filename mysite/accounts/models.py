from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    BELT_CHOICES = (
        ('White', 'White'),
        ('Blue', 'Blue'),
        ('Purple', 'Purple'),
        ('Brown', 'Brown'),
        ('Black', 'Black'),
    )

    # Choices for the 'member_type' field
    MEMBER_TYPE_CHOICES = (
        ('Fivedays', 'Fivedays'),
        ('Eightdays', 'Eightdays'),
        ('Regular', 'Regular'),
    )

    STRIPE_CHOICES = (
        (0, '0 stripes'),
        (1, '1 stripe'),
        (2, '2 stripes'),
        (3, '3 stripes'),
        (4, '4 stripes'),
    )

    GYM_CHOICES = (
        ('Kix', 'Kix'),
        ('Iwade', 'Iwade'),
        ('Both', 'Both'),
    )

    belt = models.CharField(max_length=20, choices=BELT_CHOICES, default='White')
    stripes = models.IntegerField(choices=STRIPE_CHOICES, default=0)
    member_type = models.CharField(max_length=20, choices=MEMBER_TYPE_CHOICES, default='Regular')
    gym_choice = models.CharField(max_length=20, choices=GYM_CHOICES, default='Kix')
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')
    user_limit = models.IntegerField(default=1000)


    def some_custom_method(self):
        """A basic custom method for the CustomUser model."""
        # Replace this with your custom logic
        return f"Hello, {self.username}! This is a custom method."

