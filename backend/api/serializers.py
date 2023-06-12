from rest_framework import serializers

from news.models import News
from questions.models import Skills, Question


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'title',
            'description',
        ]


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'description',
            'created_at',
        )

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = [
            'title'
        ]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
