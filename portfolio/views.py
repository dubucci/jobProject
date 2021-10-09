from django.shortcuts import render
from django.http import JsonResponse
from .models import Dept

# Create your views here.
def main(request):
    
    return render(request, 'main.html')

def project_1(request):

    dept_list = Dept.objects.all()

    return render(request, 'project/project_1.html', {'dept_list' : dept_list})

def tab_view(request):
    num = request.GET['num']
    returnPage = ''
    if num == '0' :
        returnPage = 'project/project_1_tab1.html'
    else :
        returnPage = 'project/project_1_tab2.html'
    
    return render(request, returnPage)

def ajaxtest(request):
    #text = request.GET['text']

    dept_list = Dept.objects.all()
    dept_list = list(dept_list.values())

    resultJson = {'result' : dept_list}
    return JsonResponse(resultJson, content_type="application/json")