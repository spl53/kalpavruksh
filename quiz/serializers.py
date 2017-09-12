from quiz.models import User,Question

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('Title','id','user_id')
