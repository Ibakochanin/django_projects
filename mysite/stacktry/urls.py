from django.urls import path, reverse_lazy
from . import views




app_name='stacktry'
urlpatterns = [
    path('profile/<int:user_id>/', views.ProfilePageView.as_view(), name='profile'),
    path('lesson/list', views.LessonListView.as_view(), name='lesson_list'),
    path('button/<int:pk>/', views.ButtonPageView.as_view(), name='button_page'),
    path('button/<int:pk>/delete/<int:lesson_pk>/', views.ButtonDeleteView.as_view(success_url=reverse_lazy('stacktry:button_page')), name='button_delete'),
    path('lesson/create', views.LessonCreateView.as_view(success_url=reverse_lazy('stacktry:lesson_list')), name='lesson_create'),
    path('lesson/<int:pk>', views.LessonDetailView.as_view(), name='lesson_detail'),
    path('lesson/picture/<int:pk>/', views.stream_file, name='lesson_picture'),
    path('lesson/<int:pk>/delete', views.LessonDeleteView.as_view(success_url=reverse_lazy('stacktry:lesson_list')), name='lesson_delete'),
    path('participation_increase/<int:pk>/<int:click_id>/', views.ParticipationIncreaseView.as_view(), name='participation_increase'),
    path('delete/<int:pk>/', views.AccountDeleteView.as_view(), name='delete_account'),
    path('bjj_lesson/list', views.BjjLessonListView.as_view(), name='bjj_lesson_list'),
    path('set-user-limit/', views.SetUserLimitView.as_view(), name='set_user_limit'),
    path('profile_increase/<int:user_id>/', views.ProfileParticipationChangeView.as_view(), name='profile_increase'),

]

