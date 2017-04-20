#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Example application views.

Note that `render_template` is wrapped with `make_response` in all application
routes. While not necessary for most Flask apps, it is required in the
App Template for static publishing.
"""

import app_config
import logging
import oauth
import static

from flask import Flask, make_response, render_template
from render_utils import make_context, smarty_filter, urlencode_filter
from werkzeug.debug import DebuggedApplication

from helpers import *

app = Flask(__name__)
app.debug = app_config.DEBUG

app.add_template_filter(smarty_filter, name='smarty')
app.add_template_filter(urlencode_filter, name='urlencode')

logging.basicConfig(format=app_config.LOG_FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(app_config.LOG_LEVEL)

@app.route('/')
@oauth.oauth_required
def index():
    """
    Example view demonstrating rendering a simple HTML page.
    """
    context = make_context()
    context['characters'] = get_character_slugs();
    return make_response(render_template('index.html', **context))

@app.route('/characters/')
def characters():
    context = make_context()

    context['characters'] = get_character_slugs()
    return make_response(render_template('characters.html', **context))

character_slugs = get_character_slugs()
for slug in character_slugs:
    @app.route( '/character/%s/' % slug, endpoint=slug )
    def character():
        context = make_context()
        from flask import request

        context['props'] = get_props_by_slug( slug )
        context['goals'] = get_goals_by_slug( slug )
        context['traits'] = get_traits_by_slug( slug )
        context['rumors'] = get_rumors_by_slug( slug )
        context['character'] = get_character_by_slug( slug )
        context['relationships'] = get_relationships_by_slug( slug )
        print( context )
        return make_response(render_template('character.html', **context))

app.register_blueprint(static.static)
app.register_blueprint(oauth.oauth)

# Enable Werkzeug debug pages
if app_config.DEBUG:
    wsgi_app = DebuggedApplication(app, evalex=False)
else:
    wsgi_app = app

# Catch attempts to run the app directly
if __name__ == '__main__':
    logging.error('This command has been removed! Please run "fab app" instead!')
