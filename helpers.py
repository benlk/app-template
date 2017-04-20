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

def get_traits_by_slug( slug ):
    copy = get_copy()
    traits = []
    for row in copy['characters']:
        if row['id'] == slug:
            traits.append( row )
    return traits

def get_props_by_slug( slug ):
    copy = get_copy()
    props = []
    for row in copy['characters']:
        if row['id'] == slug:
            props.append( row )
    return props

def get_relationships_by_slug( slug ):
    copy = get_copy()
    relatinoships = []
    for row in copy['relatinoships']:
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

