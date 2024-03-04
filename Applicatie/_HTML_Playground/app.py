from flask import Flask, render_template, redirect, url_for, request, flash, redirect
from flask_bootstrap import Bootstrap5


from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField,RadioField
from wtforms.validators import DataRequired, Length,InputRequired
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

from flask import Flask, render_template, request

# Een lijst van fictieve gebruikers per vakgroep
vakgroepen = {
    "DICT": ["John", "Alice", "Bob"],
    "Taal- en Letterkunde": ["Emily", "David", "Sophia"],
    "Economie": ["Michael", "Emma", "James"]
}

# Een lijst van fictieve hosts
hosts = [
    {"name": "host1", "eth_address": "AA:BB:CC:DD:EE:FF", "type": "Desktop", "smtp_host": "smtp.example.com", "client_server": "Client", "campus": "Campus A", "location": "Building 1", "port_number": "1234", "department": "IT", "subnet": "192.168.1.0", "boot_option": "PXE", "phone": "123456789", "comments": "Lorem ipsum"}
]

@app.route('/')
def index():
    return render_template('index.html', vakgroepen=vakgroepen)

@app.route('/register/<vakgroep>/<gebruiker>', methods=['GET', 'POST'])
def register(vakgroep, gebruiker):
    if request.method == 'POST':
        ip_address = request.form['ip_address']
        host_name = request.form['host_name']
        sub_domain = request.form['sub_domain']
        # Andere velden ophalen afhankelijk van de radioknoppen

        # Verwerk de ingediende informatie

        return "Informatie ingediend voor IP: {}, Hostnaam: {}, Subdomein: {}".format(ip_address, host_name, sub_domain)
    else:
        return render_template('register.html', vakgroep=vakgroep, gebruiker=gebruiker)

@app.route('/hosts', methods=['GET', 'POST'])
def manage_hosts():
    if request.method == 'POST':
        host_name = request.form['host_name']
        # Zoek de host in de lijst van hosts
        for host in hosts:
            if host['name'] == host_name:
                return render_template('manage_hosts.html', host=host)
        return "Host niet gevonden"
    else:
        return render_template('manage_hosts.html')

if __name__ == '__main__':
    app.run(debug=True)


""" 
# 1 class per form, andere form-control types: 
# https://github.com/macloo/python-adv-web-apps/blob/master/python_code_examples/flask/forms/WTForms-field-types.csv
class NameForm(FlaskForm):
    name = StringField('Which actor is your favorite?', validators=[DataRequired(), Length(10, 40)])
    submit = SubmitField('Submit')

# Voorbeeld radio's
category = RadioField('Choose a detail to search:', validators=[InputRequired(message=None)],
choices=[ ('President', 'President\'s Name, e.g. John'), ('Home-state', 'Home State, e.g. Virginia'),
('Occupation', 'Occupation, e.g. Lawyer'), ('College', 'College, e.g. Harvard')] )

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     # names = get_names(ACTORS)
#     # you must tell the variable 'form' what you named the class, above
#     # 'form' is the variable name used in this template: index.html
#     form = NameForm()
#     message = ""
#     # if form.validate_on_submit():
#     #     name = form.name.data
#     #     # if name.lower() in names:
#     #         # empty the form field
#     #         form.name.data = ""
#     #         # id = get_id(ACTORS, name)
#     #         # redirect the browser to another route and template
#     #         return redirect( url_for('actor', id=id) )
#     #     else:
#     #         message = "That actor is not in our database."
#     return render_template('index.html', form=form)#, message=message)#, names=names)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jQueryUI/', methods=('GET', 'POST'))
def jQueryUI():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            return redirect(url_for('index'))

    return render_template('jQueryUI.html')

@app.route('/ipRegistratie/', methods=('GET', 'POST'))
def ipRegistratie():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            return redirect(url_for('index'))

    return render_template('ipRegistratie.html')

if __name__ == '__main__':
    app.run(debug=True) """