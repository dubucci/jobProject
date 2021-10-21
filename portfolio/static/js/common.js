//ele = 차트를 그릴 canvas id
//chart = 차트 타입 bar, line, pie
//data = 안의 데이터
//chartTitle = 차트의 제목
//chartTitleTF = 차트 제목 사용 true, false
var chartComponent = new Object();
var makeChart = {
  make: function (ele, chart, data, chartTitle, chartTitleTF) {
    ctx = document.getElementById(ele).getContext("2d");

    var config = {
      type: chart,
      data: data,
      options: {
        // indexAxis: "y",
        responsive: true,
        legend: {
          position: "top",
          fullWidth: true,
        },
        title: {
          display: chartTitleTF, //true, false
          text: chartTitle, //제목
        },
        scales: {
          yAxes: [
            {
              ticks: {
                //min : 0,
                //max : 20,
                beginAtZero: true,
                fontSize: 14,
              },
            },
          ],
        },
      },
    };
    if (chartComponent[ele] == null) {
      chartComponent[ele] = new Chart(ctx, config);
    } else {
      chartComponent[ele].ctx = ctx;
      chartComponent[ele].config = config;
      chartComponent[ele].update();
    }
  },
};
// var makeChart_h = {
//   make: function (ele1, chart1, data1, chartTitle1, chartTitleTF1) {
//     var ctx1 = document.getElementById(ele1).getContext("2d");

//     new Chart(ctx1, {
//       type: chart1,
//       data: data1,
//       options: {
//         indexAxis: "y",
//         // responsive: true,
//         legend: {
//           position: "top",
//           fullWidth: true,
//         },
//         title: {
//           display: chartTitleTF1, //true, false
//           text: chartTitle1, //제목
//         },
//         scales: {
//           yAxes: [
//             {
//               ticks: {
//                 //min : 0
//                 //max : 20
//                 beginAtZero: true,
//                 fontSize: 14,
//               },
//             },
//           ],
//         },
//       },
//     });
//   },
// };

function callFunc(url, parameter, callback, async) {
  var boolAsync = true;
  if (arguments.length == 5 && new Boolean(async)) {
    boolAsync = async;
  }
  $.ajax({
    url: url,
    type: "get",
    dataType: "json",
    data: parameter,
    async: boolAsync,
    success: function (data, status, xhr) {
      callback(status, data);
    },
    error: function (xhr, status, error) {
      callback(status, xhr);
    },
  });
}

function callFuncView(url, parameter, callback) {
  $.ajax({
    url: url,
    dataType: "html",
    data: parameter,
    async: false,
    success: function (data, status, xhr) {
      callback(status, data);
    },
    error: function (xhr, status, error) {
      callback(status, xhr);
    },
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
