from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from stacktry.models import Click, Lesson, ParticipationCount
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from accounts.models import CustomUser
from django.http import JsonResponse
from django.utils import timezone
from django.core import serializers
from django.db.models import Sum






from stacktry.forms import CreateForm, UserPreferencesForm, ParticipationCountForm
from django.contrib.auth.mixins import LoginRequiredMixin
from stacktry.owner import OwnerDeleteView, OwnerDetailView, OwnerListView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse



def is_superuser(user):
    return user.is_superuser

class SetUserLimitView(View):
    template_name = 'stacktry/profile.html'

    def post(self, request, *args, **kwargs):
        user_limit = request.POST.get('user_limit')
        current_user = self.request.user
        current_user.user_limit = int(user_limit)
        current_user.save()
        return redirect('stacktry:profile', user_id=current_user.id)



# Create your views here.
class ProfilePageView(View):
    model = CustomUser
    template_name = 'stacktry/profile.html'


    def get(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        users = CustomUser.objects.all()

        user_preferences_form = UserPreferencesForm(instance=user)
        participation_count, _ = ParticipationCount.objects.get_or_create(user=user, jiu_jitsu_count=0, lesson=None)
        participation_count_form = ParticipationCountForm(instance=participation_count)
        return render(request, self.template_name, {'user': user, 'users': users, 'user_preferences_form': user_preferences_form, 'participation_count_form': participation_count_form})

    def get_context_data(self, **kwargs):
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        user_id = self.kwargs['user_id']

    # Ensure user_id is an integer before adding it to the context
        user_id = int(user_id)

        context['user_id'] = user_id
        return context

    def post(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        users = CustomUser.objects.all()

        user_preferences_form = UserPreferencesForm(request.POST, request.FILES or None, instance=user)
        participation_count, _ = ParticipationCount.objects.get_or_create(user=user, jiu_jitsu_count=0, lesson=None)
        participation_count_form = ParticipationCountForm(request.POST, instance=participation_count)

        if user_preferences_form.is_valid():
            user_preferences_form.save()

        if participation_count_form.is_valid():
            participation_count_form.save()


            return redirect('stacktry:profile', user_id=user.id)
        else:
            return render(request, self.template_name, {
                'user': user,
                'users': users,
                'user_preferences_form': user_preferences_form,
                'participation_count_form': participation_count_form,
            })



def profile_stream_file(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    response = HttpResponse()
    response['Content-Type'] = user.content_type
    response['Content-Length'] = len(user.profile_picture)
    response.write(user.profile_picture)
    return response



class ParticipationCountView(View):
    template_name = 'stacktry/profile.html'

    def get(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)

        # Get or create ParticipationCount instance for the user
        participation_count = ParticipationCount.objects.filter(user=user)

        form = ParticipationCountForm()  # No instance argument for GET requests
        return render(request, self.template_name, {'user': user, 'form': form, 'participation_count': participation_count})


    def post(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)

    # Get or create ParticipationCount instance for the user
        ParticipationCount.objects.filter(user=user).delete()
        participation_count = ParticipationCount.objects.create(user=user)

        form = ParticipationCountForm(request.POST, instance=participation_count)

        if form.is_valid():
        # Update the jiu_jitsu_count field in the participation_count instance


        # Save the updated instance
            participation_count.save()

        # Redirect to the same page where the form was submitted
            success_url = reverse('stacktry:profile', kwargs={'user_id': participation_count.user.id})
            return redirect(success_url)
        else:
            return render(request, self.template_name, {'user': user, 'form': form, 'participation_count': participation_count})






class AddUsersToLessonsView(View):
    template_name = 'stacktry/bjj_lesson_list.html'

    def post(self, request, *args, **kwargs):
        # Your logic to add users to lessons based on gym_choice and school
        kix_users = CustomUser.objects.filter(gym_choice='Kix')
        iwade_users = CustomUser.objects.filter(gym_choice='Iwade')
        both_users = CustomUser.objects.filter(gym_choice='Both')

        kix_lessons = Lesson.objects.filter(school='Kix')
        iwade_lessons = Lesson.objects.filter(school='Iwade')

        # Add Kix users to Kix lessons
        for user in kix_users:
            for lesson in kix_lessons:
                Click.objects.get_or_create(user=user, lesson=lesson)

        # Add Iwade users to Iwade lessons
        for user in iwade_users:
            for lesson in iwade_lessons:
                Click.objects.get_or_create(user=user, lesson=lesson)

        # Add Both users to Both Kix and Iwade lessons
        for user in both_users:
            for lesson in kix_lessons:
                Click.objects.get_or_create(user=user, lesson=lesson)

            for lesson in iwade_lessons:
                Click.objects.get_or_create(user=user, lesson=lesson)

        return HttpResponseRedirect(reverse('stacktry:bjj_lesson_list'))



class ResetMonthlyCountsView(View):
    def get(self, request):
        # Reset monthly counts for all users
        all_users = CustomUser.objects.all()  # Get all users from your user model
        for user in all_users:
            participation_counts = ParticipationCount.objects.filter(user=user)
            for count in participation_counts:
                count.monthly_count_j = 0
                count.monthly_count_f = 0
                count.monthly_count_b = 0
                count.monthly_count_c = 0
                count.save()

        return HttpResponseRedirect(reverse('stacktry:lesson_list'))





class AccountDeleteView(OwnerDeleteView):
    model = CustomUser
    template_name = 'stacktry/profile.html'

    def get_success_url(self):
        # Get the currently logged-in user's ID
        current_user_id = self.request.user.id
        # Redirect to the profile page of the currently logged-in user
        return reverse('stacktry:profile', kwargs={'user_id': current_user_id})


class LessonListView(OwnerListView):
    model = Lesson
    template_name = "stacktry/lesson_list.html"

    def get(self, request) :
        lesson_list = Lesson.objects.all()

        ctx = {'lesson_list' : lesson_list}
        return render(request, self.template_name, ctx)

class BjjLessonListView(OwnerListView):
    model = Lesson
    template_name = "stacktry/bjj_lesson_list.html"

    def get(self, request) :
        lesson_list = Lesson.objects.all()
        school = 'Kix'

        ctx = {
            'lesson_list' : lesson_list,
            'school': school,
        }
        return render(request, self.template_name, ctx)




class LessonCreateView(LoginRequiredMixin, View):
    template_name = 'stacktry/lesson_form.html'
    success_url = reverse_lazy('stacktry:lesson_list')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        if form.is_valid():
            day = form.cleaned_data['day']
            spot = form.cleaned_data['spot']
            school = form.cleaned_data['school']
            lesson_spot_used = Lesson.objects.filter(day=day, spot=spot, school=school).exists()

            if not lesson_spot_used:
                lesson = form.save(commit=False)
                lesson.owner = self.request.user
                lesson.save()
                return redirect(self.success_url)
            else:
                ctx = {'form': form, 'error_message': 'This day and spot already exist.'}
                return render(request, self.template_name, ctx)
        else:
            ctx = {'form': form}
            return render(request, self.template_name, ctx)


class LessonDetailView(OwnerDetailView):
    model = Lesson
    template_name = "stacktry/button_page.html"
    def get(self, request, pk) :
        x = get_object_or_404(Lesson, id=pk)
        context = { 'lesson' : x }
        return render(request, self.template_name, context)


def stream_file(request, pk):
    lesson = get_object_or_404(Lesson, id=pk)
    response = HttpResponse()
    response['Content-Type'] = lesson.content_type
    response['Content-Length'] = len(lesson.picture)
    response.write(lesson.picture)
    return response


class ButtonPageView(LoginRequiredMixin, View):
    template_name = 'stacktry/button_page.html'
    model = Click

    def get(self, request, pk):
        lesson = Lesson.objects.get(pk=pk)
        clicks = Click.objects.filter(lesson=lesson)
        limit = len(clicks) <= 9
        total_capacity = 10
        spots_open = total_capacity - len(clicks)
        return render(request, 'stacktry/button_page.html', {'clicks': clicks, 'limit': limit, 'spots_open': spots_open, 'lesson': lesson})

    def post(self, request, pk):
        if request.method == 'POST':
          user = request.user
          lesson = get_object_or_404(Lesson, pk=pk)

        if not Click.objects.filter(user=user, lesson=lesson).exists():
            click = Click.objects.create(user=user, lesson=lesson)
            click.save()

        return HttpResponseRedirect(reverse('stacktry:button_page', args=[pk]))


class ParticipationIncreaseView(LoginRequiredMixin, View):
    def post(self, request, pk, click_id):
        lesson = Lesson.objects.get(pk=pk)
        click = Click.objects.get(pk=click_id, lesson=lesson)
        user = click.user

        participation_count, created = ParticipationCount.objects.get_or_create(
            user=user,
            lesson=lesson
        )

        # Increment the appropriate participation count field for the user

        participation_count.monthly_count_j += 1

        if user.belt == 'White':
            participation_count.white_jiu_jitsu_count += 1
        elif user.belt == 'Blue':
            participation_count.blue_jiu_jitsu_count += 1
        elif user.belt == 'Purple':
            participation_count.purple_jiu_jitsu_count += 1
        elif user.belt == 'Brown':
            participation_count.brown_jiu_jitsu_count += 1
        elif user.belt == 'Black':
            participation_count.black_jiu_jitsu_count += 1


        # Save the participation count object to update the count
        participation_count.save()

        click.order = timezone.now()
        click.timestamp = timezone.now()
        click.save()

        clicks = Click.objects.filter(lesson=lesson, user=user).order_by('-order')

        # Serialize the queryset to JSON
        clicks_json = serializers.serialize('json', clicks)


        response_data = {
            'user_id': user.id,
            'click_id': click.id,
            'timestamp': click.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_counts': {
                'monthly_count_j':  participation_count.monthly_count_j,
                'jiu_jitsu_count': participation_count.jiu_jitsu_count,
                'white_jiu_jitsu_count': participation_count.white_jiu_jitsu_count,
                'blue_jiu_jitsu_count': participation_count.blue_jiu_jitsu_count,
                'purple_jiu_jitsu_count': participation_count.purple_jiu_jitsu_count,
                'brown_jiu_jitsu_count': participation_count.brown_jiu_jitsu_count,
                'black_jiu_jitsu_count': participation_count.black_jiu_jitsu_count,
            },
            'clicks': clicks_json,
        }

        # Redirect back to the lesson page
        return JsonResponse(response_data)


class ButtonDeleteView(OwnerDeleteView):
    model = Click
    template_name = 'stacktry/button_page.html'

    def get_success_url(self):
        lesson_pk = self.kwargs['lesson_pk']
        return reverse_lazy('stacktry:button_page', kwargs={'pk': lesson_pk})




class LessonDeleteView(OwnerDeleteView):
    model = Lesson
    template_name = 'stacktry/button_page.html'

    def get_success_url(self):
        return reverse_lazy('stacktry:lesson_list')

