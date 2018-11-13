from ..app import app
from ..app import forms
from ..app import tables
from flask import request, redirect, render_template, flash
import requests
from ..app.helpers import OMDB
import logging

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    search = forms.MusicSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)

@app.route('/results', methods=['GET', 'POST'])
def search_results(search):
    results = []

    search_string = search.data['search']
    search_form = forms.MusicSearchForm(request.form)

    if search.data['search'] != '':
        print(search.data, 'search_data')
        ntflx_api = OMDB()
        response = ntflx_api.search_shows(search.data['search'])

        if response['Response'] == 'True':
            print(response)
            for show in response['Search']:
                # print()
                row = {'Title':show['Title'], 'Year': show['Year'], 'imdbID':show['imdbID'], 'Type': show['Type']}
                results.append(row)
        print(results)


    if not results or len(results) == 0:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = tables.Results(results)
        table.border = True
        return render_template('results.html', results=results, form=search_form)




