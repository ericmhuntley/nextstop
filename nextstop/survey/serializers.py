from rest_framework import serializers
from .models import Response, Question, Answer
from django.contrib.postgres.fields import ArrayField

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer',)

class ResponseSerializer(serializers.ModelSerializer):

    q_text = serializers.CharField(source='q.question')
    a = AnswerSerializer(read_only=True, many=True)
    s_text = serializers.CharField(source='survey.name')
    free_q_text = serializers.CharField(source='free_q.free_question')

    class Meta:
        model = Response
        fields = ('id', 'q', 'q_text', 'a', 'gender', 'age', 'zip_code', 'home', 'free_q_text', 'free_resp', 'survey', 's_text', 'timestamp', 'front', 'back', )

class AnswerCountSerializer(serializers.Serializer):

    q_id = serializers.IntegerField(source='q')
    q_text = serializers.CharField(source='q__question')
    a_id  = serializers.IntegerField(source='a')
    a_text  = serializers.CharField(source='a__answer')
    total = serializers.IntegerField()
    id_list  = serializers.ListField()

class QuestionCountSerializer(serializers.Serializer):

    q = serializers.IntegerField()
    q_text  = serializers.SerializerMethodField()
    total = serializers.IntegerField()

    def get_q_text(self, obj):
        return Question.objects.filter(id=obj['q']).values_list('question', flat=True)[0]
