from django.shortcuts import render
from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import plotly.offline as opy
import plotly.graph_objs as go


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
    'convert': 'USD',
    'start': '1',
    'limit': '5'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b94ec76c-29b2-4afc-8a88-fde0c46eac96',
}

session = Session()
session.headers.update(headers)


def bitcoin_data():
    try:
        response = requests.get(url, params=parameters, headers=headers).json()
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        response = None
    return response


def bitcoin_view(request):
    data = bitcoin_data()
    figure = None
    if data:
        figure = go.Figure(
            data=[go.Scatter(x=[date['date_added'] for date in data['data']], y=["%.2f" % date['quote']['USD']['price'] for date in data['data']])],
            layout_title_text="Bitcoin USD price"
        ).to_html()
    return render(request, 'bitcoin/bitcoin.html', {'data': figure})
