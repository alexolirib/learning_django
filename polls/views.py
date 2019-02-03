from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

#view retorna HttpResponse com o conteudo, ou Http404
from polls.models import Question, Choice

#usamos aqui a ListView e DetailView
#DetailView - espera o valor de chave primaria pegue pela URL(chamado de pk)

#para view genericas
class  IndexView(generic.ListView):
    #template_name para não auto gerar um nome
    template_name = 'polls/index.html'
    #quando quero informar o nome da minha variável que vou usar no template, informo aqui
    #se não informar o nome do meu model será o da variável,
    #exemplo modelo - Question. Var - question
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            #pub_date__lte - irá retornar cujo seja igual ou menor do timezone.now()
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class  DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class  ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        #request.POST - é um objeto que permite acessar os dados submetidos
        #request.POST['choice'] -  retorna o id da opçao selecionada
        #request.POST -  estamos utilizando request post para os dados só podem ser acessado por chamada POST
        #request.POST['choice'] levanta um KeyError caso não tenha um choice no POST assim será re-exibido
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        #isso para acrescentar um voto não é a melhor forma , pois se é preciso estudar - condição de concorrência
        #https://docs.djangoproject.com/pt-br/2.1/ref/models/expressions/#avoiding-race-conditions-using-f
        selected_choice.votes += 1
        selected_choice.save()
        #é uma boa prática depois de ter sucesso com POST retornar um HttpResponseRedirect
        #reverse - é uma funçar que ajuda a evitar  colocar url dentro da view
        return HttpResponseRedirect(reverse('polls:polls_results', args=(question_id,)))
#----- view mais descritiva
#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template =loader.get_template('polls/index.html')
#     # contexto é um dicionário mapeando nomes de variáveis ​​para objetos Python.
#     context ={
#         'latest_question_list': latest_question_list
#     }
#     #return HttpResponse(template.render(context,request))
#     return render(request, 'polls/index.html',context)
#
#     # # mostra as últimas 5 salva no banco
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # #return HttpResponse(latest_question_list)
#     # #separada por vírgulas, de acordo com sua data de publicação
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#
# def detail(request, question_id):
#     #dessa forma é melhor pois é a forma de não acoplar a camada de modelo
#     #com a camisada de visão
#     # existe - get_list_or_404()(utiliza filter) e o get_object_or_404()(utiliza get)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#     #aqui estaria acoplando
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question})
#
#
# def result(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html',{'question': question})
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         #request.POST - é um objeto que permite acessar os dados submetidos
#         #request.POST['choice'] -  retorna o id da opçao selecionada
#         #request.POST -  estamos utilizando request post para os dados só podem ser acessado por chamada POST
#         #request.POST['choice'] levanta um KeyError caso não tenha um choice no POST assim será re-exibido
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         #isso para acrescentar um voto não é a melhor forma , pois se é preciso estudar - condição de concorrência
#         #https://docs.djangoproject.com/pt-br/2.1/ref/models/expressions/#avoiding-race-conditions-using-f
#         selected_choice.votes += 1
#         selected_choice.save()
#         #é uma boa prática depois de ter sucesso com POST retornar um HttpResponseRedirect
#         #reverse - é uma funçar que ajuda a evitar  colocar url dentro da view
#         return HttpResponseRedirect(reverse('polls:polls_results', args=(question_id,)))
