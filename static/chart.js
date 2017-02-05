window.onload = function () {
	var dataPoints = [];

	$.get("/topics", function(data, status) {
		// console.log(data);
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

		// console.log(dataPoints);

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

function update() {
	
}