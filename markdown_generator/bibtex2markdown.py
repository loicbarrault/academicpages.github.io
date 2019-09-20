# coding: utf-8
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogenize_latex_encoding
from bibtexparser.customization import convert_to_unicode
import os, sys
import datetime


parser = BibTexParser()
#parser.customization = homogenize_latex_encoding
parser.customization = convert_to_unicode

outdir='_publications'
if not os.path.exists(outdir):
    os.mkdir(outdir)
force=False

now = datetime.datetime.now()
#print(now.strftime("%Y-%m-%d"))

with open('papers.github.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file, parser=parser)
    
#print(bib_database.entries)
for n, entry in enumerate(bib_database.entries):
    print('######### PROCESSING ', entry['url'])
    #filename="{}/{}-{}".format(outdir, now.strftime("%Y-%m-%d"), entry['url'].split('papers/')[1].replace('pdf', 'md'))
    filename="{}/{}-{}-{}".format(outdir, entry['year'], '01-01',  entry['url'].split('papers/')[1].replace('pdf', 'md'))
    #print("FILENAME: ", filename)
    #if os.path.exists(filename) and force is False:
        #print('ERROR: ', filename, ' already exists...')
        #sys.exit(0)
        #print('WARNING: ', filename, ' already exists... skipping')
    #else:
    if not os.path.exists(filename) or force is True:
        with open(filename, 'w') as out: 
            out.write('---\n')
            out.write('title: ''{}''\n'.format(entry['title']))
            out.write('authors: {}\n'.format(entry['author']))
            out.write('collection: publications\n')
            out.write('permalink: /publication/\n')
            #out.write('excerpt: \'', entry['summary'],'\'')
            out.write('year: {}\n'.format(entry['year']))
            
            out.write('paperurl: {}\n'.format(entry['url']))
            if 'booktitle' in entry:
                bookorjournal=entry['booktitle']
            elif 'journal' in entry:
                bookorjournal=entry['journal']
            else:
                print('ERROR: no booktitle nor journal in entry')
                sys.exit(0)
            #if 'location' in entry:
            out.write('venue: ''{}''\n'.format(bookorjournal))
            #out.write('citation: {} ''{}'', <i> {} </i>, {}\n'.format(entry['author'], entry['title'], bookorjournal, entry["year"]))

            db = bibtexparser.bibdatabase.BibDatabase()
            db.entries = [entry]
            #bibtexparser.dumps(db)

            out.write('citation: "{}"'.format(bibtexparser.dumps(db).replace("\n", " ")))
            out.write('\n---\n')
            #out.write('[Download paper here] {}'.format(entry["url"]))
        #if n == 2:
        #    sys.exit(0)



    #---
    #title: "NMTPY: A Flexible Toolkit for Advanced Neural Machine Translation Systems"
    #collection: publications
    #permalink: /publication/caglayan_pbml2017
#excerpt: 'This paper is about NMTPY, an open source sofware for multimodal machine translation.'
#date: 2017-10-01
#venue: 'Journal 1'
#paperurl: 'https://loicbarrault.github.io/papers/caglayan_pbml2017.pdf'
#citation: 'O. Caglayan, M. García-Martínez, A. Bardet, W. Aransa, F. Bougares, L. Barrault, &quot;NMTPY: A Flexible Toolkit for Advanced Neural Machine Translation Systems&quto;, <i> Prague Bulletin of Mathematical Linguistics, Special Issue on Open Source Tools for Machine Translation </i>, 2017.'
#---

#[Download paper here](https://loicbarrault.github.io/papers/caglayan_pbml2017.pdf)

#Recommended citation: O. Caglayan, M. García-Martínez, A. Bardet, W. Aransa, F. Bougares, L. Barrault, &quot;NMTPY: A Flexible Toolkit for Advanced Neural Machine Translation Systems&quto;, <i> Prague Bulletin of Mathematical Linguistics, Special Issue on Open Source Tools for Machine Translation</i>, 2017.



