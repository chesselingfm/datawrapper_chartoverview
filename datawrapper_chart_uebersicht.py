#%%
import requests
import pandas as pd
import json
import jinja2
import csv
from google.cloud import storage


#%% Add your Datawrapper Token here twice. Replace the word TOKEN:

headers = {
    'authorization': 'Bearer TOKEN'}

svg_headers = {'authorization': 'Bearer TOKEN',
    "Accept": "image/png"}

#%% Loading your CSV list with Datawrapper IDs
list_of_ids = pd.read_csv('datawrapper_id_liste.csv', header=0)

#%% Defining SVG output in 1920x1080px for HD TV - change if you like

svg_querystring = {"unit":"px","mode":"rgb","width":"1920","height":"1060","plain":"true","scale":"1","zoom":"2","download":"false","fullVector":"false","transparent":"false"}

#%%

zeile = []

for index, row in list_of_ids.iterrows():
    chartid = str(row['dw_id'])
    
    
    if row['kommentar']:
        kommentar = str(row['kommentar'])
    else:
        kommentar = ""

    url = "https://api.datawrapper.de/v3/charts/{}".format(chartid)

    response = requests.request("GET", url, headers=headers)
    print(chartid, response)
    
    chart_info = json.loads(response.text)
    title = chart_info['title']
    veroeffentlicht = chart_info['publishedAt']
    try:
        datenquelle = chart_info['metadata']['data']['external-data']
    except:
        datenquelle = ""
        pass
    url2 = chart_info['publicUrl']
    bild = 'https:' + str(chart_info['thumbnails']['full'])

    iframe = chart_info['metadata']['publish']['embed-codes']['embed-method-responsive']
    iframe_code =jinja2.escape(str(chart_info['metadata']['publish']['embed-codes']['embed-method-responsive'])) 

    zeile.append([chartid, title, veroeffentlicht, datenquelle, iframe_code, iframe, bild, kommentar, datenquelle, url2] )

    response = requests.get('https://api.datawrapper.de/v3/charts/{}/export/svg'.format(chartid), headers=svg_headers, params=svg_querystring)

    svg_filename = chartid + "_export.svg"
    file = open(svg_filename, "w")
    file.write(response.text)
    file.close()
    upload_svg(svg_filename)

    if chart_info['type'] == 'd3-maps-choropleth':
        response = requests.get('https://api.datawrapper.de/v3/charts/{}/export/geojson'.format(chartid), headers=svg_headers)

        geojson_filename = chartid + "_export.svg"
        file = open(geojson_filename, "w")
        file.write(response.text)
        file.close()
        upload_svg(geojson_filename)
    

df = pd.DataFrame(zeile)
df.columns = ["dw_id", "title", "published", "source", "iframe_code", "iframe", "image", "kommentar", "datenquelle", "url"]

payload = df.T.to_dict()

#%% Generate HTML
outputfile = 'datawrapper_chart_uebersicht.html'

subs = jinja2.Environment( 
              loader=jinja2.FileSystemLoader('./')      
              ).get_template('template.html').render(title=title,mydata=payload) 
with open(outputfile,'wb') as f: f.write(subs.encode('utf-8'))


