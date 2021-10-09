from django.shortcuts import render
from .models import Dept

# Create your views here.
def main(request):
    
    return render(request, 'main.html')

def project_1(request):

    dept_list = Dept.objects.all()

    return render(request, 'project/project_1.html', {'dept_list' : dept_list})