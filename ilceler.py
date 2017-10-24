import json
from data import bolgeler, iller, ilceler

# upper ve lower islemi turkce icin duzgun calismiyor bu harflerde.
# kendimiz elle karsiliklarini vermemiz gerekiyor.
upper_map = {
    ord(u'i'): u'İ',
    ord(u'ı'): u'I',
}

for index, d in enumerate(ilceler):
    del d['FIELD3'] # baska bi yerden bulmustum. nufus bilgisi bu. gerek yok.
    d['ilce_id'] = index + 1
    for il in iller:
        if il['il'] == d['il'].translate(upper_map).upper():
            d['il_id'] = il['plaka']
            d['bolge'] = il['bolge']
            d['bolge_id'] = bolgeler[il['bolge']]


with open('data.json', 'w') as outfile:
    json.dump(ilceler, outfile, ensure_ascii=False)
