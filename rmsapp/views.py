from django.shortcuts import render
from django.http import HttpResponse
################### Authentication imprts #######################################
from django.contrib.auth.decorators import login_required,user_passes_test


# Create your views here.
@login_required
def index(request):
    #latest_question_list = 0
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'rms/base.html')
