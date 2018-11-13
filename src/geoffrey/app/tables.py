from flask_table import Table, Col


class Results(Table):
    imdb_id = Col('imdbID', show=False)
    type = Col('Type')
    title = Col('Title')
    year = Col('Year')
    # publisher = Col('Publisher')
    # media_type = Col('Media')