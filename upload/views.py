from django.db.models import QuerySet
from django.http import HttpResponse as response
from .models import Question
from django.shortcuts import render, get_object_or_404


# Create your views here.

def index(request):
    questions_list: QuerySet[Question] = Question.objects.order_by('-date')[:5]
    context = {
        'question_list': questions_list,
    }
    return render(request, 'upload/index.html', context)


def detail(request, question_id):
    res: Question = get_object_or_404(Question, pk=question_id)
    return render(request, 'upload/detail.html', {'question':res})


def results(request, question_id: int):
    res: str = "you are looking at the results of question number %s."
    return response(res % question_id)


def vote(request, question_id: int):
    return response("you're voting on question %s." % question_id)
