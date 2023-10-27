from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from stacktry.models import Click, Lesson, ParticipationCount
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from accounts.models import CustomUser





from stacktry.forms import CreateForm, ParticipationCountForm
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
        return render(request, self.template_name, {'user': user, 'users': users})

    def get_context_data(self, **kwargs):
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        user_id = self.kwargs['user_id']

    # Ensure user_id is an integer before adding it to the context
        user_id = int(user_id)

        context['user_id'] = user_id
        return context

class ProfileParticipationChangeView(View):
    template_name = 'stacktry/profile.html'

    def post(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        participation_count = get_object_or_404(ParticipationCount, user=user)
        form = ParticipationCountForm(request.POST, instance=participation_count)
        if form.is_valid():
            form.save()  # Save the form data to the model
            return HttpResponseRedirect(reverse('stacktry:profile', args=[user_id]))

        # If the form is not valid, re-render the page with error messages
        users = CustomUser.objects.all()
        return render(request, self.template_name, {'user': user, 'users': users, 'form': form})



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
        category=lesson.category

        participation_count, created = ParticipationCount.objects.get_or_create(
            user=user,
            lesson=lesson
        )

        # Increment the appropriate participation count field for the user
        if  category == 'Jiu Jitsu':
            participation_count.jiu_jitsu_count += 1
        elif category == 'Free Mat':
            participation_count.grappling_count += 1
        elif category == 'Competition':
            participation_count.kick_boxing_count += 1
        elif category == 'Basic':
            participation_count.yoga_count += 1

        # Save the participation count object to update the count
        participation_count.save()

        # Redirect back to the lesson page
        return HttpResponseRedirect(reverse('stacktry:button_page', args=[pk]))



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

