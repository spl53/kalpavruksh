from django.shortcuts import render

# Create your views here.

from quiz.models import User,Question,Answer,Tenant
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F,Case,When,CharField,Sum, Value as V
import copy
import json
from rest_framework import generics,renderers


class QuesList(APIView):
    """
    List all question and their answer.
    """
    def get(self, request, format=None):
	query = request.GET.get('query',"")
	ques = list(Question.objects.filter(private = 0,Title__icontains = query).\
	annotate(ans=F('answer__body'),answer_username=F('answer__user__name'), question_username=F('user__name')).\
		values('Title','id','ans','question_username','answer_username'))
	qids = list(set([ids['id'] for ids in ques ]))
	
	response_data = []
	for qid in qids:
		per_q = [q for q in ques if q['id'] == qid]
		data = {}
		copy_q = copy.deepcopy(per_q)
		for x in copy_q:
			data.update({'Title':x.pop('Title',None)})
			data.update({'id':x.pop('id',None)})
			data.update({'question_username':x.pop('question_username',None)})
		data.update({'answers':copy_q})
		response_data.append(data)
	print "RESPONSE DATA>>",response_data
        return Response(json.dumps(response_data))

class Dashboard(generics.RetrieveAPIView):
	renderer_classes = (renderers.TemplateHTMLRenderer,)

	def get(self,request):
		number_of_user = User.objects.count()
		number_of_question = Question.objects.count()
		number_of_answer = Answer.objects.count()
		number_of_request = list(Tenant.objects.all().values('api_key','api_request_count'))
		return Response({'number_of_user': number_of_user, 'number_of_request':number_of_request, 'number_of_question':number_of_question,'number_of_answer':number_of_answer}, template_name='dashboard.html')
