from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def analyseData(request):
    return render(request, 'analyse/analyse_index.html')


def testing(request):
    return render(request, 'analyse/the_test.html')