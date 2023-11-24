from django import template
from stacktry.models import Lesson, Click, ParticipationCount
from django.urls import reverse
from accounts.models import CustomUser
from django.conf import settings
from django.contrib import messages


register = template.Library()

@register.simple_tag
def get_lesson_title(day, spot, school):
    try:
        lesson = Lesson.objects.get(day=day, spot=spot, school=school)
        return lesson.title
    except Lesson.DoesNotExist:
        return ""

@register.simple_tag
def get_lesson_picture(day, spot, school):
    try:
        lesson = Lesson.objects.get(day=day, spot=spot, school=school)
        if lesson.picture:
            url = reverse('stacktry:lesson_picture', args=[lesson.pk])
            return url
        else:
            return None
    except Lesson.DoesNotExist:
        return None

@register.simple_tag
def get_lesson_time(day, spot, school):
    try:
        lesson = Lesson.objects.get(day=day, spot=spot, school=school)
        return lesson.time
    except Lesson.DoesNotExist:
        return ""

@register.simple_tag
def get_lesson_color(day, spot, school):
    try:
        lesson = Lesson.objects.get(day=day, spot=spot, school=school)
        return lesson.color
    except Lesson.DoesNotExist:
        return ""

@register.simple_tag
def get_spots_open(day, spot, school):
    try:
        lesson = Lesson.objects.get(day=day, spot=spot, school=school)
        clicks = Click.objects.filter(lesson=lesson)
        total_capacity = 10
        spots_open = total_capacity - len(clicks)
        if spots_open == 0:
            return 'キャンセル待ち'
        else:
            return f'参加者残：{spots_open}'
    except Lesson.DoesNotExist:
        return ""

@register.simple_tag
def get_lesson_link(day, spot, school):
    try:
        lesson = Lesson.objects.get(day=day, spot=spot, school=school)
        url = reverse('stacktry:button_page', args=[lesson.pk])
        return url
    except Lesson.DoesNotExist:
        return ""

@register.filter
def lesson_exists(day, spot):

    lesson_exists = Lesson.objects.filter(day=day, spot=spot).exists()
    return lesson_exists



@register.simple_tag
def total_jiu_jitsu_participation_count(user):
    participation_counts = ParticipationCount.objects.filter(user=user)

    total_count = sum(
        count.white_jiu_jitsu_count +
        count.blue_jiu_jitsu_count +
        count.purple_jiu_jitsu_count +
        count.brown_jiu_jitsu_count +
        count.black_jiu_jitsu_count
        for count in participation_counts
    )

    return total_count

@register.simple_tag
def white_jiu_jitsu_participation_count(user):
    participation_counts = ParticipationCount.objects.filter(user=user)
    return sum(count.white_jiu_jitsu_count for count in participation_counts)

@register.simple_tag
def blue_jiu_jitsu_participation_count(user):
    participation_counts = ParticipationCount.objects.filter(user=user)
    return sum(count.blue_jiu_jitsu_count for count in participation_counts)

@register.simple_tag
def purple_jiu_jitsu_participation_count(user):
    participation_counts = ParticipationCount.objects.filter(user=user)
    return sum(count.purple_jiu_jitsu_count for count in participation_counts)

@register.simple_tag
def brown_jiu_jitsu_participation_count(user):
    participation_counts = ParticipationCount.objects.filter(user=user)
    return sum(count.brown_jiu_jitsu_count for count in participation_counts)

@register.simple_tag
def black_jiu_jitsu_participation_count(user):
    participation_counts = ParticipationCount.objects.filter(user=user)
    return sum(count.black_jiu_jitsu_count for count in participation_counts)




@register.simple_tag
def extract_user_id_from_url(request):
    # Extract user_id from the URL and return it as a string
    return str(request.path_info.split('/')[-2])


@register.simple_tag(takes_context=True)
def user_limit(context):
    request = context['request']
    if request.user.is_authenticated:
        user_limit = CustomUser.objects.get(id=request.user.id).user_limit
        return user_limit
    return 0

@register.simple_tag
def get_customuser_count():
    return CustomUser.objects.count()



@register.simple_tag
def jiu_jitsu_monthly_count(user):
    participation_counts = ParticipationCount.objects.filter(user=user)
    total_jiu_jitsu_monthly_count = sum(count.monthly_count_j for count in participation_counts)
    return total_jiu_jitsu_monthly_count


@register.simple_tag
def white_jiu_jitsu_message(user_id):
    # Get all ParticipationCount instances for the given user
    participations = ParticipationCount.objects.filter(user_id=user_id)

    if participations.exists():
        # Calculate the total white_jiu_jitsu_count by summing across all instances
        total_count = sum(participation.white_jiu_jitsu_count for participation in participations)

        if total_count in [10, 11, 12, 13, 14, 40, 41, 42, 43, 44, 70, 71, 72, 73, 74, 100, 101, 102, 103, 104]:
            return '新ストライプ!ラインで教えて'

    return ''


@register.simple_tag
def blue_jiu_jitsu_message(user_id):
    # Get all ParticipationCount instances for the given user
    participations = ParticipationCount.objects.filter(user_id=user_id)

    if participations.exists():
        # Calculate the total blue_jiu_jitsu_count by summing across all instances
        total_count = sum(participation.blue_jiu_jitsu_count for participation in participations)

        if total_count in [60, 61, 62, 63, 64, 120, 121, 122, 123, 124, 180, 181, 182, 183, 184, 240, 241, 242, 243, 244]:
            return '新ストライプ!ラインで教えて!'

    return ''

@register.simple_tag
def purple_jiu_jitsu_message(user_id):
    # Get all ParticipationCount instances for the given user
    participations = ParticipationCount.objects.filter(user_id=user_id)

    if participations.exists():
        # Calculate the total purple_jiu_jitsu_count by summing across all instances
        total_count = sum(participation.purple_jiu_jitsu_count for participation in participations)

        if total_count in [50, 51, 52, 53, 54, 100, 101, 102, 103, 104, 150, 151, 152, 153, 154, 200, 201, 202, 203, 204]:
            return '新ストライプ!ラインで教えて'

    return ''

@register.simple_tag
def brown_jiu_jitsu_message(user_id):
    # Get all ParticipationCount instances for the given user
    participations = ParticipationCount.objects.filter(user_id=user_id)

    if participations.exists():
        # Calculate the total brown_jiu_jitsu_count by summing across all instances
        total_count = sum(participation.brown_jiu_jitsu_count for participation in participations)

        if total_count in [55, 56, 57, 58, 59, 110, 111, 112, 113, 114, 165, 166, 167, 168, 169, 220, 221, 222, 223, 224]:
            return '新ストライプ!ラインで教えて'

    return ''