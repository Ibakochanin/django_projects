from django.shortcuts import redirect
from accounts.models import CustomUser

class UserLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the user limit from the logged-in user's database record
        user_limit = CustomUser.objects.first().user_limit if CustomUser.objects.exists() else None

        # Get the current number of users in the system
        current_user_count = CustomUser.objects.count()

        # Check if the current number of users exceeds the user limit
        if user_limit is not None and current_user_count >= user_limit and request.path == '/accounts/signup/':
            return redirect('stacktry:lesson_list')

        response = self.get_response(request)
        return response