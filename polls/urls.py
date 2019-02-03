from django.urls import path

from polls.views import index, detail, result, vote

#importante adicionar um namespace para diferenciar esse app de outros
app_name = 'polls'
urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='polls_detail'),
    path('<int:question_id>/result', result, name='polls_result'),
    path('<int:question_id>/vote', vote, name='polls_vote')
]