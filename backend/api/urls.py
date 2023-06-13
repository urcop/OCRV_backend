from django.urls import path

from .views import NewsAPIView, NewsDetailAPIView, QuestionAPIView, SkillsAPIView

urlpatterns = [
    path('news/', NewsAPIView.as_view(), name='news_list'),
    path('news/<uuid:pk>', NewsDetailAPIView.as_view(), name='news_detail'),
    path('skills/', SkillsAPIView.as_view(), name='skills_list'),
    path('questions/', QuestionAPIView.as_view(), name='questions_list'),
]
