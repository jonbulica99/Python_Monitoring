# Monitoring

Checks
-----

```
Code
```

Localhost / Server
---
Mit @app.route("/") erstellen wir einen Localhost in diesen Localhost haben wir unsere Website eingefügt mit den Daten CHECK.
```
@app.route("/")
def localhost():
    data = {'checks': checks}
    return render_template('website.html', **data)
```
In diesem Abschnitt haben wir eine Schleife die immer wieder die Informationen aus den Checks holt und auf die Websiten Synchronisiert.
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
Link zu Javascript dateien:
```
<script src="/static/canvasjs.min.js"></script>
    <script src="/static/charts.js"></script>
```
Link zur CSS datei:
```
<link rel="stylesheet" href="/static/style.css"/>
```
Im Body haben wir einen for Schleife genommen, für jeden Check haben wir ein eigenes Diagramm das aus dem Javascript mit den Daten des einzelnen Checks wiedergegeben wird.
```
{% for check in checks %}
    <div class="{{ check }}">
        <div id="{{ check }}-chart" class="chart"></div>
        <script>setupChart("{{ check }}")</script>
    </div>
{% endfor %}
```
CSS Datei
---
In der CSS datei haben wir ein Bild aus der Source datei von der implementierung des Diagramms entfernt und haben die größe des Diagramms definiert.
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
