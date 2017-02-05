window.onload = function () {
	var dataPoints = [];

	var term = getParameterByName('term');
	console.log(term);

	$.get("/topics", {term: term}, function(data, status) {
		data = data[1].years;

		console.log(data);

		data = data.sort(function(a, b) {
			return a.year - b.year;
		});

		console.log(dataPoints);

		for (var i = data.length - 1; i >= 0; i--) {
			var curr = data[i];
			dataPoints.push({x: new Date(curr.year, 0), y: parseInt(curr.count)});
		}

		var chart = new CanvasJS.Chart("line-chart",
		{
			zoomEnabled: false,
		                animationEnabled: true,
			title:{
				text: "Search Term by Year"
			},
			axisY2:{
				// valueFormatString:"0",
				
				maximum: 5000,
				interval: 1000,
				interlacedColor: "#F5F5F5",
				gridColor: "#D7D7D7",      
					tickColor: "#D7D7D7"								
			},
		                theme: "theme2",
		                toolTip:{
		                        shared: true
		                },
			legend:{
				verticalAlign: "bottom",
				horizontalAlign: "center",
				fontSize: 15,
				fontFamily: "Lucida Sans Unicode"

			},
			data: [
			{        
				type: "line",
				lineThickness:3,       
				axisYType:"secondary",
				dataPoints: dataPoints,
			}
			],
		  legend: {
		    cursor:"pointer",
		    itemclick : function(e) {
		      if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
		      e.dataSeries.visible = false;
		      }
		      else {
		        e.dataSeries.visible = true;
		      }
		      chart.render();
		    }
		  }
		});
		chart.render();
		});
}

function getParameterByName(name, url) {
    if (!url) {
      url = window.location.href;
    }

    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}