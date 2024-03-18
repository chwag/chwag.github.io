from pybtex.database import parse_file, BibliographyData, Entry
from pybtex.database.input.bibtex import Parser

nuParser = Parser()
bib_data = parse_file('WeisseGroup.bib')

for pprKey in bib_data.entries:
    print(pprKey)
    ppr = bib_data.entries[pprKey]

    fieldsDict = dict(ppr.fields)
    if "abstract" in fieldsDict.keys():
        fieldsDict.pop('abstract')
    if "doi" in fieldsDict.keys():
        fieldsDict['html'] = "https://doi.org/" + fieldsDict['doi']
    if "keywords" in fieldsDict.keys():
        fieldsDict['preview'] = fieldsDict['keywords']
        fieldsDict.pop('keywords')
    nuEntry = Entry(ppr.type, fields=fieldsDict, persons=ppr.persons)
    nuParser.data.add_entry(pprKey, nuEntry)

nuParser.data.to_file('papers.bib', bib_format='bibtex')
