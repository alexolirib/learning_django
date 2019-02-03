from django.urls import path

from polls.views import vote, IndexView, DetailView, ResultsView

#importante adicionar um namespace para diferenciar esse app de outros
app_name = 'polls'
urlpatterns = [
    #para view genericas
    path('',IndexView.as_view(), name='index'),
    #pk - pois será urilizado na  DetailView
    path('<int:pk>/', DetailView.as_view(), name='polls_detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='polls_results'),
    path('<int:question_id>/vote/', vote, name='polls_vote')
    #----- view mais descritiva
    # path('', index, name='index'),
    # path('<int:question_id>/', detail, name='polls_detail'),
    # path('<int:question_id>/results', result, name='polls_results'),
    # path('<int:question_id>/vote', vote, name='polls_vote')
]