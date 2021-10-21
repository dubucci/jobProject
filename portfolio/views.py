from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from .models import TDetailIndicator, TbDept, TUnityIndicator, TIndicator, TCode
from .models import Vunityindex, Vdetailindex
import folium
import json

# Create your views here.

def main(request):
    
    return render(request, 'main.html')

def project_1(request):

    return render(request, 'project/project_1.html')

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
    year_list2 = unityindicator_list.filter(code = 0, gubun = 'I')

    indus_list = code_list.filter(group_code = 'I')
    # test_list = unityindicator_list.filter(gubun = 'C', year = 2008).values_list('unity_index', flat=True)
    
    m = folium.Map(location=[35.8, 127.51], zoom_start=6.2, width='100%', height='100', tiles='cartodbpositron') 
    
    # resultJson = {'chart1uni':chart1uni, 'chart1det':chart1det}
    # return JsonResponse(resultJson, content_type="application/json")
    #==================================================================================
    # uni = Vunityindex.objects.all()
    # det = Vdetailindex.objects.all()

    # year3 = request.GET.get('param_year3')
    # indicator3 = request.GET.get('param_indicator3')

    # chart3uni = uni.filter(gubun = 'C', year = year3).values()
    # chart3det = det.filter(gubun = 'C', year = year3, indicator= indicator3).values()
    
    # map_dataframe = pd.DataFrame()

    # temporary = folium.Choropleth(
    #     geo_data=state_geo,
    #     name='통합 지수',
    #     data=df2019_m,
    #     columns=['CITY_CODE', 'UNITY_INDEX'],
    #     key_on='feature.properties.CTP_KOR_NM',
    #     fill_color='RdYlGn',
    #     fill_opacity=0.7,
    #     line_opacity=0.3,
    #     color = 'gray',
    #     legend_name = '통합 지수'
    # ).add_to(m)

    # temporary.geojson.add_child(folium.features.GeoJsonTooltip(['CTP_KOR_NM'], labels=False))
    # title_html = '<h3 align="center" style="font-size:20px"><b 2019 index </b></h3>'
    # m.get_root().html.add_child(folium.Element(title_html))
    # folium.LayerControl().add_to(m)

    maps=m._repr_html_() #지도를 템플릿에 삽입하기위해 iframe이 있는 문자열로 반환
    
    return render(request, returnPage, {'year_list' : year_list, 'indicator_list' : indicator_list, 'sido_list' : sido_list, 'map' : maps, 'year_list2':year_list2, 'indus_list':indus_list})

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

    # uni = Vunityindex.objects.all()
    # det = Vdetailindex.objects.all()

    # testuni = list(uni1.filter(gubun = 'C', year = 2008).values())
    # testdet = list(det1.filter(gubun = 'C', year = 2008, indicator_nm = '고용기회').values())
    
    # testuni = list(uni1.filter(gubun = 'C', year = request.POST.get('param_year')).values())
    # year = request.GET.get('param_year1')
    # indicator = request.GET.get('param_indicator1')
    # testuni = list(uni1.filter(gubun = 'C', year = '2008').values())
    # testuni = list(uni.filter(gubun = 'C', year = year).values())
    # testdet = list(det.filter(gubun = 'C', year = year, indicator= indicator).values())
    # testdet = list(det1.filter(gubun = 'C', year = 2013, indicator= 17).values())
    # test_2008_통합지수= list(uni1.filter(gubun = 'C', year = 2008).values())
    # test_2008_고용기회= list(det1.filter(gubun = 'C', year = 2008, indicator_nm = '고용기회').values())
    # test_2009_고용기회= list(det1.filter(gubun = 'C', year = 2009, indicator_nm = '고용기회').values())
    
    # for i in range(2008,2020):
    #     'list_'f'{i}'+'_uni' = list(unityindicator_list.filter(gubun = 'C', year = f'{i}').values())
    
    # detailindicator_list = TDetailIndicator.objects.all()

    uni = Vunityindex.objects.all()
    det = Vdetailindex.objects.all()

    year1 = request.GET.get('param_year1')
    indicator1 = request.GET.get('param_indicator1')
    chart1uni = list(uni.filter(gubun = 'C', year = year1).values())
    chart1det = list(det.filter(gubun = 'C', year = year1, indicator= indicator1).values())
    
    resultJson = {'chart1uni':chart1uni, 'chart1det':chart1det}
    return JsonResponse(resultJson, content_type="application/json")

def charts(request):
    uni = Vunityindex.objects.all()
    det = Vdetailindex.objects.all()

    region = request.GET.get('param_region')
    indicator2 = request.GET.get('param_indicator2')
    chart2uni = list(uni.filter(gubun = 'C', code = region).values())
    chart2det = list(det.filter(gubun = 'C', code = region, indicator= indicator2).values())

    resultJson = {'chart2uni':chart2uni, 'chart2det':chart2det}
    return JsonResponse(resultJson, content_type="application/json")

def chartm(request):
    uni = Vunityindex.objects.all()
    det = Vdetailindex.objects.all()

    year3 = request.GET.get('param_year3')
    indicator3 = request.GET.get('param_indicator3')
    chart3uni = list(uni.filter(gubun = 'C', year = year3).values())
    chart3det = list(det.filter(gubun = 'C', year = year3, indicator= indicator3).values())
    
    resultJson = {'chart3uni':chart3uni, 'chart3det':chart3det}
    return JsonResponse(resultJson, content_type="application/json")

def chartff(request):
    uni = Vunityindex.objects.all()
    det = Vdetailindex.objects.all()

    year11 = request.GET.get('param_year11')
    indicator11 = request.GET.get('param_indicator11')
    chart11uni = list(uni.filter(gubun = 'I', year = year11).values())
    chart11det = list(det.filter(gubun = 'I', year = year11, indicator= indicator11).values())
    
    resultJson = {'chart11uni':chart11uni, 'chart11det':chart11det}
    return JsonResponse(resultJson, content_type="application/json")

def chartss(request):
    uni = Vunityindex.objects.all()
    det = Vdetailindex.objects.all()

    industry = request.GET.get('param_industry')
    indicator22 = request.GET.get('param_indicator22')
    chart22uni = list(uni.filter(gubun = 'I', code = industry).values())
    chart22det = list(det.filter(gubun = 'I', code = industry, indicator= indicator22).values())

    resultJson = {'chart22uni':chart22uni, 'chart22det':chart22det}
    return JsonResponse(resultJson, content_type="application/json")
