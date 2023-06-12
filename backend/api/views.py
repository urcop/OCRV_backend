from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import NewsSerializer, NewsDetailSerializer, SkillsSerializer, QuestionSerializer
from news.models import News
from questions.models import Skills, Question


class NewsAPIView(ListAPIView):
    """Список всех новостей."""
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailAPIView(RetrieveAPIView):
    """Детали для конкретной новости."""
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer


class SkillsAPIView(ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


class QuestionAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
