from django.contrib import admin
from polls.models import Question, Choice

#para customizar a apresentação do admin
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

#uma forma
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
#outra forma
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#outra forma em grupos
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'],
         'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    #was_published_recently - método que o model possui
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)