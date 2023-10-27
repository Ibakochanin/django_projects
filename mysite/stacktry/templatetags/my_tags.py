from django import template
from stacktry.models import Lesson, Click, ParticipationCount
from django.urls import reverse
from accounts.models import CustomUser
from django.conf import settings


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
def kick_boxing_participation_count(user):
    # Filter ParticipationCount objects by user and category (kick_boxing_count)
    participation_counts = ParticipationCount.objects.filter(user=user)

    # Sum up all kick_boxing_count values for the user
    total_kick_boxing_count = sum(count.kick_boxing_count for count in participation_counts)

    return total_kick_boxing_count

@register.simple_tag
def jiu_jitsu_participation_count(user):
    # Filter ParticipationCount objects by user and category (jiu_jitsu_count)
    participation_counts = ParticipationCount.objects.filter(user=user)

    # Sum up all jiu_jitsu_count values for the user
    total_jiu_jitsu_count = sum(count.jiu_jitsu_count for count in participation_counts)

    return total_jiu_jitsu_count

@register.simple_tag
def grappling_participation_count(user):
    # Filter ParticipationCount objects by user and category (grappling_count)
    participation_counts = ParticipationCount.objects.filter(user=user)

    # Sum up all grappling_count values for the user
    total_grappling_count = sum(count.grappling_count for count in participation_counts)

    return total_grappling_count

@register.simple_tag
def yoga_participation_count(user):
    # Filter ParticipationCount objects by user and category (yoga_count)
    participation_counts = ParticipationCount.objects.filter(user=user)

    # Sum up all yoga_count values for the user
    total_yoga_count = sum(count.yoga_count for count in participation_counts)

    return total_yoga_count

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