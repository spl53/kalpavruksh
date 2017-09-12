from quiz.models import Tenant
from rest_framework import authentication,throttling
from rest_framework import exceptions
import random


class APIKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        api_key = request.GET.get('api_key')
        if not api_key:
            raise exceptions.AuthenticationFailed('please provide API KEY')
            return None
	
        try:
            tenant = Tenant.objects.get(api_key = api_key)
	    tenant.api_request_count += 1
	    tenant.save() 
        except Tenant.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such API KEY Exist')

        return (tenant, None)


class RandomRateThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
	tmp = random.randint(1, 10)
	print "ALLOW THROTALLING>>",tmp
        return tmp != 1
