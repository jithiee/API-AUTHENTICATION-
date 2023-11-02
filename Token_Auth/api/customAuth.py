from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomeAuthentication(BaseAuthentication):
    def authenticate(self, request):
            try:
                username = request.GET.get('username')
                if username is not None:
                    user = User.objects.get(username=username)
                    return (user,None)
            except User.DoesNotExist:
                raise AuthenticationFailed('No such user')
                    
            