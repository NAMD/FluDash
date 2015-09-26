from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components, Resources
from bokeh.models import ColumnDataSource
import pandas as pd
import psycopg2


conn = psycopg2.connect(database='influenza', user='flu', password='influenza', host='localhost')

# Create your views here.

class SeriesView(View):
    def get(self, request):
        year = request.GET['year']
        city = request.get['geocode']

        sql = 'select * from public."INFLUD{}-utf8"'.format(year)
        try:
            df  = pd.read_sql_query(sql=sql, con=conn, index_col='id', parse_dates=True)
        except Exception as e:
            raise e


