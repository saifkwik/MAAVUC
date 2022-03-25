import geoip2.database
import dns_lookup

# FLASK
from flask import Flask, render_template

app = Flask(__name__)

headings = dns_lookup.ip_result[1].keys()

_data = []
_x = 0
for _contents in dns_lookup.ip_result:
    _data.append(list(dns_lookup.ip_result[_x].values()))
    _x += 1

k = 0
for ip in range(len(_data)):
    with geoip2.database.Reader('GeoIP/GeoLite2-City.mmdb') as reader:
        try:
            response = reader.city(_data[k][2])
            city = response.city.name
        except geoip2.errors.AddressNotFoundError as r:
            pass
        if response.city.name is not None:
            _data[k][2] = _data[k][2] + ' - ' + str(city) + ', ' + list(response.country.names.values())[1]
        else:
            _data[k][2] = _data[k][2] + ' - ' + list(response.country.names.values())[1]
        k += 1


@app.route('/')
def table():
    return render_template('table.html', headings=headings, data=_data)
