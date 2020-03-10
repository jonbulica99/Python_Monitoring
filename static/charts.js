function setupChart(name) {
    var xVal = 0;
    var yVal = 100;
    var updateInterval = 1000;
    var dataLength = 20; // number of dataPoints visible at any point
    var dps = []; // dataPoints

    var chart = new CanvasJS.Chart(name + "-chart", {
        title: {
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

    var updateChart = function (name) {
        getJSON('http://localhost:5000/check/' + name, function (err, data) {
//                    if (err !== null) {
            dps.push({
                x: xVal,
                y: data
            })
            xVal++;
//                    }
        });
        if (dps.length > dataLength) {
            dps.shift();
        }
        chart.render();
    };

    updateChart(name);
    setInterval(function () {
        updateChart(name)
    }, updateInterval);
}

function capitalize(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

var getJSON = function (url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function () {
        var status = xhr.status;
        if (status === 200) {
            callback(null, xhr.response);
        } else {
            callback(status, xhr.response);
        }
    };
    xhr.send();
};
