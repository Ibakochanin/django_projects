from django.db import models
from accounts.models import CustomUser
from django.utils import timezone


class Lesson(models.Model) :
    title = models.CharField(
            max_length=200,
    )

    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    SPOT_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
    ]


    CATEGORY_CHOICES = [
        ('Jiu Jitsu', 'Jiu Jitsu'),
        ('Free Mat', 'Free Mat'),
        ('Competition', 'Competition'),
        ('Basic', 'Basic'),
    ]

    COLOR_CHOICES = [
        ('sky', 'Sky'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('purple', 'Purple'),
        ('pink', 'Pink'),
        ('light red', 'Light Red'),
    ]

    SCHOOL_CHOICES = [
        ('Kix', 'Kix'),
        ('Iwade', 'Iwade'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    day = models.CharField(max_length=10, choices=DAY_CHOICES, null=True)
    spot = models.IntegerField(choices=SPOT_CHOICES, null=True)
    text = models.TextField(null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, null=True)
    time = models.CharField(max_length=12, null=True)
    picture = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')
    school = models.CharField(max_length=10, choices=SCHOOL_CHOICES, null=True)

class ParticipationCount(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)

    jiu_jitsu_count = models.PositiveIntegerField(default=0)
    free_mat_count = models.PositiveIntegerField(default=0)
    competition_count = models.PositiveIntegerField(default=0)
    basic_count = models.PositiveIntegerField(default=0)
    monthly_count_j = models.PositiveIntegerField(default=0)
    monthly_count_f = models.PositiveIntegerField(default=0)
    monthly_count_b = models.PositiveIntegerField(default=0)
    monthly_count_c = models.PositiveIntegerField(default=0)

    white_jiu_jitsu_count = models.PositiveIntegerField(default=0)
    blue_jiu_jitsu_count = models.PositiveIntegerField(default=0)
    purple_jiu_jitsu_count = models.PositiveIntegerField(default=0)
    brown_jiu_jitsu_count = models.PositiveIntegerField(default=0)
    black_jiu_jitsu_count = models.PositiveIntegerField(default=0)




class Click(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    order = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)