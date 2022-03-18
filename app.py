
import dns_lookup


#FLASK
from flask import Flask, render_template

app = Flask(__name__)

headings = dns_lookup.ip_result[1].keys()

_data = []
_x = 0
for _contents in dns_lookup.ip_result:
    _data.append(list(dns_lookup.ip_result[_x].values()))
    _x += 1


@app.route('/')
def table():
    return render_template('table.html', headings=headings, data=_data)
