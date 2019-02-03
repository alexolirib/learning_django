from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

#view retorna HttpResponse com o conteudo, ou Http404
from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template =loader.get_template('polls/index.html')
    # contexto é um dicionário mapeando nomes de variáveis ​​para objetos Python.
    context ={
        'latest_question_list': latest_question_list
    }
    #return HttpResponse(template.render(context,request))
    return render(request, 'polls/index.html',context)

    # # mostra as últimas 5 salva no banco
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # #return HttpResponse(latest_question_list)
    # #separada por vírgulas, de acordo com sua data de publicação
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

def detail(request, question_id):
    #dessa forma é melhor pois é a forma de não acoplar a camada de modelo
    #com a camisada de visão
    # existe - get_list_or_404()(utiliza filter) e o get_object_or_404()(utiliza get)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    #aqui estaria acoplando
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})


def result(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
