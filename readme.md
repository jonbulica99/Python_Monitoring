                                  Monitoring
==============================================================

Checks
-----

```
Code
```










Localhost
---
```
@app.route("/")
def localhost():
    data = {'checks': checks}
    return render_template('website.html', **data)
```
text
```
@app.route('/check/<check>', methods=['GET'])
def daily_post(check):
    if check in checks:
        value = client.check_by_name(check)
        return "{}".format(value)
    else:
        return "Error: {} check not found!".format(check)
```

Website
---
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Monitoring</title>
    <link rel="stylesheet" href="/static/style.css"/>
    <script src="/static/canvasjs.min.js"></script>
    <script src="/static/charts.js"></script>
</head>
<body>
{% for check in checks %}
    <div class="{{ check }}">
        <div id="{{ check }}-chart" class="chart"></div>
        <script>setupChart("{{ check }}")</script>
    </div>
{% endfor %}
</body>
</html>
```
```
div.chart{
    height: 360px;
    width: 90%;
    padding: 20px;
}

.canvasjs-chart-credit{
    display: none;
}
```