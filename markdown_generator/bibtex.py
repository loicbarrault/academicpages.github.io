
from operator import itemgetter
from itertools import groupby


def parse_bibfile(bib_path):
    """Read a bibtex file into a dictionary."""
    dct = {}
    with open(bib_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                if line.startswith('@'):
                    entries = {}
                    start = line.find('{')
                    end = line.find(',')
                    citekey = '\cite{%s}' % line[start+1:end]
                    while not line.startswith('}'):
                        line = next(f)
                        if ' = ' not in line:
                            continue
                        key, value = line.split(' = ')
                        key = key.strip()
                        value = value.strip()[1:-1].strip('{}')
                        entries[key] = value
                    dct[citekey] = entries
    return dct
    
    
def bibentry_to_style(bibentry, style='default'):
    """Format a bibtext dictionary entry as a string."""
    s = ''
    if style == 'default':
        s += '%s ' % bibentry['author']
        s += '(%s). ' % bibentry['year']
        s += '*%s*' % bibentry['title']

        if 'journal' in bibentry:
            s += '. %s, ' % bibentry['journal']

        if 'volume' in bibentry:
            s += '%s' % bibentry['volume']

            if 'number' in bibentry:
                s += '(%s)' % bibentry['number']

                if 'pages' in bibentry:
                    s += ', %s' % bibentry['pages'].replace('--', '-')

        s += '.'
    return s
