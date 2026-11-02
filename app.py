from flask import Flask, render_template_string, request
import os, json
from src.snapshot import load, generate_snapshot
from src.compare import compare

app = Flask(__name__)
SNAPSHOT_DIR = "snapshots"

HTML = '''
<!doctype html>
<html><head><title>Compare Snapshots</title>
<style>
body { font-family: sans-serif; margin: 2rem; }
table { border-collapse: collapse; width: 100%; margin-top: 1rem; }
th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
th { background: #f0f0f0; }
.side-by-side { display: flex; gap: 1rem; }
.side-by-side table { width: 48%; }
.button-row { margin-top: 1rem; }
</style>
</head>
<body>
<h1>Compare Snapshots — Side-by-Side</h1>
<form method="post" action="/compare">
  <label>First date/time (YYYY-MM-DD or YYYY-MM-DD-HHMM): <input name="date1" value="2026-11-02-1430"></label>
  <label>Second date/time: <input name="date2" value="2026-11-02-1530"></label>
  <button type="submit">Compare</button>
</form>
<form method="post" action="/generate">
  <button type="submit">Generate New Snapshot</button>
</form>
{% if message %}<p>{{ message }}</p>{% endif %}
{% if data1 and data2 %}
<div class="side-by-side">
  <table>
    <tr><th>Field</th><th>{{ d1 }}</th></tr>
    {% for k, v in data1.items() %}<tr><td>{{ k }}</td><td>{{ v }}</td></tr>{% endfor %}
  </table>
  <table>
    <tr><th>Field</th><th>{{ d2 }}</th></tr>
    {% for k, v in data2.items() %}<tr><td>{{ k }}</td><td>{{ v }}</td></tr>{% endfor %}
  </table>
</div>
{% endif %}
</body></html>
'''

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML, data1={}, data2={}, d1="", d2="", message="")

@app.route('/compare', methods=['POST'])
def compare_view():
    d1_name = request.form.get('date1', '')
    d2_name = request.form.get('date2', '')
    data1 = load(d1_name)
    data2 = load(d2_name)
    return render_template_string(HTML, data1=data1, data2=data2, d1=d1_name, d2=d2_name, message="")

@app.route('/generate', methods=['POST'])
def generate():
    timestamp = generate_snapshot()
    return render_template_string(HTML, data1={}, data2={}, d1="", d2="", message=f"Snapshot saved: {timestamp}")

if __name__ == '__main__':
    app.run(debug=True)
