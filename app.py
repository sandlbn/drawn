# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for
from flask import redirect, request, session
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form
from drawn import Drawn
from shop.cart import Cart
from wtforms import TextField, SubmitField
from wtforms.validators import Required, URL
import json
from random import choice

class DrawnForm(Form):
    url_field = TextField(
        '',
        description='Enter url from Amazon, etc.',
        validators=[Required(), URL()]
    )
    submit_button = SubmitField('Add')


def create_app(configfile=None):
    app = Flask(__name__)
    AppConfig(app, configfile)  # Flask-Appconfig is not necessary, but
                                # highly recommend =)
                                # https://github.com/mbr/flask-appconfig
    Bootstrap(app)

    # in a real app, these should be configured through Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'

    @app.route('/', methods=['GET', 'POST'])
    def index():
        #session['drawn'] = []
        form = DrawnForm()
        if request.method == 'POST' and form.validate():
            url_data = form.url_field.data
            element = Drawn(url_data)
            element_json = {}
            element_json['title'] = element.item.title
            element_json['price'] = element.item.price
            element_json['photo'] = element.item.photo
            try:
                session['drawn'].append(element_json)
            except KeyError:
                session['drawn'] = []
                session['drawn'].append(element_json)
            return redirect(url_for('index'))
        try:
            drawn = session['drawn']
        except KeyError:
            drawn = []
        return render_template('index.html', form=form, drawn=drawn)
    @app.route('/delete/<int:element_id>/')
    def delete(element_id):
        try:
            del session['drawn'][element_id]
            return redirect(url_for('index'))
        except ValueError:
            return redirect(url_for('index'))

    @app.route('/drawn/')
    def drawn():
        try:
            session['drawn'] = [choice(session['drawn'])]
            return redirect(url_for('index'))
        except KeyError:
            return redirect(url_for('index'))



    return app


if __name__ == '__main__':
    create_app().run(debug=True, host='0.0.0.0', port=5000)
