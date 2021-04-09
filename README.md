# Datawrapper Chart Overview
Some lousy written code to generate a HTML overview page of your Datawrapper charts

## How to use it

- Just add your Datawrapper chart IDs to the file `datawrapper_id_liste.csv`. One for each line. You can also add comments which will be displayed on the HTML page
- Get your Datawrapper Token from the settings page (https://app.datawrapper.de/account/api-tokens) and add it here twice: `datawrapper_chart_uebersicht.py`
- You can refine the HTML template any time

We run this script hourly via cron to get a fresh and beautiful chart overview.

## Questions?
Mailto c.hesseling.fm@ndr.de

## Disclaimer
The fantastic people at Datawrapper do not have anything to with this. All coding errors are mine. Use it at you own risk!
