from pybtex.database import parse_file, BibliographyData, Entry
from pybtex.database.input.bibtex import Parser

nuParser = Parser()
bib_data = parse_file('WeisseGroup.bib')

for pprKey in bib_data.entries:
    print(pprKey)
    ppr = bib_data.entries[pprKey]

    if 'note' in list(ppr.fields):
        note = ppr.fields['note']
        fieldsDict = dict(ppr.fields)
        fieldsDict['preview'] = note
        fieldsDict.pop('note')

        nuEntry = Entry(ppr.type, fields=fieldsDict)
        nuParser.data.add_entry(pprKey, nuEntry)

nuParser.data.to_file('papers', bib_format='bibtex')
