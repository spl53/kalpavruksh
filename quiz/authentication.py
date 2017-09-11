from quiz.models import Tenant
from rest_framework import authentication
from rest_framework import exceptions


class APIKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        api_key = request.GET.get('api_key')
        if not api_key:
            raise exceptions.AuthenticationFailed('please provide API KEY')
            return None
	
        try:
            tenant = Tenant.objects.get(api_key = api_key)
        except Tenant.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such API KEY Exist')

        return (tenant, None)
