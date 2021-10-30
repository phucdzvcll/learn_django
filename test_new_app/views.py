from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Question

def testRequets(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('html/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'html/detail.html', {'question': question})