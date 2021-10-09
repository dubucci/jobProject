//ele = 차트를 그릴 canvas id
//chart = 차트 타입 bar, line, pie
//data = 안의 데이터
//chartTitle = 차트의 제목
//chartTitleTF = 차트 제목 사용 true, false
var makeChart = {
    make : function(ele, chart, data, chartTitle, chartTitleTF) {
        var ctx = document.getElementById(ele).getContext('2d');
        
        new Chart(ctx, {
            type: chart,
            data: data
            , options: {
                responsive: true,
                legend: {
                  position: 'top',
                  fullWidth: true
                },
                title: {
                  display: chartTitleTF, //true, false
                  text: chartTitle //제목
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            //min : 0
                            //max : 20
                            beginAtZero: true,
                            fontSize : 14,
                        }
                    }]
                }
            }
        });
    }
}

function callFunc(url, parameter, callback, async){
	var boolAsync = true; 
	if(arguments.length == 5 && new Boolean(async)){
		boolAsync = async;
	}
	$.ajax({
    	url: url,
        dataType: 'json',
        data: parameter,
        async: boolAsync,
        success: function (data, status, xhr) {
        	callback(status, data);
        },
        error: function (xhr, status, error)  {
        	callback(status, xhr);
        }
    });
}

function callFuncView(url, parameter, callback) {
    $.ajax({
    	url: url,
        dataType: 'html',
        data: parameter,
        async: false,
        success: function (data, status, xhr) {
        	callback(status, data);
        },
        error: function (xhr, status, error)  {
        	callback(status, xhr);
        }
    });
}

// callFunc(url, 'post', JSON.stringify(param), function(status, data){
//     if(status == 'success'){
//         returnData = data.resultList;
//     } else {
//         swAlertToast('데이터 가져오기 실패');
//         returnData = null;	
//     }
// }, false);