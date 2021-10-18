from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from .models import TDetailIndicator, TbDept, TUnityIndicator, TIndicator, TCode
from .models import Vunityindex, Vdetailindex
import folium

# Create your views here.

def main(request):
    
    return render(request, 'main.html')

def project_1(request):

    dept_list = TbDept.objects.all()

    return render(request, 'project/project_1.html', {'dept_list' : dept_list})

def tab_view(request):
    num = request.GET['num']
    returnPage = ''
    if num == '0' :
        returnPage = 'project/project_1_tab1.html'
    else :
        returnPage = 'project/project_1_tab2.html'
    indicator_list = TIndicator.objects.all()
    unityindicator_list = TUnityIndicator.objects.all()
    code_list = TCode.objects.all()
    sido_list = code_list.filter(group_code = 'C')
    year_list = unityindicator_list.filter(code = 6, gubun = 'C')
    # test_list = unityindicator_list.filter(gubun = 'C', year = 2008).values_list('unity_index', flat=True)
    
    map = folium.Map(location=[35.8, 127.51], zoom_start=6.2, width='100%', height='100', tiles='cartodbpositron') 
    maps=map._repr_html_() #지도를 템플릿에 삽입하기위해 iframe이 있는 문자열로 반환
    
    return render(request, returnPage, {'year_list' : year_list, 'indicator_list' : indicator_list, 'sido_list' : sido_list, 'map' : maps})

def ajaxtest(request):
    # text = request.GET['text']

    dept_list = TbDept.objects.all()
    dept_list = list(dept_list.values())
    # test_list = unityindicator_list.filter(gubun = 'C', year = 2008).values_list('unity_index', flat=True)

    resultJson = {'result1' : dept_list}
    return JsonResponse(resultJson, content_type="application/json")

def chartf(request):
    
    # tcode_list = TCode.objects.all()
    
    # join_list = list(TUnityIndicator.objects.raw('''select ui.CODE, ui.GUBUN, ui.YEAR, ui.UNITY_INDEX, c.CODE, c.CODE_NM
    #                                                 from t_unity_indicator as ui                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    #                                                 join t_code as c
    #                                                 on c.CODE = ui.CODE and c.GROUP_CODE = ui.GUBUN        
    #                                                 where ui.GUBUN = 'C' and ui.YEAR = '2008';'''    
    #                                                 ))
    # join_list = TUnityIndicator.objects.extra(tables=['TCode'], where = ['TCode.code = TUnityIndicator.code','TCode.group_code = TUnityIndicator.gubun'])
    # test_list = list(join_list.filter(gubun = 'C', year = 2008).values())

    uni1 = Vunityindex.objects.all()
    det1 = Vdetailindex.objects.all()

    test_2008_통합지수= list(uni1.filter(gubun = 'C', year = 2008).values())
    test_2008_고용기회= list(det1.filter(gubun = 'C', year = 2008, indicator_nm = '고용기회').values())
    test_2009_고용기회= list(det1.filter(gubun = 'C', year = 2009, indicator_nm = '고용기회').values())
    
    # for i in range(2008,2020):
    #     'list_'f'{i}'+'_uni' = list(unityindicator_list.filter(gubun = 'C', year = f'{i}').values())
    
    # detailindicator_list = TDetailIndicator.objects.all()

    
    resultJson = {'test_2008_통합지수' : test_2008_통합지수, 'test_2008_고용기회' : test_2008_고용기회, 'test_2009_고용기회':test_2009_고용기회}
    return JsonResponse(resultJson, content_type="application/json")
