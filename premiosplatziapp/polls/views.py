# Django
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

# Models
from .models import Question, Choice

# Create your views here.


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # latest_question_list = Question.objects.all()[:5]
#     return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

#     # Separado por comas
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # question_list = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(question_list)


# def detail(request, question_id):
#     # get_object_or_404(Question, pk=question_id) = Question.objects.get(pk=question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     # choice = question.choice_set.all()
#     # context = {
#     #     'question': question,
#     #     'url_index': 'polls/',
#     # }
#     return render(request, 'polls/detail.html', {'question': question})

#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


# CLASS BASES VIEWS. (GENERIC VIEWS)--------------------------------------------------------------------------------


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
        # return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(DetailView):
    # Heredando de DetailView para evitar el DRY en este caso. Sino heredarar de generic.DetailView
    # model = Question
    template_name = 'polls/results.html'


def vote(request, question_id): 
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist): 
        return render(request, "polls/detail.html", {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else: 
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
