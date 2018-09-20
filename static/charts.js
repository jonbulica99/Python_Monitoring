    function setupChart (name) {
        var xVal = 0;
        var yVal = 100;
        var updateInterval = 1000;
        var dataLength = 20; // number of dataPoints visible at any point
        var dps = []; // dataPoints

        var chart = new CanvasJS.Chart(name + "-chart", {
            title :{
                text: capitalize(name) + " data"
            },
            axisY: {
                includeZero: false
            },
            data: [{
                type: "line",
                dataPoints: dps
            }]
        });

        var updateChart = function (count) {
            count = count || 1;
            for (var j = 0; j < count; j++) {
                yVal = yVal +  Math.round(5 + Math.random() *(-5-5));
                dps.push({
                    x: xVal,
                    y: yVal
                });
                xVal++;
            }
            if (dps.length > dataLength) {
                dps.shift();
            }
            chart.render();
        };

        updateChart(dataLength);
        setInterval(function(){updateChart()}, updateInterval);
    }

    function capitalize(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
