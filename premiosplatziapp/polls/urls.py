# Django
from django.urls import path

# Views
from . import views

# Create your URLS here.

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/detail/', views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name="vote"),
]
