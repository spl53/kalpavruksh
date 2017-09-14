from quiz.models import Tenant,ApiRequestCount
from rest_framework import authentication,throttling
from rest_framework import exceptions
import random
from datetime import datetime,timedelta

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
	url = request.get_full_path()
	current_time = datetime.utcnow()
	start_time = current_time.date()
	end_time = start_time + timedelta(days = 1)
	total_request = ApiRequestCount.objects.filter(date__gte = start_time,date__lt = end_time).order_by('-date')
	if total_request.count() <= 100:
	        api_key = request.GET.get('api_key')
        	tenant = Tenant.objects.get(api_key = api_key)
		ApiRequestCount.objects.create(date = current_time, api_request = url, tenant = tenant)
        	return True
	else:
		elapsed_time = (current_time - total_request[0].date.replace(tzinfo=None)).seconds
		if elapsed_time < 10:
			return False
		else:
			api_key = request.GET.get('api_key')
			tenant = Tenant.objects.get(api_key = api_key)
			ApiRequestCount.objects.create(date = current_time, api_request = url, tenant = tenant)
			return True
