# Monitoring

Checks
------
Ein Check ist erst dann gültig, wenn er gewisse Voraussetzungen erfüllt. Zum einen, muss er ein Nachkomme der Klasse `Check` sein. Somit wird sichergestellt, dass er die Grundfunktionalität eines Checks hat. 
Zudem muss der Check die Funktion `check()` der Standardklasse so erweitern, dass er innerhalb dieser Funktion seine eigene Funktionalität implementiert, die Funktion `set_value()` aufruft und schließlich seinen Wert zurückgibt. 

Die o. a. Implementierung sieht in der Praxis folgendermaßen aus:
```python
    # CPU check
    def check(self):
        cpu = cpu_percent()
        self.set_value(cpu)
        return cpu
```

Weitere Voraussetzungen sind die Einhaltung der Struktur- und Namenskonvention. Im Allgemeinen gilt es folgenes zu beachten:
* Es muss für jeden Check eine neue Datei im Verzeichnis `checks` angelegt werden, welche zwangsweise `check_name.py` zu heißen hat, wobei `name` mit dem Namen der entsprechenden Check-Klasse ersetzt wird. Für den CPU-Check heißt die Datei `check_cpu.py`.
* Der Klassenname muss die PEP8-Konvention (Stand 2018) entsprechen. Konkret bedeutet dies, dass die erste Buchstabe großgeschrieben wird und keine Sonderzeichen enthalten sein sollten. Dementsprechend heißt die Klasse für den CPU-Check wie folgt:
    ```python
    class Cpu(Check):
    ```

Konfiguration
-------------
Zuständig für die Konfiguration des gesamten Systems ist die `settings.py`-Datei. Die darin enthalteten Einstellungen sind relativ selbsterklärend.

Webserver
---------
Ein Webserver wird mittles `flask` zur Verügung gestellt und läuft standardmäßig auf Port 80.
Mit `@app.route("/")` erstellen wir einen lokalen Host. Auf diesen Host haben wir unsere Website erstellt, wo wir die Ausgaben der einzelnen Checks wiedergeben.
```python
@app.route("/")
def localhost():
    data = {'checks': checks}
    return render_template('website.html', **data)
```

Der aktuelle Status der einzelnen Checks lässt sich über eine Anfrage an `/check/<name>` (wobei `name` bspw. durch den Check "cpu" ersetzt wird) abfragen. Die dafür zuständige Funktion `daily_post()` sieht folgendermaßen aus:
```python
@app.route('/check/<check>', methods=['GET'])
def daily_post(check):
    if check in checks:
        value = client.check_by_name(check)
        return "{}".format(value)
    else:
        return "Error: {} check not found!".format(check)
```

Die wiederkehrende Aktualisierung der Informationen der einzelnen Checks auf der Webseite erfolgt durch eine Javaskript-Funktion names `setupChart()`, welche den Checknamen jede Sekunde abfragt und diesen auf der Webseite aktualisiert.

Website
-------

Die Webseite wird durch ein Jinja-Template erzeugt. Jeder Checks wird durch die Schleife innerhalb des `<body>` mit dem Template verknüpft und auf der Webseite einzeln wiedergegeben.

```html
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

#### Link zu Javascript-Dateien
```html
<script src="/static/canvasjs.min.js"></script>
    <script src="/static/charts.js"></script>
```
#### Link zur CSS-Datei
```html
<link rel="stylesheet" href="/static/style.css"/>
```

CSS Datei
---------

In der CSS-Datei haben wir ein Bild aus der Source-Datei von der Implementierung des Diagramms entfernt und haben die größe des Diagramms definiert:
```css
div.chart{
    height: 360px;
    width: 90%;
    padding: 20px;
}

.canvasjs-chart-credit{
    display: none;
}
```
