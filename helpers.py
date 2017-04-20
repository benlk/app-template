# Helper functions for acquiring stuff
import app_config
import collections
import copytext
import re

from unicodedata import normalize

CACHE = {}
_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

def get_character_slugs():
    copy = get_copy()
    slugs = []
    for row in copy['characters']:
        slugs.append( slugify( row['id'] ) )
    return list( set( slugs ) )

def get_props():
    copy = get_copy()
    props = []
    for row in copy['props']:
        props.append( row )
    return props

# get stuff for a specific character

def get_character_by_slug( slug ):
    copy = get_copy()
    traits = []
    for row in copy['characters']:
        if row['id'] == in [ 'fullname', 'alignment', 'magic', 'description' ]:
            traits[ row['key'] ] = row['value']
    return traits

def get_props_by_slug( slug ):
    copy = get_copy()
    props = []
    for row in copy['characters']:
        if row['id'] == slug:
            if row['key'] == 'prop':
                props[] = row['value']
    return props

def get_rumors_by_slug( slug ):
    copy = get_copy()
    rumors = []
    for row in copy['characters']:
        if row['id'] == slug:
            if row['key'] == 'trait':
                rumors[] = row['value']
    return rumors

def get_traits_by_slug( slug ):
    copy = get_copy()
    traits = []
    for row in copy['characters']:
        if row['id'] == slug:
            if row['key'] == 'trait':
                traits[] = row['value']
    return traits

def get_goals_by_slug( slug ):
    copy = get_copy()
    goals = []
    for row in copy['characters']:
        if row['id'] == slug:
            if row['key'] == 'goal':
                goals[] = row['value']
    return goals

def get_relationships_by_slug( slug ):
    copy = get_copy()
    relatinoships = []
    for row in copy['relationships']:
        if row['id'] == slug:
            relatinoships.append( row )
    return relatinoships

# other helpers

def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))

def get_copy():
    if not CACHE.get('copy', None):
        CACHE['copy'] = copytext.Copy(app_config.COPY_PATH)
    return CACHE['copy']

