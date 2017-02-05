window.onload = function () {
	var chart = new CanvasJS.Chart("line-chart",
	{
		zoomEnabled: false,
	                animationEnabled: true,
		title:{
			text: "Mobile Phone Subscriptions"
		},
		axisY2:{
			valueFormatString:"0.0 bn",
			
			maximum: 1.2,
			interval: .2,
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
			showInLegend: true,           
			name: "USA",        
			axisYType:"secondary",
			dataPoints: [
			{ x: new Date(2001, 00), y: 0.16 },
			{ x: new Date(2002, 0), y: 0.17 },
			{ x: new Date(2003, 0), y: 0.18},
			{ x: new Date(2004, 0), y: 0.19 },
			{ x: new Date(2005, 0), y: 0.20 },
			{ x: new Date(2006, 0), y: 0.23 },
			{ x: new Date(2007, 0), y: 0.261 },
			{ x: new Date(2008, 0), y: 0.289  },
			{ x: new Date(2009, 0), y: 0.3 },
			{ x: new Date(2010, 0), y: 0.31 },
			{ x: new Date(2011, 0), y: 0.32 },
			{ x: new Date(2012, 0), y: 0.33 }


			]
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
}