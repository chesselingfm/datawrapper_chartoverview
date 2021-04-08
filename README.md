# Datawrapper Chart-Übersicht

Some lousy written code to generate a HTML overview page of your Datawrapper charts

## How to use it

- Just add your Datawrapper chart ID to the file datawrapper_id_liste.csv
- Get your Datawrapper Token from the settings page and add it here: datawrapper_chart_uebersicht.py
- If you use GCS, add your settings, too
- You can refine the HTML template any time

We run this script hourly via cron to get a fresh and beautiful chart overview.

## Questions?
Mailto c.hesseling.fm@ndr.de