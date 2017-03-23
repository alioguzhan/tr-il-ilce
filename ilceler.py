import locale
import json

locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')


bolgeler = {
    'AKDENİZ': 1,
    'DOĞU ANADOLU':2,
    'EGE': 3,
    'GÜNEYDOĞU ANADOLU': 4,
    'İÇ ANADOLU': 5,
    'MARMARA': 6,
    'KARADENİZ': 7
}

iller = [
  {
    "bolge": "AKDENİZ",
    "il": "ADANA",
    "plaka": 1
  },
  {
    "bolge": "GÜNEYDOĞU ANADOLU",
    "il": "ADIYAMAN",
    "plaka": 2
  },
  {
    "bolge": "EGE",
    "il": "AFYONKARAHİSAR",
    "plaka": 3
  },
  {
    "bolge": "DOĞU ANADOLU",
    "il": "AĞRI",
    "plaka": 4
  },
  {
    "bolge": "KARADENİZ",
    "il": "AMASYA",
    "plaka": 5
  },
  {
    "bolge": "İÇ ANADOLU",
    "il": "ANKARA",
    "plaka": 6
  },
  {
    "bolge": "AKDENİZ",
    "il": "ANTALYA",
    "plaka": 7
  },
  {
    "bolge": "KARADENİZ",
    "il": "ARTVİN",
    "plaka": 8
  },
  {
    "bolge": "EGE",
    "il": "AYDIN",
    "plaka": 9
  },
  {
    "bolge": "MARMARA",
    "il": "BALIKESİR",
    "plaka": 10
  },
  {
    "bolge": "MARMARA",
    "il": "BİLECİK",
    "plaka": 11
  },
  {
    "bolge": "DOĞU ANADOLU",
    "il": "BİNGÖL",
    "plaka": 12
  },
  {
    "bolge": "DOĞU ANADOLU",
    "il": "BİTLİS",
    "plaka": 13
  },
  {
    "bolge": "KARADENİZ",
    "il": "BOLU",
    "plaka": 14
  },
  {
    "bolge": "AKDENİZ",
    "il": "BURDUR",
    "plaka": 15
  },
  {
    "bolge": "MARMARA",
    "il": "BURSA",
    "plaka": 16
  },
  {
    "bolge": "MARMARA",
    "il": "ÇANAKKALE",
    "plaka": 17
  },
  {
    "bolge": "İÇ ANADOLU",
    "il": "ÇANKIRI",
    "plaka": 18
  },
  {
    "bolge": "KARADENİZ",
    "il": "ÇORUM",
    "plaka": 19
  },
  {
    "bolge": "EGE",
    "il": "DENİZLİ",
    "plaka": 20
  },
  {
    "bolge": "GÜNEYDOĞU ANADOLU",
    "il": "DİYARBAKIR",
    "plaka": 21
  },
  {
    "bolge": "MARMARA",
    "il": "EDİRNE",
    "plaka": 22
  },
  {
    "bolge": "DOĞU ANADOLU",
    "il": "ELAZIĞ",
    "plaka": 23
  },
  {
    "bolge": "DOĞU ANADOLU",
    "il": "ERZİNCAN",
    "plaka": 24
  },
  {
    "bolge": "DOĞU ANADOLU",
    "il": "ERZURUM",
    "plaka": 25
  },
  {
    "bolge": "İÇ ANADOLU",
    "il": "ESKİŞEHİR",
    "plaka": 26
  },
  {
    "bolge": "GÜNEYDOĞU ANADOLU",
    "il": "GAZİANTEP",
    "plaka": 27
  },
  {
    "bolge": "KARADENİZ",
    "il": "GİRESUN",
    "plaka": 28
  },
  {
    "bolge": "KARADENİZ",
    "il": "GÜMÜŞHANE",
    "plaka": 29
  },
  {
    "bolge": "DOĞU ANADOLU",
    "il": "HAKKARİ",
    "plaka": 30
  },
  {
    "bolge": "AKDENİZ",
    "il": "HATAY",
    "plaka": 31
  },
  {
    "bolge": "AKDENİZ",
    "il": "ISPARTA",
    "plaka": 32
  },
  {
    "bolge": "AKDENİZ",
    "il": "MERSİN",
    "plaka": 33
  },
  {
    "bolge": "MARMARA",
    "il": "İSTANBUL",
    "plaka": 34
  },
  {
    "bolge": "EGE",
    "il": "İZMİR",
    "plaka": 35
  },
  {
    "bolge": "DOĞU ANADOLU",
    "il": "KARS",
    "plaka": 36
  },
  {
    "bolge": "KARADENİZ",
    "il": "KASTAMONU",
    "plaka": 37
  },
  {
    "bolge": "İÇ ANADOLU",
    "il": "KAYSERİ",
    "plaka": 38
  },
  {
    "bolge": "MARMARA",
    "il": "KIRKLARELİ",
    "plaka": 39
  },
  {
    "bolge": "İÇ ANADOLU",
    "il": "KIRŞEHİR",
    "plaka": 40
  },
  {
    "bolge": "MARMARA",
    "il": "KOCAELİ",
    "plaka": 41
  },
  {
    "bolge": "İÇ ANADOLU",
    "il": "KONYA",
    "plaka": 42
  },
  {
    "bolge": "EGE",
    "il": "KÜTAHYA",
    "plaka": 43
  },
  {
    "bolge": "DOĞU ANADOLU",
    "il": "MALATYA",
    "plaka": 44
  },
  {
    "bolge": "EGE",
    "il": "MANİSA",
    "plaka": 45
  },
  {
    "bolge": "AKDENİZ",
    "il": "KAHRAMANMARAŞ",
    "plaka": 46
  },
  {
    "bolge": "GÜNEYDOĞU ANADOLU",
    "il": "MARDİN",
    "plaka": 47
  },
  {
    "bolge": "EGE",
    "il": "MUĞLA",
    "plaka": 48
  },
  {
    "bolge": "DOĞU ANADOLU",
    "il": "MUŞ",
    "plaka": 49
  },
  {
    "bolge": "İÇ ANADOLU",
    "il": "NEVŞEHİR",
    "plaka": 50
  },
  {
    "bolge": "İÇ ANADOLU",
    "il": "NİĞDE",
    "plaka": 51
  },
  {
    "bolge": "KARADENİZ",
    "il": "ORDU",
    "plaka": 52
  },
  {
    "bolge": "KARADENİZ",
    "il": "RİZE",
    "plaka": 53
  },
  {
    "bolge": "MARMARA",
    "il": "SAKARYA",
    "plaka": 54
  },
  {
    "bolge": "KARADENİZ",
    "il": "SAMSUN",
    "plaka": 55
  },
  {
    "bolge": "GÜNEYDOĞU ANADOLU",
    "il": "SİİRT",
    "plaka": 56
  },
  {
    "bolge": "KARADENİZ",
    "il": "SİNOP",
    "plaka": 57
  },
  {
    "bolge": "İÇ ANADOLU",
    "il": "SİVAS",
    "plaka": 58
  },
  {
    "bolge": "MARMARA",
    "il": "TEKİRDAĞ",
    "plaka": 59
  },
  {
    "bolge": "KARADENİZ",
    "il": "TOKAT",
    "plaka": 60
  },
  {
    "bolge": "KARADENİZ",
    "il": "TRABZON",
    "plaka": 61
  },
  {
    "bolge": "DOĞU ANADOLU",
    "il": "TUNCELİ",
    "plaka": 62
  },
  {
    "bolge": "GÜNEYDOĞU ANADOLU",
    "il": "ŞANLIURFA",
    "plaka": 63
  },
  {
    "bolge": "EGE",
    "il": "UŞAK",
    "plaka": 64
  },
  {
    "bolge": "DOĞU ANADOLU",
    "il": "VAN",
    "plaka": 65
  },
  {
    "bolge": "İÇ ANADOLU",
    "il": "YOZGAT",
    "plaka": 66
  },
  {
    "bolge": "KARADENİZ",
    "il": "ZONGULDAK",
    "plaka": 67
  },
  {
    "bolge": "İÇ ANADOLU",
    "il": "AKSARAY",
    "plaka": 68
  },
  {
    "bolge": "KARADENİZ",
    "il": "BAYBURT",
    "plaka": 69
  },
  {
    "bolge": "İÇ ANADOLU",
    "il": "KARAMAN",
    "plaka": 70
  },
  {
    "bolge": "İÇ ANADOLU",
    "il": "KIRIKKALE",
    "plaka": 71
  },
  {
    "bolge": "GÜNEYDOĞU ANADOLU",
    "il": "BATMAN",
    "plaka": 72
  },
  {
    "bolge": "GÜNEYDOĞU ANADOLU",
    "il": "ŞIRNAK",
    "plaka": 73
  },
  {
    "bolge": "KARADENİZ",
    "il": "BARTIN",
    "plaka": 74
  },
  {
    "bolge": "DOĞU ANADOLU",
    "il": "ARDAHAN",
    "plaka": 75
  },
  {
    "bolge": "DOĞU ANADOLU",
    "il": "IĞDIR",
    "plaka": 76
  },
  {
    "bolge": "MARMARA",
    "il": "YALOVA",
    "plaka": 77
  },
  {
    "bolge": "KARADENİZ",
    "il": "KARABÜK",
    "plaka": 78
  },
  {
    "bolge": "GÜNEYDOĞU ANADOLU",
    "il": "KİLİS",
    "plaka": 79
  },
  {
    "bolge": "AKDENİZ",
    "il": "OSMANİYE",
    "plaka": 80
  },
  {
    "bolge": "KARADENİZ",
    "il": "DÜZCE",
    "plaka": 81
  }
]

data = [
 {
   "ilce": "Saimbeyli",
   "il": "Adana",
   "FIELD3": 16
 },
 {
   "ilce": "Aladağ",
   "il": "Adana",
   "FIELD3": 17.113
 },
 {
   "ilce": "Feke",
   "il": "Adana",
   "FIELD3": 17.82
 },
 {
   "ilce": "Yumurtalık",
   "il": "Adana",
   "FIELD3": 18.457
 },
 {
   "ilce": "Tufanbeyli",
   "il": "Adana",
   "FIELD3": 19.184
 },
 {
   "ilce": "Pozantı",
   "il": "Adana",
   "FIELD3": 20.004
 },
 {
   "ilce": "Karaisalı",
   "il": "Adana",
   "FIELD3": 21.682
 },
 {
   "ilce": "Karataş",
   "il": "Adana",
   "FIELD3": 22.178
 },
 {
   "ilce": "İmamoğlu",
   "il": "Adana",
   "FIELD3": 29.111
 },
 {
   "ilce": "Kozan",
   "il": "Adana",
   "FIELD3": 128.893
 },
 {
   "ilce": "Sarıçam",
   "il": "Adana",
   "FIELD3": 143.547
 },
 {
   "ilce": "Ceyhan",
   "il": "Adana",
   "FIELD3": 159.454
 },
 {
   "ilce": "Çukurova",
   "il": "Adana",
   "FIELD3": 353.68
 },
 {
   "ilce": "Yüreğir",
   "il": "Adana",
   "FIELD3": 419.24
 },
 {
   "ilce": "Seyhan",
   "il": "Adana",
   "FIELD3": 779.232
 },
 {
   "ilce": "Samsat",
   "il": "Adıyaman",
   "FIELD3": 8.534
 },
 {
   "ilce": "Tut",
   "il": "Adıyaman",
   "FIELD3": 10.422
 },
 {
   "ilce": "Çelikhan",
   "il": "Adıyaman",
   "FIELD3": 15.381
 },
 {
   "ilce": "Sincik",
   "il": "Adıyaman",
   "FIELD3": 18.107
 },
 {
   "ilce": "Gerger",
   "il": "Adıyaman",
   "FIELD3": 20.368
 },
 {
   "ilce": "Gölbaşı",
   "il": "Adıyaman",
   "FIELD3": 47.593
 },
 {
   "ilce": "Besni",
   "il": "Adıyaman",
   "FIELD3": 75.91
 },
 {
   "ilce": "Kahta",
   "il": "Adıyaman",
   "FIELD3": 117.964
 },
 {
   "ilce": "Adıyaman",
   "il": "Adıyaman",
   "FIELD3": 283.556
 },
 {
   "ilce": "Kızılören",
   "il": "Afyonkarahisar",
   "FIELD3": 2.526
 },
 {
   "ilce": "Evciler",
   "il": "Afyonkarahisar",
   "FIELD3": 7.634
 },
 {
   "ilce": "Bayat",
   "il": "Afyonkarahisar",
   "FIELD3": 8.412
 },
 {
   "ilce": "Hocalar",
   "il": "Afyonkarahisar",
   "FIELD3": 10.184
 },
 {
   "ilce": "Başmakçı",
   "il": "Afyonkarahisar",
   "FIELD3": 10.436
 },
 {
   "ilce": "Dazkırı",
   "il": "Afyonkarahisar",
   "FIELD3": 11.104
 },
 {
   "ilce": "Çobanlar",
   "il": "Afyonkarahisar",
   "FIELD3": 14.028
 },
 {
   "ilce": "Sultandağı",
   "il": "Afyonkarahisar",
   "FIELD3": 15.988
 },
 {
   "ilce": "İscehisar",
   "il": "Afyonkarahisar",
   "FIELD3": 24.225
 },
 {
   "ilce": "İhsaniye",
   "il": "Afyonkarahisar",
   "FIELD3": 28.253
 },
 {
   "ilce": "Çay",
   "il": "Afyonkarahisar",
   "FIELD3": 32.597
 },
 {
   "ilce": "Şuhut",
   "il": "Afyonkarahisar",
   "FIELD3": 37.377
 },
 {
   "ilce": "Emirdağ",
   "il": "Afyonkarahisar",
   "FIELD3": 38.269
 },
 {
   "ilce": "Sinanpaşa",
   "il": "Afyonkarahisar",
   "FIELD3": 41.004
 },
 {
   "ilce": "Bolvadin",
   "il": "Afyonkarahisar",
   "FIELD3": 45.098
 },
 {
   "ilce": "Dinar",
   "il": "Afyonkarahisar",
   "FIELD3": 47.889
 },
 {
   "ilce": "Sandıklı",
   "il": "Afyonkarahisar",
   "FIELD3": 56.708
 },
 {
   "ilce": "Afyonkarahisar",
   "il": "Afyonkarahisar",
   "FIELD3": 274.639
 },
 {
   "ilce": "Sarıyahşi",
   "il": "Aksaray",
   "FIELD3": 5.22
 },
 {
   "ilce": "Ağaçören",
   "il": "Aksaray",
   "FIELD3": 8.881
 },
 {
   "ilce": "Güzelyurt",
   "il": "Aksaray",
   "FIELD3": 12.147
 },
 {
   "ilce": "Gülağaç",
   "il": "Aksaray",
   "FIELD3": 19.801
 },
 {
   "ilce": "Eskil",
   "il": "Aksaray",
   "FIELD3": 25.984
 },
 {
   "ilce": "Ortaköy",
   "il": "Aksaray",
   "FIELD3": 34.048
 },
 {
   "ilce": "Aksaray",
   "il": "Aksaray",
   "FIELD3": 278.171
 },
 {
   "ilce": "Hamamözü",
   "il": "Amasya",
   "FIELD3": 4.056
 },
 {
   "ilce": "Göynücek",
   "il": "Amasya",
   "FIELD3": 10.771
 },
 {
   "ilce": "Gümüşhacıköy",
   "il": "Amasya",
   "FIELD3": 23.254
 },
 {
   "ilce": "Taşova",
   "il": "Amasya",
   "FIELD3": 31.333
 },
 {
   "ilce": "Suluova",
   "il": "Amasya",
   "FIELD3": 46.612
 },
 {
   "ilce": "Merzifon",
   "il": "Amasya",
   "FIELD3": 69.937
 },
 {
   "ilce": "Amasya",
   "il": "Amasya",
   "FIELD3": 135.95
 },
 {
   "ilce": "Evren",
   "il": "Ankara",
   "FIELD3": 2.901
 },
 {
   "ilce": "Çamlıdere",
   "il": "Ankara",
   "FIELD3": 6.781
 },
 {
   "ilce": "Güdül",
   "il": "Ankara",
   "FIELD3": 8.626
 },
 {
   "ilce": "Ayaş",
   "il": "Ankara",
   "FIELD3": 13.018
 },
 {
   "ilce": "Kalecik",
   "il": "Ankara",
   "FIELD3": 13.604
 },
 {
   "ilce": "Bala",
   "il": "Ankara",
   "FIELD3": 22.142
 },
 {
   "ilce": "Kızılcahamam",
   "il": "Ankara",
   "FIELD3": 25.767
 },
 {
   "ilce": "Nallıhan",
   "il": "Ankara",
   "FIELD3": 29.289
 },
 {
   "ilce": "Akyurt",
   "il": "Ankara",
   "FIELD3": 29.403
 },
 {
   "ilce": "Haymana",
   "il": "Ankara",
   "FIELD3": 31.176
 },
 {
   "ilce": "Şereflikoçhisar",
   "il": "Ankara",
   "FIELD3": 33.946
 },
 {
   "ilce": "Elmadağ",
   "il": "Ankara",
   "FIELD3": 43.666
 },
 {
   "ilce": "Kazan",
   "il": "Ankara",
   "FIELD3": 47.224
 },
 {
   "ilce": "Beypazarı",
   "il": "Ankara",
   "FIELD3": 47.646
 },
 {
   "ilce": "Çubuk",
   "il": "Ankara",
   "FIELD3": 84.636
 },
 {
   "ilce": "Gölbaşı",
   "il": "Ankara",
   "FIELD3": 118.346
 },
 {
   "ilce": "Polatlı",
   "il": "Ankara",
   "FIELD3": 121.101
 },
 {
   "ilce": "Pursaklar",
   "il": "Ankara",
   "FIELD3": 129.152
 },
 {
   "ilce": "Altındağ",
   "il": "Ankara",
   "FIELD3": 361.259
 },
 {
   "ilce": "Sincan",
   "il": "Ankara",
   "FIELD3": 497.516
 },
 {
   "ilce": "Etimesgut",
   "il": "Ankara",
   "FIELD3": 501.351
 },
 {
   "ilce": "Mamak",
   "il": "Ankara",
   "FIELD3": 587.565
 },
 {
   "ilce": "Yenimahalle",
   "il": "Ankara",
   "FIELD3": 608.217
 },
 {
   "ilce": "Keçiören",
   "il": "Ankara",
   "FIELD3": 872.025
 },
 {
   "ilce": "Çankaya",
   "il": "Ankara",
   "FIELD3": 913.715
 },
 {
   "ilce": "İbradı",
   "il": "Antalya",
   "FIELD3": 2.8
 },
 {
   "ilce": "Gündoğmuş",
   "il": "Antalya",
   "FIELD3": 7.949
 },
 {
   "ilce": "Akseki",
   "il": "Antalya",
   "FIELD3": 12.254
 },
 {
   "ilce": "Demre",
   "il": "Antalya",
   "FIELD3": 26.059
 },
 {
   "ilce": "Elmalı",
   "il": "Antalya",
   "FIELD3": 38.598
 },
 {
   "ilce": "Kemer",
   "il": "Antalya",
   "FIELD3": 41.621
 },
 {
   "ilce": "Finike",
   "il": "Antalya",
   "FIELD3": 46.853
 },
 {
   "ilce": "Gazipaşa",
   "il": "Antalya",
   "FIELD3": 48.561
 },
 {
   "ilce": "Korkuteli",
   "il": "Antalya",
   "FIELD3": 52.913
 },
 {
   "ilce": "Döşemealtı",
   "il": "Antalya",
   "FIELD3": 53.554
 },
 {
   "ilce": "Kaş",
   "il": "Antalya",
   "FIELD3": 55.574
 },
 {
   "ilce": "Kumluca",
   "il": "Antalya",
   "FIELD3": 66.783
 },
 {
   "ilce": "Aksu",
   "il": "Antalya",
   "FIELD3": 68.106
 },
 {
   "ilce": "Serik",
   "il": "Antalya",
   "FIELD3": 117.67
 },
 {
   "ilce": "Konyaaltı",
   "il": "Antalya",
   "FIELD3": 145.648
 },
 {
   "ilce": "Manavgat",
   "il": "Antalya",
   "FIELD3": 215.526
 },
 {
   "ilce": "Alanya",
   "il": "Antalya",
   "FIELD3": 285.407
 },
 {
   "ilce": "Muratpaşa",
   "il": "Antalya",
   "FIELD3": 465.927
 },
 {
   "ilce": "Kepez",
   "il": "Antalya",
   "FIELD3": 470.759
 },
 {
   "ilce": "Damal",
   "il": "Ardahan",
   "FIELD3": 5.767
 },
 {
   "ilce": "Posof",
   "il": "Ardahan",
   "FIELD3": 7.322
 },
 {
   "ilce": "Hanak",
   "il": "Ardahan",
   "FIELD3": 9.484
 },
 {
   "ilce": "Çıldır",
   "il": "Ardahan",
   "FIELD3": 10.134
 },
 {
   "ilce": "Göle",
   "il": "Ardahan",
   "FIELD3": 27.142
 },
 {
   "ilce": "Ardahan",
   "il": "Ardahan",
   "FIELD3": 40.96
 },
 {
   "ilce": "Murgul",
   "il": "Artvin",
   "FIELD3": 6.142
 },
 {
   "ilce": "Ardanuç",
   "il": "Artvin",
   "FIELD3": 11.16
 },
 {
   "ilce": "Şavşat",
   "il": "Artvin",
   "FIELD3": 19.024
 },
 {
   "ilce": "Arhavi",
   "il": "Artvin",
   "FIELD3": 20.306
 },
 {
   "ilce": "Yusufeli",
   "il": "Artvin",
   "FIELD3": 21.596
 },
 {
   "ilce": "Borçka",
   "il": "Artvin",
   "FIELD3": 23.162
 },
 {
   "ilce": "Artvin",
   "il": "Artvin",
   "FIELD3": 34.05
 },
 {
   "ilce": "Hopa",
   "il": "Artvin",
   "FIELD3": 34.234
 },
 {
   "ilce": "Karpuzlu",
   "il": "Aydın",
   "FIELD3": 11.603
 },
 {
   "ilce": "Buharkent",
   "il": "Aydın",
   "FIELD3": 12.458
 },
 {
   "ilce": "Yenipazar",
   "il": "Aydın",
   "FIELD3": 12.963
 },
 {
   "ilce": "Karacasu",
   "il": "Aydın",
   "FIELD3": 19.536
 },
 {
   "ilce": "Sultanhisar",
   "il": "Aydın",
   "FIELD3": 20.91
 },
 {
   "ilce": "Koçarlı",
   "il": "Aydın",
   "FIELD3": 23.859
 },
 {
   "ilce": "Köşk",
   "il": "Aydın",
   "FIELD3": 27.005
 },
 {
   "ilce": "Kuyucak",
   "il": "Aydın",
   "FIELD3": 27.505
 },
 {
   "ilce": "Bozdoğan",
   "il": "Aydın",
   "FIELD3": 34.576
 },
 {
   "ilce": "Germencik",
   "il": "Aydın",
   "FIELD3": 43.256
 },
 {
   "ilce": "İncirliova",
   "il": "Aydın",
   "FIELD3": 46.132
 },
 {
   "ilce": "Çine",
   "il": "Aydın",
   "FIELD3": 50.585
 },
 {
   "ilce": "Didim",
   "il": "Aydın",
   "FIELD3": 73.385
 },
 {
   "ilce": "Kuşadası",
   "il": "Aydın",
   "FIELD3": 101.619
 },
 {
   "ilce": "Söke",
   "il": "Aydın",
   "FIELD3": 115.936
 },
 {
   "ilce": "Nazilli",
   "il": "Aydın",
   "FIELD3": 149.816
 },
 {
   "ilce": "Efeler",
   "il": "Aydın",
   "FIELD3": 270.835
 },
 {
   "ilce": "Hamur",
   "il": "Ağrı",
   "FIELD3": 20.364
 },
 {
   "ilce": "Taşlıçay",
   "il": "Ağrı",
   "FIELD3": 21.611
 },
 {
   "ilce": "Tutak",
   "il": "Ağrı",
   "FIELD3": 32.58
 },
 {
   "ilce": "Eleşkirt",
   "il": "Ağrı",
   "FIELD3": 37.744
 },
 {
   "ilce": "Diyadin",
   "il": "Ağrı",
   "FIELD3": 44.693
 },
 {
   "ilce": "Doğubayazıt",
   "il": "Ağrı",
   "FIELD3": 121.112
 },
 {
   "ilce": "Patnos",
   "il": "Ağrı",
   "FIELD3": 125.324
 },
 {
   "ilce": "Ağrı",
   "il": "Ağrı",
   "FIELD3": 146.007
 },
 {
   "ilce": "Marmara",
   "il": "Balıkesir",
   "FIELD3": 9.456
 },
 {
   "ilce": "Gömeç",
   "il": "Balıkesir",
   "FIELD3": 13.431
 },
 {
   "ilce": "Balya",
   "il": "Balıkesir",
   "FIELD3": 13.912
 },
 {
   "ilce": "Savaştepe",
   "il": "Balıkesir",
   "FIELD3": 18.863
 },
 {
   "ilce": "Manyas",
   "il": "Balıkesir",
   "FIELD3": 20.477
 },
 {
   "ilce": "Kepsut",
   "il": "Balıkesir",
   "FIELD3": 24.18
 },
 {
   "ilce": "Havran",
   "il": "Balıkesir",
   "FIELD3": 27.876
 },
 {
   "ilce": "İvrindi",
   "il": "Balıkesir",
   "FIELD3": 34.207
 },
 {
   "ilce": "Erdek",
   "il": "Balıkesir",
   "FIELD3": 34.676
 },
 {
   "ilce": "Sındırgı",
   "il": "Balıkesir",
   "FIELD3": 35.591
 },
 {
   "ilce": "Dursunbey",
   "il": "Balıkesir",
   "FIELD3": 39.411
 },
 {
   "ilce": "Susurluk",
   "il": "Balıkesir",
   "FIELD3": 39.929
 },
 {
   "ilce": "Bigadiç",
   "il": "Balıkesir",
   "FIELD3": 48.47
 },
 {
   "ilce": "Burhaniye",
   "il": "Balıkesir",
   "FIELD3": 57.554
 },
 {
   "ilce": "Ayvalık",
   "il": "Balıkesir",
   "FIELD3": 69.88
 },
 {
   "ilce": "Gönen",
   "il": "Balıkesir",
   "FIELD3": 73.095
 },
 {
   "ilce": "Edremit",
   "il": "Balıkesir",
   "FIELD3": 140.161
 },
 {
   "ilce": "Bandırma",
   "il": "Balıkesir",
   "FIELD3": 145.089
 },
 {
   "ilce": "Karesi",
   "il": "Balıkesir",
   "FIELD3": 170.776
 },
 {
   "ilce": "Altıeylül",
   "il": "Balıkesir",
   "FIELD3": 172.023
 },
 {
   "ilce": "Kurucaşile",
   "il": "Bartın",
   "FIELD3": 6.844
 },
 {
   "ilce": "Amasra",
   "il": "Bartın",
   "FIELD3": 15.376
 },
 {
   "ilce": "Ulus",
   "il": "Bartın",
   "FIELD3": 21.955
 },
 {
   "ilce": "Bartın",
   "il": "Bartın",
   "FIELD3": 145.23
 },
 {
   "ilce": "Hasankeyf",
   "il": "Batman",
   "FIELD3": 6.509
 },
 {
   "ilce": "Gercüş",
   "il": "Batman",
   "FIELD3": 20.862
 },
 {
   "ilce": "Beşiri",
   "il": "Batman",
   "FIELD3": 30.327
 },
 {
   "ilce": "Sason",
   "il": "Batman",
   "FIELD3": 30.646
 },
 {
   "ilce": "Kozluk",
   "il": "Batman",
   "FIELD3": 61.001
 },
 {
   "ilce": "Batman",
   "il": "Batman",
   "FIELD3": 408.248
 },
 {
   "ilce": "Aydıntepe",
   "il": "Bayburt",
   "FIELD3": 7.026
 },
 {
   "ilce": "Demirözü",
   "il": "Bayburt",
   "FIELD3": 9.733
 },
 {
   "ilce": "Bayburt",
   "il": "Bayburt",
   "FIELD3": 63.848
 },
 {
   "ilce": "İnhisar",
   "il": "Bilecik",
   "FIELD3": 2.61
 },
 {
   "ilce": "Yenipazar",
   "il": "Bilecik",
   "FIELD3": 3.106
 },
 {
   "ilce": "Gölpazarı",
   "il": "Bilecik",
   "FIELD3": 10.016
 },
 {
   "ilce": "Pazaryeri",
   "il": "Bilecik",
   "FIELD3": 11.099
 },
 {
   "ilce": "Söğüt",
   "il": "Bilecik",
   "FIELD3": 19.785
 },
 {
   "ilce": "Osmaneli",
   "il": "Bilecik",
   "FIELD3": 20.934
 },
 {
   "ilce": "Bozüyük",
   "il": "Bilecik",
   "FIELD3": 69.764
 },
 {
   "ilce": "Bilecik",
   "il": "Bilecik",
   "FIELD3": 72.611
 },
 {
   "ilce": "Yayladere",
   "il": "Bingöl",
   "FIELD3": 1.957
 },
 {
   "ilce": "Yedisu",
   "il": "Bingöl",
   "FIELD3": 2.957
 },
 {
   "ilce": "Kiğı",
   "il": "Bingöl",
   "FIELD3": 5.496
 },
 {
   "ilce": "Adaklı",
   "il": "Bingöl",
   "FIELD3": 8.905
 },
 {
   "ilce": "Karlıova",
   "il": "Bingöl",
   "FIELD3": 31.467
 },
 {
   "ilce": "Solhan",
   "il": "Bingöl",
   "FIELD3": 33.256
 },
 {
   "ilce": "Genç",
   "il": "Bingöl",
   "FIELD3": 34.894
 },
 {
   "ilce": "Bingöl",
   "il": "Bingöl",
   "FIELD3": 147.087
 },
 {
   "ilce": "Adilcevaz",
   "il": "Bitlis",
   "FIELD3": 31.196
 },
 {
   "ilce": "Mutki",
   "il": "Bitlis",
   "FIELD3": 32.528
 },
 {
   "ilce": "Hizan",
   "il": "Bitlis",
   "FIELD3": 36.663
 },
 {
   "ilce": "Ahlat",
   "il": "Bitlis",
   "FIELD3": 38.121
 },
 {
   "ilce": "Güroymak",
   "il": "Bitlis",
   "FIELD3": 46.269
 },
 {
   "ilce": "Bitlis",
   "il": "Bitlis",
   "FIELD3": 66.732
 },
 {
   "ilce": "Tatvan",
   "il": "Bitlis",
   "FIELD3": 86.514
 },
 {
   "ilce": "Kıbrıscık",
   "il": "Bolu",
   "FIELD3": 3.461
 },
 {
   "ilce": "Seben",
   "il": "Bolu",
   "FIELD3": 5.552
 },
 {
   "ilce": "Dörtdivan",
   "il": "Bolu",
   "FIELD3": 6.527
 },
 {
   "ilce": "Yeniçağa",
   "il": "Bolu",
   "FIELD3": 7.499
 },
 {
   "ilce": "Mengen",
   "il": "Bolu",
   "FIELD3": 14.042
 },
 {
   "ilce": "Göynük",
   "il": "Bolu",
   "FIELD3": 15.772
 },
 {
   "ilce": "Mudurnu",
   "il": "Bolu",
   "FIELD3": 19.987
 },
 {
   "ilce": "Gerede",
   "il": "Bolu",
   "FIELD3": 34.094
 },
 {
   "ilce": "Bolu",
   "il": "Bolu",
   "FIELD3": 177.855
 },
 {
   "ilce": "Kemer",
   "il": "Burdur",
   "FIELD3": 3.594
 },
 {
   "ilce": "Çeltikçi",
   "il": "Burdur",
   "FIELD3": 5.375
 },
 {
   "ilce": "Altınyayla",
   "il": "Burdur",
   "FIELD3": 5.601
 },
 {
   "ilce": "Karamanlı",
   "il": "Burdur",
   "FIELD3": 8.079
 },
 {
   "ilce": "Ağlasun",
   "il": "Burdur",
   "FIELD3": 8.679
 },
 {
   "ilce": "Tefenni",
   "il": "Burdur",
   "FIELD3": 10.29
 },
 {
   "ilce": "Çavdır",
   "il": "Burdur",
   "FIELD3": 12.891
 },
 {
   "ilce": "Yeşilova",
   "il": "Burdur",
   "FIELD3": 16.622
 },
 {
   "ilce": "Gölhisar",
   "il": "Burdur",
   "FIELD3": 21.671
 },
 {
   "ilce": "Bucak",
   "il": "Burdur",
   "FIELD3": 64.763
 },
 {
   "ilce": "Burdur",
   "il": "Burdur",
   "FIELD3": 99.333
 },
 {
   "ilce": "Harmancık",
   "il": "Bursa",
   "FIELD3": 6.873
 },
 {
   "ilce": "Büyükorhan",
   "il": "Bursa",
   "FIELD3": 11.396
 },
 {
   "ilce": "Keles",
   "il": "Bursa",
   "FIELD3": 13.123
 },
 {
   "ilce": "Orhaneli",
   "il": "Bursa",
   "FIELD3": 21.563
 },
 {
   "ilce": "İznik",
   "il": "Bursa",
   "FIELD3": 42.727
 },
 {
   "ilce": "Yenişehir",
   "il": "Bursa",
   "FIELD3": 52.215
 },
 {
   "ilce": "Kestel",
   "il": "Bursa",
   "FIELD3": 52.938
 },
 {
   "ilce": "Gürsu",
   "il": "Bursa",
   "FIELD3": 74.827
 },
 {
   "ilce": "Orhangazi",
   "il": "Bursa",
   "FIELD3": 76.143
 },
 {
   "ilce": "Mudanya",
   "il": "Bursa",
   "FIELD3": 80.385
 },
 {
   "ilce": "Karacabey",
   "il": "Bursa",
   "FIELD3": 80.594
 },
 {
   "ilce": "Mustafakemalpaşa",
   "il": "Bursa",
   "FIELD3": 99.651
 },
 {
   "ilce": "Gemlik",
   "il": "Bursa",
   "FIELD3": 103.39
 },
 {
   "ilce": "İnegöl",
   "il": "Bursa",
   "FIELD3": 242.232
 },
 {
   "ilce": "Nilüfer",
   "il": "Bursa",
   "FIELD3": 375.474
 },
 {
   "ilce": "Yıldırım",
   "il": "Bursa",
   "FIELD3": 640.746
 },
 {
   "ilce": "Osmangazi",
   "il": "Bursa",
   "FIELD3": 813.262
 },
 {
   "ilce": "Baklan",
   "il": "Denizli",
   "FIELD3": 5.8
 },
 {
   "ilce": "Babadağ",
   "il": "Denizli",
   "FIELD3": 6.623
 },
 {
   "ilce": "Beyağaç",
   "il": "Denizli",
   "FIELD3": 6.922
 },
 {
   "ilce": "Bekilli",
   "il": "Denizli",
   "FIELD3": 7.512
 },
 {
   "ilce": "Çardak",
   "il": "Denizli",
   "FIELD3": 9.076
 },
 {
   "ilce": "Güney",
   "il": "Denizli",
   "FIELD3": 10.697
 },
 {
   "ilce": "Bozkurt",
   "il": "Denizli",
   "FIELD3": 12.352
 },
 {
   "ilce": "Serinhisar",
   "il": "Denizli",
   "FIELD3": 14.796
 },
 {
   "ilce": "Çameli",
   "il": "Denizli",
   "FIELD3": 18.819
 },
 {
   "ilce": "Çal",
   "il": "Denizli",
   "FIELD3": 20.218
 },
 {
   "ilce": "Kale",
   "il": "Denizli",
   "FIELD3": 21.133
 },
 {
   "ilce": "Buldan",
   "il": "Denizli",
   "FIELD3": 27.455
 },
 {
   "ilce": "Sarayköy",
   "il": "Denizli",
   "FIELD3": 29.739
 },
 {
   "ilce": "Honaz",
   "il": "Denizli",
   "FIELD3": 32.282
 },
 {
   "ilce": "Tavas",
   "il": "Denizli",
   "FIELD3": 46.463
 },
 {
   "ilce": "Acıpayam",
   "il": "Denizli",
   "FIELD3": 55.722
 },
 {
   "ilce": "Çivril",
   "il": "Denizli",
   "FIELD3": 61.007
 },
 {
   "ilce": "Merkezefendi",
   "il": "Denizli",
   "FIELD3": 271.942
 },
 {
   "ilce": "Pamukkale",
   "il": "Denizli",
   "FIELD3": 320.142
 },
 {
   "ilce": "Çüngüş",
   "il": "Diyarbakır",
   "FIELD3": 12.895
 },
 {
   "ilce": "Kocaköy",
   "il": "Diyarbakır",
   "FIELD3": 16.357
 },
 {
   "ilce": "Hazro",
   "il": "Diyarbakır",
   "FIELD3": 17.054
 },
 {
   "ilce": "Eğil",
   "il": "Diyarbakır",
   "FIELD3": 22.786
 },
 {
   "ilce": "Lice",
   "il": "Diyarbakır",
   "FIELD3": 26.427
 },
 {
   "ilce": "Hani",
   "il": "Diyarbakır",
   "FIELD3": 32.413
 },
 {
   "ilce": "Kulp",
   "il": "Diyarbakır",
   "FIELD3": 36.215
 },
 {
   "ilce": "Dicle",
   "il": "Diyarbakır",
   "FIELD3": 40.033
 },
 {
   "ilce": "Çermik",
   "il": "Diyarbakır",
   "FIELD3": 50.928
 },
 {
   "ilce": "Çınar",
   "il": "Diyarbakır",
   "FIELD3": 69.38
 },
 {
   "ilce": "Silvan",
   "il": "Diyarbakır",
   "FIELD3": 86.633
 },
 {
   "ilce": "Bismil",
   "il": "Diyarbakır",
   "FIELD3": 112.461
 },
 {
   "ilce": "Sur",
   "il": "Diyarbakır",
   "FIELD3": 121.75
 },
 {
   "ilce": "Ergani",
   "il": "Diyarbakır",
   "FIELD3": 123.474
 },
 {
   "ilce": "Yenişehir",
   "il": "Diyarbakır",
   "FIELD3": 206.534
 },
 {
   "ilce": "Kayapınar",
   "il": "Diyarbakır",
   "FIELD3": 292.394
 },
 {
   "ilce": "Bağlar",
   "il": "Diyarbakır",
   "FIELD3": 367.314
 },
 {
   "ilce": "Cumayeri",
   "il": "Düzce",
   "FIELD3": 13.332
 },
 {
   "ilce": "Gümüşova",
   "il": "Düzce",
   "FIELD3": 14.685
 },
 {
   "ilce": "Yığılca",
   "il": "Düzce",
   "FIELD3": 16.09
 },
 {
   "ilce": "Çilimli",
   "il": "Düzce",
   "FIELD3": 17.645
 },
 {
   "ilce": "Gölyaka",
   "il": "Düzce",
   "FIELD3": 20.226
 },
 {
   "ilce": "Kaynaşlı",
   "il": "Düzce",
   "FIELD3": 20.833
 },
 {
   "ilce": "Akçakoca",
   "il": "Düzce",
   "FIELD3": 37.747
 },
 {
   "ilce": "Düzce",
   "il": "Düzce",
   "FIELD3": 214.991
 },
 {
   "ilce": "Lalapaşa",
   "il": "Edirne",
   "FIELD3": 7.077
 },
 {
   "ilce": "Süloğlu",
   "il": "Edirne",
   "FIELD3": 7.823
 },
 {
   "ilce": "Enez",
   "il": "Edirne",
   "FIELD3": 11.203
 },
 {
   "ilce": "Meriç",
   "il": "Edirne",
   "FIELD3": 14.509
 },
 {
   "ilce": "Havsa",
   "il": "Edirne",
   "FIELD3": 19.976
 },
 {
   "ilce": "İpsala",
   "il": "Edirne",
   "FIELD3": 28.915
 },
 {
   "ilce": "Uzunköprü",
   "il": "Edirne",
   "FIELD3": 64.312
 },
 {
   "ilce": "Keşan",
   "il": "Edirne",
   "FIELD3": 80.486
 },
 {
   "ilce": "Edirne",
   "il": "Edirne",
   "FIELD3": 165.979
 },
 {
   "ilce": "Ağın",
   "il": "Elazığ",
   "FIELD3": 2.819
 },
 {
   "ilce": "Alacakaya",
   "il": "Elazığ",
   "FIELD3": 6.885
 },
 {
   "ilce": "Keban",
   "il": "Elazığ",
   "FIELD3": 7.031
 },
 {
   "ilce": "Sivrice",
   "il": "Elazığ",
   "FIELD3": 8.857
 },
 {
   "ilce": "Maden",
   "il": "Elazığ",
   "FIELD3": 12.46
 },
 {
   "ilce": "Baskil",
   "il": "Elazığ",
   "FIELD3": 14.466
 },
 {
   "ilce": "Arıcak",
   "il": "Elazığ",
   "FIELD3": 15.306
 },
 {
   "ilce": "Palu",
   "il": "Elazığ",
   "FIELD3": 20.035
 },
 {
   "ilce": "Karakoçan",
   "il": "Elazığ",
   "FIELD3": 28.884
 },
 {
   "ilce": "Kovancılar",
   "il": "Elazığ",
   "FIELD3": 39.79
 },
 {
   "ilce": "Elazığ",
   "il": "Elazığ",
   "FIELD3": 412.22
 },
 {
   "ilce": "Otlukbeli",
   "il": "Erzincan",
   "FIELD3": 2.63
 },
 {
   "ilce": "Kemaliye",
   "il": "Erzincan",
   "FIELD3": 5.238
 },
 {
   "ilce": "İliç",
   "il": "Erzincan",
   "FIELD3": 7.717
 },
 {
   "ilce": "Kemah",
   "il": "Erzincan",
   "FIELD3": 7.76
 },
 {
   "ilce": "Çayırlı",
   "il": "Erzincan",
   "FIELD3": 9.602
 },
 {
   "ilce": "Üzümlü",
   "il": "Erzincan",
   "FIELD3": 11.376
 },
 {
   "ilce": "Refahiye",
   "il": "Erzincan",
   "FIELD3": 11.66
 },
 {
   "ilce": "Tercan",
   "il": "Erzincan",
   "FIELD3": 17.771
 },
 {
   "ilce": "Erzincan",
   "il": "Erzincan",
   "FIELD3": 149.879
 },
 {
   "ilce": "Pazaryolu",
   "il": "Erzurum",
   "FIELD3": 4.601
 },
 {
   "ilce": "Olur",
   "il": "Erzurum",
   "FIELD3": 7.082
 },
 {
   "ilce": "Uzundere",
   "il": "Erzurum",
   "FIELD3": 8.465
 },
 {
   "ilce": "Narman",
   "il": "Erzurum",
   "FIELD3": 14.632
 },
 {
   "ilce": "İspir",
   "il": "Erzurum",
   "FIELD3": 16.869
 },
 {
   "ilce": "Köprüköy",
   "il": "Erzurum",
   "FIELD3": 17.043
 },
 {
   "ilce": "Tortum",
   "il": "Erzurum",
   "FIELD3": 17.394
 },
 {
   "ilce": "Çat",
   "il": "Erzurum",
   "FIELD3": 18.505
 },
 {
   "ilce": "Şenkaya",
   "il": "Erzurum",
   "FIELD3": 19.979
 },
 {
   "ilce": "Aşkale",
   "il": "Erzurum",
   "FIELD3": 24.073
 },
 {
   "ilce": "Karaçoban",
   "il": "Erzurum",
   "FIELD3": 24.641
 },
 {
   "ilce": "Tekman",
   "il": "Erzurum",
   "FIELD3": 27.775
 },
 {
   "ilce": "Hınıs",
   "il": "Erzurum",
   "FIELD3": 28.607
 },
 {
   "ilce": "Karayazı",
   "il": "Erzurum",
   "FIELD3": 30.591
 },
 {
   "ilce": "Pasinler",
   "il": "Erzurum",
   "FIELD3": 30.646
 },
 {
   "ilce": "Oltu",
   "il": "Erzurum",
   "FIELD3": 31.424
 },
 {
   "ilce": "Horasan",
   "il": "Erzurum",
   "FIELD3": 41.31
 },
 {
   "ilce": "Aziziye",
   "il": "Erzurum",
   "FIELD3": 51.605
 },
 {
   "ilce": "Palandöken",
   "il": "Erzurum",
   "FIELD3": 164.146
 },
 {
   "ilce": "Yakutiye",
   "il": "Erzurum",
   "FIELD3": 183.932
 },
 {
   "ilce": "Han",
   "il": "Eskişehir",
   "FIELD3": 2.04
 },
 {
   "ilce": "Mihalgazi",
   "il": "Eskişehir",
   "FIELD3": 4.412
 },
 {
   "ilce": "Sarıcakaya",
   "il": "Eskişehir",
   "FIELD3": 5.61
 },
 {
   "ilce": "Günyüzü",
   "il": "Eskişehir",
   "FIELD3": 6
 },
 {
   "ilce": "Beylikova",
   "il": "Eskişehir",
   "FIELD3": 6.083
 },
 {
   "ilce": "İnönü",
   "il": "Eskişehir",
   "FIELD3": 7.006
 },
 {
   "ilce": "Mahmudiye",
   "il": "Eskişehir",
   "FIELD3": 8.221
 },
 {
   "ilce": "Mihalıççık",
   "il": "Eskişehir",
   "FIELD3": 9.302
 },
 {
   "ilce": "Alpu",
   "il": "Eskişehir",
   "FIELD3": 11.822
 },
 {
   "ilce": "Seyitgazi",
   "il": "Eskişehir",
   "FIELD3": 14.24
 },
 {
   "ilce": "Çifteler",
   "il": "Eskişehir",
   "FIELD3": 15.513
 },
 {
   "ilce": "Sivrihisar",
   "il": "Eskişehir",
   "FIELD3": 21.79
 },
 {
   "ilce": "Tepebaşı",
   "il": "Eskişehir",
   "FIELD3": 323.631
 },
 {
   "ilce": "Odunpazarı",
   "il": "Eskişehir",
   "FIELD3": 376.65
 },
 {
   "ilce": "Karkamış",
   "il": "Gaziantep",
   "FIELD3": 10.438
 },
 {
   "ilce": "Yavuzeli",
   "il": "Gaziantep",
   "FIELD3": 21.333
 },
 {
   "ilce": "Oğuzeli",
   "il": "Gaziantep",
   "FIELD3": 29.526
 },
 {
   "ilce": "Araban",
   "il": "Gaziantep",
   "FIELD3": 31.835
 },
 {
   "ilce": "Nurdağı",
   "il": "Gaziantep",
   "FIELD3": 37.719
 },
 {
   "ilce": "İslahiye",
   "il": "Gaziantep",
   "FIELD3": 65.869
 },
 {
   "ilce": "Nizip",
   "il": "Gaziantep",
   "FIELD3": 136.365
 },
 {
   "ilce": "Şehitkamil",
   "il": "Gaziantep",
   "FIELD3": 710.853
 },
 {
   "ilce": "Şahinbey",
   "il": "Gaziantep",
   "FIELD3": 845.528
 },
 {
   "ilce": "Çamoluk",
   "il": "Giresun",
   "FIELD3": 6.542
 },
 {
   "ilce": "Doğankent",
   "il": "Giresun",
   "FIELD3": 6.552
 },
 {
   "ilce": "Çanakçı",
   "il": "Giresun",
   "FIELD3": 6.644
 },
 {
   "ilce": "Güce",
   "il": "Giresun",
   "FIELD3": 8.371
 },
 {
   "ilce": "Alucra",
   "il": "Giresun",
   "FIELD3": 12.948
 },
 {
   "ilce": "Eynesil",
   "il": "Giresun",
   "FIELD3": 13.28
 },
 {
   "ilce": "Piraziz",
   "il": "Giresun",
   "FIELD3": 13.292
 },
 {
   "ilce": "Yağlıdere",
   "il": "Giresun",
   "FIELD3": 16.292
 },
 {
   "ilce": "Keşap",
   "il": "Giresun",
   "FIELD3": 20.18
 },
 {
   "ilce": "Dereli",
   "il": "Giresun",
   "FIELD3": 20.615
 },
 {
   "ilce": "Şebinkarahisar",
   "il": "Giresun",
   "FIELD3": 21.68
 },
 {
   "ilce": "Tirebolu",
   "il": "Giresun",
   "FIELD3": 30.695
 },
 {
   "ilce": "Görele",
   "il": "Giresun",
   "FIELD3": 31.367
 },
 {
   "ilce": "Espiye",
   "il": "Giresun",
   "FIELD3": 32.71
 },
 {
   "ilce": "Bulancak",
   "il": "Giresun",
   "FIELD3": 62.644
 },
 {
   "ilce": "Giresun",
   "il": "Giresun",
   "FIELD3": 126.172
 },
 {
   "ilce": "Köse",
   "il": "Gümüşhane",
   "FIELD3": 7.971
 },
 {
   "ilce": "Torul",
   "il": "Gümüşhane",
   "FIELD3": 11.495
 },
 {
   "ilce": "Kürtün",
   "il": "Gümüşhane",
   "FIELD3": 12.229
 },
 {
   "ilce": "Şiran",
   "il": "Gümüşhane",
   "FIELD3": 19.615
 },
 {
   "ilce": "Kelkit",
   "il": "Gümüşhane",
   "FIELD3": 42.415
 },
 {
   "ilce": "Gümüşhane",
   "il": "Gümüşhane",
   "FIELD3": 52.628
 },
 {
   "ilce": "Çukurca",
   "il": "Hakkari",
   "FIELD3": 16.251
 },
 {
   "ilce": "Şemdinli",
   "il": "Hakkari",
   "FIELD3": 63.261
 },
 {
   "ilce": "Hakkâri",
   "il": "Hakkari",
   "FIELD3": 79.335
 },
 {
   "ilce": "Yüksekova",
   "il": "Hakkari",
   "FIELD3": 117.44
 },
 {
   "ilce": "Kumlu",
   "il": "Hatay",
   "FIELD3": 13.345
 },
 {
   "ilce": "Yayladağı",
   "il": "Hatay",
   "FIELD3": 27.8
 },
 {
   "ilce": "Belen",
   "il": "Hatay",
   "FIELD3": 30.577
 },
 {
   "ilce": "Payas",
   "il": "Hatay",
   "FIELD3": 39.857
 },
 {
   "ilce": "Erzin",
   "il": "Hatay",
   "FIELD3": 41.233
 },
 {
   "ilce": "Hassa",
   "il": "Hatay",
   "FIELD3": 54.146
 },
 {
   "ilce": "Altınözü",
   "il": "Hatay",
   "FIELD3": 61.341
 },
 {
   "ilce": "Arsuz",
   "il": "Hatay",
   "FIELD3": 81.001
 },
 {
   "ilce": "Reyhanlı",
   "il": "Hatay",
   "FIELD3": 89.98
 },
 {
   "ilce": "Kırıkhan",
   "il": "Hatay",
   "FIELD3": 107.994
 },
 {
   "ilce": "Dörtyol",
   "il": "Hatay",
   "FIELD3": 117.053
 },
 {
   "ilce": "Samandağ",
   "il": "Hatay",
   "FIELD3": 118.373
 },
 {
   "ilce": "Defne",
   "il": "Hatay",
   "FIELD3": 137.398
 },
 {
   "ilce": "İskenderun",
   "il": "Hatay",
   "FIELD3": 244.97
 },
 {
   "ilce": "Antakya",
   "il": "Hatay",
   "FIELD3": 354.768
 },
 {
   "ilce": "Yenişarbademli",
   "il": "Isparta",
   "FIELD3": 2.359
 },
 {
   "ilce": "Aksu",
   "il": "Isparta",
   "FIELD3": 5.13
 },
 {
   "ilce": "Atabey",
   "il": "Isparta",
   "FIELD3": 5.593
 },
 {
   "ilce": "Uluborlu",
   "il": "Isparta",
   "FIELD3": 7.165
 },
 {
   "ilce": "Gönen",
   "il": "Isparta",
   "FIELD3": 7.649
 },
 {
   "ilce": "Sütçüler",
   "il": "Isparta",
   "FIELD3": 11.464
 },
 {
   "ilce": "Senirkent",
   "il": "Isparta",
   "FIELD3": 12.592
 },
 {
   "ilce": "Keçiborlu",
   "il": "Isparta",
   "FIELD3": 14.329
 },
 {
   "ilce": "Gelendost",
   "il": "Isparta",
   "FIELD3": 16.133
 },
 {
   "ilce": "Şarkikaraağaç",
   "il": "Isparta",
   "FIELD3": 25.769
 },
 {
   "ilce": "Eğirdir",
   "il": "Isparta",
   "FIELD3": 33.064
 },
 {
   "ilce": "Yalvaç",
   "il": "Isparta",
   "FIELD3": 48.803
 },
 {
   "ilce": "Isparta",
   "il": "Isparta",
   "FIELD3": 228.73
 },
 {
   "ilce": "Karakoyunlu",
   "il": "Iğdır",
   "FIELD3": 13.929
 },
 {
   "ilce": "Aralık",
   "il": "Iğdır",
   "FIELD3": 21.843
 },
 {
   "ilce": "Tuzluca",
   "il": "Iğdır",
   "FIELD3": 24.174
 },
 {
   "ilce": "Iğdır",
   "il": "Iğdır",
   "FIELD3": 132.11
 },
 {
   "ilce": "Adalar",
   "il": "İstanbul",
   "FIELD3": 16.052
 },
 {
   "ilce": "Şile",
   "il": "İstanbul",
   "FIELD3": 32.823
 },
 {
   "ilce": "Çatalca",
   "il": "İstanbul",
   "FIELD3": 67.843
 },
 {
   "ilce": "Silivri",
   "il": "İstanbul",
   "FIELD3": 161.165
 },
 {
   "ilce": "Beşiktaş",
   "il": "İstanbul",
   "FIELD3": 188.793
 },
 {
   "ilce": "Çekmeköy",
   "il": "İstanbul",
   "FIELD3": 220.656
 },
 {
   "ilce": "Bakırköy",
   "il": "İstanbul",
   "FIELD3": 221.594
 },
 {
   "ilce": "Tuzla",
   "il": "İstanbul",
   "FIELD3": 221.62
 },
 {
   "ilce": "Büyükçekmece",
   "il": "İstanbul",
   "FIELD3": 223.324
 },
 {
   "ilce": "Arnavutköy",
   "il": "İstanbul",
   "FIELD3": 225.67
 },
 {
   "ilce": "Beyoğlu",
   "il": "İstanbul",
   "FIELD3": 241.52
 },
 {
   "ilce": "Beykoz",
   "il": "İstanbul",
   "FIELD3": 248.071
 },
 {
   "ilce": "Beylikdüzü",
   "il": "İstanbul",
   "FIELD3": 262.473
 },
 {
   "ilce": "Bayrampaşa",
   "il": "İstanbul",
   "FIELD3": 269.809
 },
 {
   "ilce": "Şişli",
   "il": "İstanbul",
   "FIELD3": 272.38
 },
 {
   "ilce": "Zeytinburnu",
   "il": "İstanbul",
   "FIELD3": 287.223
 },
 {
   "ilce": "Güngören",
   "il": "İstanbul",
   "FIELD3": 303.371
 },
 {
   "ilce": "Sultanbeyli",
   "il": "İstanbul",
   "FIELD3": 315.022
 },
 {
   "ilce": "Sancaktepe",
   "il": "İstanbul",
   "FIELD3": 329.788
 },
 {
   "ilce": "Sarıyer",
   "il": "İstanbul",
   "FIELD3": 337.681
 },
 {
   "ilce": "Başakşehir",
   "il": "İstanbul",
   "FIELD3": 342.422
 },
 {
   "ilce": "Eyüp",
   "il": "İstanbul",
   "FIELD3": 367.824
 },
 {
   "ilce": "Ataşehir",
   "il": "İstanbul",
   "FIELD3": 408.986
 },
 {
   "ilce": "Avcılar",
   "il": "İstanbul",
   "FIELD3": 417.852
 },
 {
   "ilce": "Fatih",
   "il": "İstanbul",
   "FIELD3": 419.266
 },
 {
   "ilce": "Kağıthane",
   "il": "İstanbul",
   "FIELD3": 432.23
 },
 {
   "ilce": "Kartal",
   "il": "İstanbul",
   "FIELD3": 450.498
 },
 {
   "ilce": "Esenler",
   "il": "İstanbul",
   "FIELD3": 458.857
 },
 {
   "ilce": "Maltepe",
   "il": "İstanbul",
   "FIELD3": 476.806
 },
 {
   "ilce": "Kadıköy",
   "il": "İstanbul",
   "FIELD3": 482.571
 },
 {
   "ilce": "Gaziosmanpaşa",
   "il": "İstanbul",
   "FIELD3": 498.12
 },
 {
   "ilce": "Sultangazi",
   "il": "İstanbul",
   "FIELD3": 513.022
 },
 {
   "ilce": "Üsküdar",
   "il": "İstanbul",
   "FIELD3": 534.97
 },
 {
   "ilce": "Bahçelievler",
   "il": "İstanbul",
   "FIELD3": 599.027
 },
 {
   "ilce": "Pendik",
   "il": "İstanbul",
   "FIELD3": 663.569
 },
 {
   "ilce": "Ümraniye",
   "il": "İstanbul",
   "FIELD3": 674.131
 },
 {
   "ilce": "Esenyurt",
   "il": "İstanbul",
   "FIELD3": 686.968
 },
 {
   "ilce": "Küçükçekmece",
   "il": "İstanbul",
   "FIELD3": 748.398
 },
 {
   "ilce": "Bağcılar",
   "il": "İstanbul",
   "FIELD3": 754.623
 },
 {
   "ilce": "Karaburun",
   "il": "İzmir",
   "FIELD3": 9.456
 },
 {
   "ilce": "Beydağ",
   "il": "İzmir",
   "FIELD3": 12.457
 },
 {
   "ilce": "Kınık",
   "il": "İzmir",
   "FIELD3": 28.072
 },
 {
   "ilce": "Güzelbahçe",
   "il": "İzmir",
   "FIELD3": 28.47
 },
 {
   "ilce": "Foça",
   "il": "İzmir",
   "FIELD3": 30.002
 },
 {
   "ilce": "Selçuk",
   "il": "İzmir",
   "FIELD3": 35.281
 },
 {
   "ilce": "Seferihisar",
   "il": "İzmir",
   "FIELD3": 35.96
 },
 {
   "ilce": "Çeşme",
   "il": "İzmir",
   "FIELD3": 39.243
 },
 {
   "ilce": "Bayındır",
   "il": "İzmir",
   "FIELD3": 40.31
 },
 {
   "ilce": "Dikili",
   "il": "İzmir",
   "FIELD3": 41.999
 },
 {
   "ilce": "Kiraz",
   "il": "İzmir",
   "FIELD3": 43.971
 },
 {
   "ilce": "Urla",
   "il": "İzmir",
   "FIELD3": 59.166
 },
 {
   "ilce": "Narlıdere",
   "il": "İzmir",
   "FIELD3": 64.599
 },
 {
   "ilce": "Balçova",
   "il": "İzmir",
   "FIELD3": 77.311
 },
 {
   "ilce": "Menderes",
   "il": "İzmir",
   "FIELD3": 81.297
 },
 {
   "ilce": "Tire",
   "il": "İzmir",
   "FIELD3": 81.315
 },
 {
   "ilce": "Aliağa",
   "il": "İzmir",
   "FIELD3": 83.366
 },
 {
   "ilce": "Kemalpaşa",
   "il": "İzmir",
   "FIELD3": 99.626
 },
 {
   "ilce": "Bergama",
   "il": "İzmir",
   "FIELD3": 101.813
 },
 {
   "ilce": "Ödemiş",
   "il": "İzmir",
   "FIELD3": 129.407
 },
 {
   "ilce": "Gaziemir",
   "il": "İzmir",
   "FIELD3": 130.87
 },
 {
   "ilce": "Menemen",
   "il": "İzmir",
   "FIELD3": 148.662
 },
 {
   "ilce": "Torbalı",
   "il": "İzmir",
   "FIELD3": 150.127
 },
 {
   "ilce": "Çiğli",
   "il": "İzmir",
   "FIELD3": 176.864
 },
 {
   "ilce": "Bayraklı",
   "il": "İzmir",
   "FIELD3": 310.765
 },
 {
   "ilce": "Karşıyaka",
   "il": "İzmir",
   "FIELD3": 325.717
 },
 {
   "ilce": "Konak",
   "il": "İzmir",
   "FIELD3": 380.295
 },
 {
   "ilce": "Bornova",
   "il": "İzmir",
   "FIELD3": 431.149
 },
 {
   "ilce": "Buca",
   "il": "İzmir",
   "FIELD3": 461.761
 },
 {
   "ilce": "Karabağlar",
   "il": "İzmir",
   "FIELD3": 473.741
 },
 {
   "ilce": "Ekinözü",
   "il": "Kahramanmaraş",
   "FIELD3": 12.526
 },
 {
   "ilce": "Nurhak",
   "il": "Kahramanmaraş",
   "FIELD3": 13.068
 },
 {
   "ilce": "Çağlayancerit",
   "il": "Kahramanmaraş",
   "FIELD3": 24.548
 },
 {
   "ilce": "Andırın",
   "il": "Kahramanmaraş",
   "FIELD3": 35.298
 },
 {
   "ilce": "Göksun",
   "il": "Kahramanmaraş",
   "FIELD3": 52.142
 },
 {
   "ilce": "Türkoğlu",
   "il": "Kahramanmaraş",
   "FIELD3": 68.423
 },
 {
   "ilce": "Pazarcık",
   "il": "Kahramanmaraş",
   "FIELD3": 69.32
 },
 {
   "ilce": "Afşin",
   "il": "Kahramanmaraş",
   "FIELD3": 82.122
 },
 {
   "ilce": "Elbistan",
   "il": "Kahramanmaraş",
   "FIELD3": 142.168
 },
 {
   "ilce": "Dulkadiroğlu",
   "il": "Kahramanmaraş",
   "FIELD3": 218.029
 },
 {
   "ilce": "Onikişubat",
   "il": "Kahramanmaraş",
   "FIELD3": 371.394
 },
 {
   "ilce": "Ovacık",
   "il": "Karabük",
   "FIELD3": 3.168
 },
 {
   "ilce": "Eflani",
   "il": "Karabük",
   "FIELD3": 8.918
 },
 {
   "ilce": "Eskipazar",
   "il": "Karabük",
   "FIELD3": 12.544
 },
 {
   "ilce": "Yenice",
   "il": "Karabük",
   "FIELD3": 20.75
 },
 {
   "ilce": "Safranbolu",
   "il": "Karabük",
   "FIELD3": 58.295
 },
 {
   "ilce": "Karabük",
   "il": "Karabük",
   "FIELD3": 127.658
 },
 {
   "ilce": "Başyayla",
   "il": "Karaman",
   "FIELD3": 3.861
 },
 {
   "ilce": "Kazımkarabekir",
   "il": "Karaman",
   "FIELD3": 4.302
 },
 {
   "ilce": "Ayrancı",
   "il": "Karaman",
   "FIELD3": 8.713
 },
 {
   "ilce": "Sarıveliler",
   "il": "Karaman",
   "FIELD3": 12.146
 },
 {
   "ilce": "Ermenek",
   "il": "Karaman",
   "FIELD3": 29.957
 },
 {
   "ilce": "Karaman",
   "il": "Karaman",
   "FIELD3": 181.383
 },
 {
   "ilce": "Susuz",
   "il": "Kars",
   "FIELD3": 11.302
 },
 {
   "ilce": "Akyaka",
   "il": "Kars",
   "FIELD3": 11.375
 },
 {
   "ilce": "Arpaçay",
   "il": "Kars",
   "FIELD3": 18.737
 },
 {
   "ilce": "Selim",
   "il": "Kars",
   "FIELD3": 24.924
 },
 {
   "ilce": "Digor",
   "il": "Kars",
   "FIELD3": 24.932
 },
 {
   "ilce": "Kağızman",
   "il": "Kars",
   "FIELD3": 46.687
 },
 {
   "ilce": "Sarıkamış",
   "il": "Kars",
   "FIELD3": 47.231
 },
 {
   "ilce": "Kars",
   "il": "Kars",
   "FIELD3": 111.278
 },
 {
   "ilce": "Ağlı",
   "il": "Kastamonu",
   "FIELD3": 2.98
 },
 {
   "ilce": "Hanönü",
   "il": "Kastamonu",
   "FIELD3": 3.976
 },
 {
   "ilce": "Seydiler",
   "il": "Kastamonu",
   "FIELD3": 4.015
 },
 {
   "ilce": "Abana",
   "il": "Kastamonu",
   "FIELD3": 4.175
 },
 {
   "ilce": "Şenpazar",
   "il": "Kastamonu",
   "FIELD3": 4.77
 },
 {
   "ilce": "Pınarbaşı",
   "il": "Kastamonu",
   "FIELD3": 5.59
 },
 {
   "ilce": "İhsangazi",
   "il": "Kastamonu",
   "FIELD3": 6.104
 },
 {
   "ilce": "Doğanyurt",
   "il": "Kastamonu",
   "FIELD3": 6.464
 },
 {
   "ilce": "Çatalzeytin",
   "il": "Kastamonu",
   "FIELD3": 6.551
 },
 {
   "ilce": "Küre",
   "il": "Kastamonu",
   "FIELD3": 6.588
 },
 {
   "ilce": "Azdavay",
   "il": "Kastamonu",
   "FIELD3": 7.154
 },
 {
   "ilce": "Daday",
   "il": "Kastamonu",
   "FIELD3": 9.186
 },
 {
   "ilce": "Bozkurt",
   "il": "Kastamonu",
   "FIELD3": 9.292
 },
 {
   "ilce": "Devrekani",
   "il": "Kastamonu",
   "FIELD3": 12.728
 },
 {
   "ilce": "Araç",
   "il": "Kastamonu",
   "FIELD3": 19.038
 },
 {
   "ilce": "Cide",
   "il": "Kastamonu",
   "FIELD3": 20.613
 },
 {
   "ilce": "İnebolu",
   "il": "Kastamonu",
   "FIELD3": 22.918
 },
 {
   "ilce": "Taşköprü",
   "il": "Kastamonu",
   "FIELD3": 38.775
 },
 {
   "ilce": "Tosya",
   "il": "Kastamonu",
   "FIELD3": 40.599
 },
 {
   "ilce": "Kastamonu",
   "il": "Kastamonu",
   "FIELD3": 137.391
 },
 {
   "ilce": "Özvatan",
   "il": "Kayseri",
   "FIELD3": 3.934
 },
 {
   "ilce": "Akkışla",
   "il": "Kayseri",
   "FIELD3": 6.234
 },
 {
   "ilce": "Felahiye",
   "il": "Kayseri",
   "FIELD3": 6.451
 },
 {
   "ilce": "Sarız",
   "il": "Kayseri",
   "FIELD3": 10.529
 },
 {
   "ilce": "Hacılar",
   "il": "Kayseri",
   "FIELD3": 12.29
 },
 {
   "ilce": "Sarıoğlan",
   "il": "Kayseri",
   "FIELD3": 14.521
 },
 {
   "ilce": "Yeşilhisar",
   "il": "Kayseri",
   "FIELD3": 15.864
 },
 {
   "ilce": "Tomarza",
   "il": "Kayseri",
   "FIELD3": 24.131
 },
 {
   "ilce": "İncesu",
   "il": "Kayseri",
   "FIELD3": 24.405
 },
 {
   "ilce": "Pınarbaşı",
   "il": "Kayseri",
   "FIELD3": 25.293
 },
 {
   "ilce": "Bünyan",
   "il": "Kayseri",
   "FIELD3": 27.944
 },
 {
   "ilce": "Yahyalı",
   "il": "Kayseri",
   "FIELD3": 36.578
 },
 {
   "ilce": "Develi",
   "il": "Kayseri",
   "FIELD3": 64.55
 },
 {
   "ilce": "Talas",
   "il": "Kayseri",
   "FIELD3": 128.414
 },
 {
   "ilce": "Kocasinan",
   "il": "Kayseri",
   "FIELD3": 384.203
 },
 {
   "ilce": "Melikgazi",
   "il": "Kayseri",
   "FIELD3": 537.035
 },
 {
   "ilce": "Polateli",
   "il": "Kilis",
   "FIELD3": 5.306
 },
 {
   "ilce": "Elbeyli",
   "il": "Kilis",
   "FIELD3": 5.982
 },
 {
   "ilce": "Musabeyli",
   "il": "Kilis",
   "FIELD3": 13.962
 },
 {
   "ilce": "Kilis",
   "il": "Kilis",
   "FIELD3": 103.531
 },
 {
   "ilce": "Dilovası",
   "il": "Kocaeli",
   "FIELD3": 45.714
 },
 {
   "ilce": "Kandıra",
   "il": "Kocaeli",
   "FIELD3": 49.203
 },
 {
   "ilce": "Karamürsel",
   "il": "Kocaeli",
   "FIELD3": 54.225
 },
 {
   "ilce": "Başiskele",
   "il": "Kocaeli",
   "FIELD3": 79.625
 },
 {
   "ilce": "Kartepe",
   "il": "Kocaeli",
   "FIELD3": 104.882
 },
 {
   "ilce": "Çayırova",
   "il": "Kocaeli",
   "FIELD3": 109.698
 },
 {
   "ilce": "Derince",
   "il": "Kocaeli",
   "FIELD3": 133.739
 },
 {
   "ilce": "Körfez",
   "il": "Kocaeli",
   "FIELD3": 146.21
 },
 {
   "ilce": "Gölcük",
   "il": "Kocaeli",
   "FIELD3": 149.238
 },
 {
   "ilce": "Darıca",
   "il": "Kocaeli",
   "FIELD3": 173.139
 },
 {
   "ilce": "Gebze",
   "il": "Kocaeli",
   "FIELD3": 338.412
 },
 {
   "ilce": "İzmit",
   "il": "Kocaeli",
   "FIELD3": 338.71
 },
 {
   "ilce": "Yalıhüyük",
   "il": "Konya",
   "FIELD3": 1.666
 },
 {
   "ilce": "Halkapınar",
   "il": "Konya",
   "FIELD3": 4.519
 },
 {
   "ilce": "Derbent",
   "il": "Konya",
   "FIELD3": 4.612
 },
 {
   "ilce": "Ahırlı",
   "il": "Konya",
   "FIELD3": 4.722
 },
 {
   "ilce": "Akören",
   "il": "Konya",
   "FIELD3": 6.39
 },
 {
   "ilce": "Taşkent",
   "il": "Konya",
   "FIELD3": 6.62
 },
 {
   "ilce": "Tuzlukçu",
   "il": "Konya",
   "FIELD3": 6.89
 },
 {
   "ilce": "Derebucak",
   "il": "Konya",
   "FIELD3": 7.272
 },
 {
   "ilce": "Emirgazi",
   "il": "Konya",
   "FIELD3": 9.135
 },
 {
   "ilce": "Güneysınır",
   "il": "Konya",
   "FIELD3": 9.769
 },
 {
   "ilce": "Çeltik",
   "il": "Konya",
   "FIELD3": 10.209
 },
 {
   "ilce": "Hadim",
   "il": "Konya",
   "FIELD3": 13.26
 },
 {
   "ilce": "Altınekin",
   "il": "Konya",
   "FIELD3": 14.357
 },
 {
   "ilce": "Hüyük",
   "il": "Konya",
   "FIELD3": 16.296
 },
 {
   "ilce": "Doğanhisar",
   "il": "Konya",
   "FIELD3": 17.683
 },
 {
   "ilce": "Yunak",
   "il": "Konya",
   "FIELD3": 23.956
 },
 {
   "ilce": "Sarayönü",
   "il": "Konya",
   "FIELD3": 26.355
 },
 {
   "ilce": "Bozkır",
   "il": "Konya",
   "FIELD3": 27.457
 },
 {
   "ilce": "Kadınhanı",
   "il": "Konya",
   "FIELD3": 33.065
 },
 {
   "ilce": "Karapınar",
   "il": "Konya",
   "FIELD3": 48.968
 },
 {
   "ilce": "Kulu",
   "il": "Konya",
   "FIELD3": 50.675
 },
 {
   "ilce": "Cihanbeyli",
   "il": "Konya",
   "FIELD3": 54.892
 },
 {
   "ilce": "Ilgın",
   "il": "Konya",
   "FIELD3": 55.79
 },
 {
   "ilce": "Seydişehir",
   "il": "Konya",
   "FIELD3": 63.773
 },
 {
   "ilce": "Çumra",
   "il": "Konya",
   "FIELD3": 65.054
 },
 {
   "ilce": "Beyşehir",
   "il": "Konya",
   "FIELD3": 71.366
 },
 {
   "ilce": "Akşehir",
   "il": "Konya",
   "FIELD3": 94.133
 },
 {
   "ilce": "Ereğli",
   "il": "Konya",
   "FIELD3": 139.131
 },
 {
   "ilce": "Karatay",
   "il": "Konya",
   "FIELD3": 295.332
 },
 {
   "ilce": "Meram",
   "il": "Konya",
   "FIELD3": 340.817
 },
 {
   "ilce": "Selçuklu",
   "il": "Konya",
   "FIELD3": 584.644
 },
 {
   "ilce": "Dumlupınar",
   "il": "Kütahya",
   "FIELD3": 2.986
 },
 {
   "ilce": "Pazarlar",
   "il": "Kütahya",
   "FIELD3": 5.335
 },
 {
   "ilce": "Şaphane",
   "il": "Kütahya",
   "FIELD3": 7.038
 },
 {
   "ilce": "Çavdarhisar",
   "il": "Kütahya",
   "FIELD3": 7.349
 },
 {
   "ilce": "Aslanapa",
   "il": "Kütahya",
   "FIELD3": 10.249
 },
 {
   "ilce": "Hisarcık",
   "il": "Kütahya",
   "FIELD3": 13.438
 },
 {
   "ilce": "Domaniç",
   "il": "Kütahya",
   "FIELD3": 15.424
 },
 {
   "ilce": "Altıntaş",
   "il": "Kütahya",
   "FIELD3": 17.071
 },
 {
   "ilce": "Emet",
   "il": "Kütahya",
   "FIELD3": 21.506
 },
 {
   "ilce": "Gediz",
   "il": "Kütahya",
   "FIELD3": 51.185
 },
 {
   "ilce": "Simav",
   "il": "Kütahya",
   "FIELD3": 64.899
 },
 {
   "ilce": "Tavşanlı",
   "il": "Kütahya",
   "FIELD3": 101.899
 },
 {
   "ilce": "Kütahya",
   "il": "Kütahya",
   "FIELD3": 253.175
 },
 {
   "ilce": "Kofçaz",
   "il": "Kırklareli",
   "FIELD3": 2.707
 },
 {
   "ilce": "Pehlivanköy",
   "il": "Kırklareli",
   "FIELD3": 3.965
 },
 {
   "ilce": "Demirköy",
   "il": "Kırklareli",
   "FIELD3": 8.566
 },
 {
   "ilce": "Pınarhisar",
   "il": "Kırklareli",
   "FIELD3": 18.914
 },
 {
   "ilce": "Vize",
   "il": "Kırklareli",
   "FIELD3": 27.7
 },
 {
   "ilce": "Babaeski",
   "il": "Kırklareli",
   "FIELD3": 49.121
 },
 {
   "ilce": "Kırklareli",
   "il": "Kırklareli",
   "FIELD3": 92.514
 },
 {
   "ilce": "Lüleburgaz",
   "il": "Kırklareli",
   "FIELD3": 140.236
 },
 {
   "ilce": "Çelebi",
   "il": "Kırıkkale",
   "FIELD3": 2.318
 },
 {
   "ilce": "Karakeçili",
   "il": "Kırıkkale",
   "FIELD3": 4.077
 },
 {
   "ilce": "Balışeyh",
   "il": "Kırıkkale",
   "FIELD3": 6.1
 },
 {
   "ilce": "Bahşili",
   "il": "Kırıkkale",
   "FIELD3": 6.91
 },
 {
   "ilce": "Sulakyurt",
   "il": "Kırıkkale",
   "FIELD3": 7.089
 },
 {
   "ilce": "Delice",
   "il": "Kırıkkale",
   "FIELD3": 8.914
 },
 {
   "ilce": "Keskin",
   "il": "Kırıkkale",
   "FIELD3": 17.814
 },
 {
   "ilce": "Yahşihan",
   "il": "Kırıkkale",
   "FIELD3": 20.833
 },
 {
   "ilce": "Kırıkkale",
   "il": "Kırıkkale",
   "FIELD3": 197.037
 },
 {
   "ilce": "Akçakent",
   "il": "Kırşehir",
   "FIELD3": 4.184
 },
 {
   "ilce": "Boztepe",
   "il": "Kırşehir",
   "FIELD3": 5.365
 },
 {
   "ilce": "Akpınar",
   "il": "Kırşehir",
   "FIELD3": 7.874
 },
 {
   "ilce": "Çiçekdağı",
   "il": "Kırşehir",
   "FIELD3": 14.863
 },
 {
   "ilce": "Mucur",
   "il": "Kırşehir",
   "FIELD3": 18.633
 },
 {
   "ilce": "Kaman",
   "il": "Kırşehir",
   "FIELD3": 37.421
 },
 {
   "ilce": "Kırşehir",
   "il": "Kırşehir",
   "FIELD3": 134.367
 },
 {
   "ilce": "Doğanyol",
   "il": "Malatya",
   "FIELD3": 4.44
 },
 {
   "ilce": "Kale",
   "il": "Malatya",
   "FIELD3": 5.677
 },
 {
   "ilce": "Arguvan",
   "il": "Malatya",
   "FIELD3": 8.162
 },
 {
   "ilce": "Kuluncak",
   "il": "Malatya",
   "FIELD3": 8.32
 },
 {
   "ilce": "Arapgir",
   "il": "Malatya",
   "FIELD3": 10.796
 },
 {
   "ilce": "Yazıhan",
   "il": "Malatya",
   "FIELD3": 14.315
 },
 {
   "ilce": "Pütürge",
   "il": "Malatya",
   "FIELD3": 16.612
 },
 {
   "ilce": "Hekimhan",
   "il": "Malatya",
   "FIELD3": 19.946
 },
 {
   "ilce": "Darende",
   "il": "Malatya",
   "FIELD3": 28.06
 },
 {
   "ilce": "Akçadağ",
   "il": "Malatya",
   "FIELD3": 29.573
 },
 {
   "ilce": "Doğanşehir",
   "il": "Malatya",
   "FIELD3": 40.064
 },
 {
   "ilce": "Yeşilyurt",
   "il": "Malatya",
   "FIELD3": 283.716
 },
 {
   "ilce": "Battalgazi",
   "il": "Malatya",
   "FIELD3": 299.863
 },
 {
   "ilce": "Köprübaşı",
   "il": "Manisa",
   "FIELD3": 14.191
 },
 {
   "ilce": "Gölmarmara",
   "il": "Manisa",
   "FIELD3": 15.384
 },
 {
   "ilce": "Ahmetli",
   "il": "Manisa",
   "FIELD3": 16.104
 },
 {
   "ilce": "Selendi",
   "il": "Manisa",
   "FIELD3": 21.437
 },
 {
   "ilce": "Gördes",
   "il": "Manisa",
   "FIELD3": 29.768
 },
 {
   "ilce": "Sarıgöl",
   "il": "Manisa",
   "FIELD3": 36.206
 },
 {
   "ilce": "Demirci",
   "il": "Manisa",
   "FIELD3": 43.027
 },
 {
   "ilce": "Kula",
   "il": "Manisa",
   "FIELD3": 45.587
 },
 {
   "ilce": "Kırkağaç",
   "il": "Manisa",
   "FIELD3": 45.73
 },
 {
   "ilce": "Saruhanlı",
   "il": "Manisa",
   "FIELD3": 53.684
 },
 {
   "ilce": "Alaşehir",
   "il": "Manisa",
   "FIELD3": 99.962
 },
 {
   "ilce": "Soma",
   "il": "Manisa",
   "FIELD3": 105.518
 },
 {
   "ilce": "Turgutlu",
   "il": "Manisa",
   "FIELD3": 150.46
 },
 {
   "ilce": "Salihli",
   "il": "Manisa",
   "FIELD3": 156.861
 },
 {
   "ilce": "Akhisar",
   "il": "Manisa",
   "FIELD3": 163.107
 },
 {
   "ilce": "Şehzadeler",
   "il": "Manisa",
   "FIELD3": 166.443
 },
 {
   "ilce": "Yunusemre",
   "il": "Manisa",
   "FIELD3": 204.436
 },
 {
   "ilce": "Ömerli",
   "il": "Mardin",
   "FIELD3": 14.539
 },
 {
   "ilce": "Yeşilli",
   "il": "Mardin",
   "FIELD3": 17.136
 },
 {
   "ilce": "Dargeçit",
   "il": "Mardin",
   "FIELD3": 28.601
 },
 {
   "ilce": "Savur",
   "il": "Mardin",
   "FIELD3": 29.026
 },
 {
   "ilce": "Mazıdağı",
   "il": "Mardin",
   "FIELD3": 33.07
 },
 {
   "ilce": "Derik",
   "il": "Mardin",
   "FIELD3": 61.32
 },
 {
   "ilce": "Midyat",
   "il": "Mardin",
   "FIELD3": 105.252
 },
 {
   "ilce": "Nusaybin",
   "il": "Mardin",
   "FIELD3": 116.068
 },
 {
   "ilce": "Artuklu",
   "il": "Mardin",
   "FIELD3": 151.356
 },
 {
   "ilce": "Kızıltepe",
   "il": "Mardin",
   "FIELD3": 232.628
 },
 {
   "ilce": "Çamlıyayla",
   "il": "Mersin",
   "FIELD3": 8.65
 },
 {
   "ilce": "Aydıncık",
   "il": "Mersin",
   "FIELD3": 11.241
 },
 {
   "ilce": "Gülnar",
   "il": "Mersin",
   "FIELD3": 26.029
 },
 {
   "ilce": "Bozyazı",
   "il": "Mersin",
   "FIELD3": 26.813
 },
 {
   "ilce": "Mut",
   "il": "Mersin",
   "FIELD3": 62.354
 },
 {
   "ilce": "Anamur",
   "il": "Mersin",
   "FIELD3": 63.983
 },
 {
   "ilce": "Silifke",
   "il": "Mersin",
   "FIELD3": 116.18
 },
 {
   "ilce": "Erdemli",
   "il": "Mersin",
   "FIELD3": 132.938
 },
 {
   "ilce": "Mezitli",
   "il": "Mersin",
   "FIELD3": 164.429
 },
 {
   "ilce": "Yenişehir",
   "il": "Mersin",
   "FIELD3": 233.489
 },
 {
   "ilce": "Akdeniz",
   "il": "Mersin",
   "FIELD3": 276.058
 },
 {
   "ilce": "Toroslar",
   "il": "Mersin",
   "FIELD3": 281.13
 },
 {
   "ilce": "Tarsus",
   "il": "Mersin",
   "FIELD3": 323.961
 },
 {
   "ilce": "Kavaklıdere",
   "il": "Muğla",
   "FIELD3": 10.814
 },
 {
   "ilce": "Datça",
   "il": "Muğla",
   "FIELD3": 20.156
 },
 {
   "ilce": "Ula",
   "il": "Muğla",
   "FIELD3": 23.61
 },
 {
   "ilce": "Köyceğiz",
   "il": "Muğla",
   "FIELD3": 34.027
 },
 {
   "ilce": "Dalaman",
   "il": "Muğla",
   "FIELD3": 35.958
 },
 {
   "ilce": "Yatağan",
   "il": "Muğla",
   "FIELD3": 44.783
 },
 {
   "ilce": "Ortaca",
   "il": "Muğla",
   "FIELD3": 44.827
 },
 {
   "ilce": "Seydikemer",
   "il": "Muğla",
   "FIELD3": 58.771
 },
 {
   "ilce": "Marmaris",
   "il": "Muğla",
   "FIELD3": 88.621
 },
 {
   "ilce": "Menteşe",
   "il": "Muğla",
   "FIELD3": 102.414
 },
 {
   "ilce": "Milas",
   "il": "Muğla",
   "FIELD3": 132.445
 },
 {
   "ilce": "Fethiye",
   "il": "Muğla",
   "FIELD3": 145.643
 },
 {
   "ilce": "Bodrum",
   "il": "Muğla",
   "FIELD3": 152.44
 },
 {
   "ilce": "Korkut",
   "il": "Muş",
   "FIELD3": 26.431
 },
 {
   "ilce": "Hasköy",
   "il": "Muş",
   "FIELD3": 27.24
 },
 {
   "ilce": "Varto",
   "il": "Muş",
   "FIELD3": 32.378
 },
 {
   "ilce": "Malazgirt",
   "il": "Muş",
   "FIELD3": 55.804
 },
 {
   "ilce": "Bulanık",
   "il": "Muş",
   "FIELD3": 83.266
 },
 {
   "ilce": "Muş",
   "il": "Muş",
   "FIELD3": 186.097
 },
 {
   "ilce": "Hacıbektaş",
   "il": "Nevşehir",
   "FIELD3": 11.426
 },
 {
   "ilce": "Kozaklı",
   "il": "Nevşehir",
   "FIELD3": 14.358
 },
 {
   "ilce": "Acıgöl",
   "il": "Nevşehir",
   "FIELD3": 19.399
 },
 {
   "ilce": "Derinkuyu",
   "il": "Nevşehir",
   "FIELD3": 21.432
 },
 {
   "ilce": "Gülşehir",
   "il": "Nevşehir",
   "FIELD3": 22.558
 },
 {
   "ilce": "Avanos",
   "il": "Nevşehir",
   "FIELD3": 33.875
 },
 {
   "ilce": "Ürgüp",
   "il": "Nevşehir",
   "FIELD3": 35.311
 },
 {
   "ilce": "Nevşehir",
   "il": "Nevşehir",
   "FIELD3": 127.891
 },
 {
   "ilce": "Altunhisar",
   "il": "Niğde",
   "FIELD3": 13.706
 },
 {
   "ilce": "Çamardı",
   "il": "Niğde",
   "FIELD3": 13.944
 },
 {
   "ilce": "Ulukışla",
   "il": "Niğde",
   "FIELD3": 20.842
 },
 {
   "ilce": "Çiftlik",
   "il": "Niğde",
   "FIELD3": 28.265
 },
 {
   "ilce": "Bor",
   "il": "Niğde",
   "FIELD3": 61.388
 },
 {
   "ilce": "Niğde",
   "il": "Niğde",
   "FIELD3": 205.753
 },
 {
   "ilce": "Kabadüz",
   "il": "Ordu",
   "FIELD3": 8.025
 },
 {
   "ilce": "Gülyalı",
   "il": "Ordu",
   "FIELD3": 8.384
 },
 {
   "ilce": "Çamaş",
   "il": "Ordu",
   "FIELD3": 9.07
 },
 {
   "ilce": "Kabataş",
   "il": "Ordu",
   "FIELD3": 10.923
 },
 {
   "ilce": "Çaybaşı",
   "il": "Ordu",
   "FIELD3": 13.643
 },
 {
   "ilce": "Çatalpınar",
   "il": "Ordu",
   "FIELD3": 14.168
 },
 {
   "ilce": "Gürgentepe",
   "il": "Ordu",
   "FIELD3": 14.314
 },
 {
   "ilce": "İkizce",
   "il": "Ordu",
   "FIELD3": 15.225
 },
 {
   "ilce": "Mesudiye",
   "il": "Ordu",
   "FIELD3": 16.576
 },
 {
   "ilce": "Ulubey",
   "il": "Ordu",
   "FIELD3": 19.903
 },
 {
   "ilce": "Aybastı",
   "il": "Ordu",
   "FIELD3": 23.049
 },
 {
   "ilce": "Akkuş",
   "il": "Ordu",
   "FIELD3": 24.634
 },
 {
   "ilce": "Gölköy",
   "il": "Ordu",
   "FIELD3": 29.959
 },
 {
   "ilce": "Korgan",
   "il": "Ordu",
   "FIELD3": 30.392
 },
 {
   "ilce": "Kumru",
   "il": "Ordu",
   "FIELD3": 31.209
 },
 {
   "ilce": "Perşembe",
   "il": "Ordu",
   "FIELD3": 31.702
 },
 {
   "ilce": "Fatsa",
   "il": "Ordu",
   "FIELD3": 108.365
 },
 {
   "ilce": "Ünye",
   "il": "Ordu",
   "FIELD3": 118.91
 },
 {
   "ilce": "Altınordu",
   "il": "Ordu",
   "FIELD3": 195.817
 },
 {
   "ilce": "Hasanbeyli",
   "il": "Osmaniye",
   "FIELD3": 4.623
 },
 {
   "ilce": "Sumbas",
   "il": "Osmaniye",
   "FIELD3": 14.841
 },
 {
   "ilce": "Toprakkale",
   "il": "Osmaniye",
   "FIELD3": 17.688
 },
 {
   "ilce": "Bahçe",
   "il": "Osmaniye",
   "FIELD3": 21.042
 },
 {
   "ilce": "Düziçi",
   "il": "Osmaniye",
   "FIELD3": 80.43
 },
 {
   "ilce": "Kadirli",
   "il": "Osmaniye",
   "FIELD3": 119.047
 },
 {
   "ilce": "Osmaniye",
   "il": "Osmaniye",
   "FIELD3": 249.136
 },
 {
   "ilce": "Hemşin",
   "il": "Rize",
   "FIELD3": 2.183
 },
 {
   "ilce": "Çamlıhemşin",
   "il": "Rize",
   "FIELD3": 6.28
 },
 {
   "ilce": "İkizdere",
   "il": "Rize",
   "FIELD3": 6.511
 },
 {
   "ilce": "Derepazarı",
   "il": "Rize",
   "FIELD3": 7.806
 },
 {
   "ilce": "İyidere",
   "il": "Rize",
   "FIELD3": 8.679
 },
 {
   "ilce": "Kalkandere",
   "il": "Rize",
   "FIELD3": 12.517
 },
 {
   "ilce": "Güneysu",
   "il": "Rize",
   "FIELD3": 14.56
 },
 {
   "ilce": "Fındıklı",
   "il": "Rize",
   "FIELD3": 16.241
 },
 {
   "ilce": "Pazar",
   "il": "Rize",
   "FIELD3": 30.824
 },
 {
   "ilce": "Ardeşen",
   "il": "Rize",
   "FIELD3": 40.478
 },
 {
   "ilce": "Çayeli",
   "il": "Rize",
   "FIELD3": 42.45
 },
 {
   "ilce": "Rize",
   "il": "Rize",
   "FIELD3": 141.25
 },
 {
   "ilce": "Taraklı",
   "il": "Sakarya",
   "FIELD3": 6.993
 },
 {
   "ilce": "Karapürçek",
   "il": "Sakarya",
   "FIELD3": 12.373
 },
 {
   "ilce": "Söğütlü",
   "il": "Sakarya",
   "FIELD3": 13.988
 },
 {
   "ilce": "Kocaali",
   "il": "Sakarya",
   "FIELD3": 21.8
 },
 {
   "ilce": "Kaynarca",
   "il": "Sakarya",
   "FIELD3": 23.297
 },
 {
   "ilce": "Ferizli",
   "il": "Sakarya",
   "FIELD3": 24.944
 },
 {
   "ilce": "Pamukova",
   "il": "Sakarya",
   "FIELD3": 28.309
 },
 {
   "ilce": "Arifiye",
   "il": "Sakarya",
   "FIELD3": 39.024
 },
 {
   "ilce": "Sapanca",
   "il": "Sakarya",
   "FIELD3": 39.437
 },
 {
   "ilce": "Geyve",
   "il": "Sakarya",
   "FIELD3": 48.051
 },
 {
   "ilce": "Karasu",
   "il": "Sakarya",
   "FIELD3": 57.008
 },
 {
   "ilce": "Hendek",
   "il": "Sakarya",
   "FIELD3": 76.664
 },
 {
   "ilce": "Erenler",
   "il": "Sakarya",
   "FIELD3": 79.934
 },
 {
   "ilce": "Akyazı",
   "il": "Sakarya",
   "FIELD3": 84.865
 },
 {
   "ilce": "Serdivan",
   "il": "Sakarya",
   "FIELD3": 112.611
 },
 {
   "ilce": "Adapazarı",
   "il": "Sakarya",
   "FIELD3": 263.408
 },
 {
   "ilce": "Yakakent",
   "il": "Samsun",
   "FIELD3": 8.934
 },
 {
   "ilce": "Ladik",
   "il": "Samsun",
   "FIELD3": 16.979
 },
 {
   "ilce": "Asarcık",
   "il": "Samsun",
   "FIELD3": 17.448
 },
 {
   "ilce": "Salıpazarı",
   "il": "Samsun",
   "FIELD3": 19.167
 },
 {
   "ilce": "Kavak",
   "il": "Samsun",
   "FIELD3": 20.251
 },
 {
   "ilce": "Ayvacık",
   "il": "Samsun",
   "FIELD3": 21.344
 },
 {
   "ilce": "Ondokuzmayıs",
   "il": "Samsun",
   "FIELD3": 24.391
 },
 {
   "ilce": "Alaçam",
   "il": "Samsun",
   "FIELD3": 27.238
 },
 {
   "ilce": "Havza",
   "il": "Samsun",
   "FIELD3": 41.959
 },
 {
   "ilce": "Tekkeköy",
   "il": "Samsun",
   "FIELD3": 49.579
 },
 {
   "ilce": "Terme",
   "il": "Samsun",
   "FIELD3": 72.599
 },
 {
   "ilce": "Canik",
   "il": "Samsun",
   "FIELD3": 95.56
 },
 {
   "ilce": "Vezirköprü",
   "il": "Samsun",
   "FIELD3": 99.904
 },
 {
   "ilce": "Çarşamba",
   "il": "Samsun",
   "FIELD3": 136.964
 },
 {
   "ilce": "Bafra",
   "il": "Samsun",
   "FIELD3": 142.556
 },
 {
   "ilce": "Atakum",
   "il": "Samsun",
   "FIELD3": 158.031
 },
 {
   "ilce": "İlkadım",
   "il": "Samsun",
   "FIELD3": 317.085
 },
 {
   "ilce": "Tillo",
   "il": "Siirt",
   "FIELD3": 4.129
 },
 {
   "ilce": "Eruh",
   "il": "Siirt",
   "FIELD3": 19.903
 },
 {
   "ilce": "Şirvan",
   "il": "Siirt",
   "FIELD3": 23.986
 },
 {
   "ilce": "Baykan",
   "il": "Siirt",
   "FIELD3": 27.323
 },
 {
   "ilce": "Pervari",
   "il": "Siirt",
   "FIELD3": 32.453
 },
 {
   "ilce": "Kurtalan",
   "il": "Siirt",
   "FIELD3": 58.033
 },
 {
   "ilce": "Siirt",
   "il": "Siirt",
   "FIELD3": 152.539
 },
 {
   "ilce": "Saraydüzü",
   "il": "Sinop",
   "FIELD3": 5.132
 },
 {
   "ilce": "Dikmen",
   "il": "Sinop",
   "FIELD3": 5.613
 },
 {
   "ilce": "Erfelek",
   "il": "Sinop",
   "FIELD3": 11.244
 },
 {
   "ilce": "Türkeli",
   "il": "Sinop",
   "FIELD3": 14.236
 },
 {
   "ilce": "Durağan",
   "il": "Sinop",
   "FIELD3": 19.495
 },
 {
   "ilce": "Gerze",
   "il": "Sinop",
   "FIELD3": 22.327
 },
 {
   "ilce": "Ayancık",
   "il": "Sinop",
   "FIELD3": 23.047
 },
 {
   "ilce": "Boyabat",
   "il": "Sinop",
   "FIELD3": 43.861
 },
 {
   "ilce": "Sinop",
   "il": "Sinop",
   "FIELD3": 59.571
 },
 {
   "ilce": "Doğanşar",
   "il": "Sivas",
   "FIELD3": 3.014
 },
 {
   "ilce": "Gölova",
   "il": "Sivas",
   "FIELD3": 3.261
 },
 {
   "ilce": "Akıncılar",
   "il": "Sivas",
   "FIELD3": 5.537
 },
 {
   "ilce": "İmranlı",
   "il": "Sivas",
   "FIELD3": 7.989
 },
 {
   "ilce": "Ulaş",
   "il": "Sivas",
   "FIELD3": 9.229
 },
 {
   "ilce": "Altınyayla",
   "il": "Sivas",
   "FIELD3": 9.566
 },
 {
   "ilce": "Hafik",
   "il": "Sivas",
   "FIELD3": 9.624
 },
 {
   "ilce": "Koyulhisar",
   "il": "Sivas",
   "FIELD3": 13.14
 },
 {
   "ilce": "Divriği",
   "il": "Sivas",
   "FIELD3": 16.829
 },
 {
   "ilce": "Gürün",
   "il": "Sivas",
   "FIELD3": 19.843
 },
 {
   "ilce": "Kangal",
   "il": "Sivas",
   "FIELD3": 22.768
 },
 {
   "ilce": "Zara",
   "il": "Sivas",
   "FIELD3": 22.887
 },
 {
   "ilce": "Gemerek",
   "il": "Sivas",
   "FIELD3": 24.517
 },
 {
   "ilce": "Suşehri",
   "il": "Sivas",
   "FIELD3": 26.091
 },
 {
   "ilce": "Şarkışla",
   "il": "Sivas",
   "FIELD3": 38.655
 },
 {
   "ilce": "Yıldızeli",
   "il": "Sivas",
   "FIELD3": 38.735
 },
 {
   "ilce": "Sivas",
   "il": "Sivas",
   "FIELD3": 351.431
 },
 {
   "ilce": "Marmaraereğlisi",
   "il": "Tekirdağ",
   "FIELD3": 23.476
 },
 {
   "ilce": "Muratlı",
   "il": "Tekirdağ",
   "FIELD3": 26.821
 },
 {
   "ilce": "Şarköy",
   "il": "Tekirdağ",
   "FIELD3": 31.524
 },
 {
   "ilce": "Hayrabolu",
   "il": "Tekirdağ",
   "FIELD3": 33.488
 },
 {
   "ilce": "Saray",
   "il": "Tekirdağ",
   "FIELD3": 47.522
 },
 {
   "ilce": "Malkara",
   "il": "Tekirdağ",
   "FIELD3": 53.014
 },
 {
   "ilce": "Ergene",
   "il": "Tekirdağ",
   "FIELD3": 57.613
 },
 {
   "ilce": "Kapaklı",
   "il": "Tekirdağ",
   "FIELD3": 92.003
 },
 {
   "ilce": "Çerkezköy",
   "il": "Tekirdağ",
   "FIELD3": 123.119
 },
 {
   "ilce": "Süleymanpaşa",
   "il": "Tekirdağ",
   "FIELD3": 182.522
 },
 {
   "ilce": "Çorlu",
   "il": "Tekirdağ",
   "FIELD3": 235.63
 },
 {
   "ilce": "Sulusaray",
   "il": "Tokat",
   "FIELD3": 7.835
 },
 {
   "ilce": "Artova",
   "il": "Tokat",
   "FIELD3": 9.106
 },
 {
   "ilce": "Başçiftlik",
   "il": "Tokat",
   "FIELD3": 9.399
 },
 {
   "ilce": "Yeşilyurt",
   "il": "Tokat",
   "FIELD3": 10.291
 },
 {
   "ilce": "Pazar",
   "il": "Tokat",
   "FIELD3": 14.117
 },
 {
   "ilce": "Almus",
   "il": "Tokat",
   "FIELD3": 26.589
 },
 {
   "ilce": "Reşadiye",
   "il": "Tokat",
   "FIELD3": 38.87
 },
 {
   "ilce": "Zile",
   "il": "Tokat",
   "FIELD3": 58.147
 },
 {
   "ilce": "Niksar",
   "il": "Tokat",
   "FIELD3": 64.254
 },
 {
   "ilce": "Turhal",
   "il": "Tokat",
   "FIELD3": 81.813
 },
 {
   "ilce": "Erbaa",
   "il": "Tokat",
   "FIELD3": 91.873
 },
 {
   "ilce": "Tokat",
   "il": "Tokat",
   "FIELD3": 185.626
 },
 {
   "ilce": "Dernekpazarı",
   "il": "Trabzon",
   "FIELD3": 3.803
 },
 {
   "ilce": "Köprübaşı",
   "il": "Trabzon",
   "FIELD3": 4.94
 },
 {
   "ilce": "Hayrat",
   "il": "Trabzon",
   "FIELD3": 7.631
 },
 {
   "ilce": "Şalpazarı",
   "il": "Trabzon",
   "FIELD3": 10.903
 },
 {
   "ilce": "Çaykara",
   "il": "Trabzon",
   "FIELD3": 13.854
 },
 {
   "ilce": "Düzköy",
   "il": "Trabzon",
   "FIELD3": 14.527
 },
 {
   "ilce": "Tonya",
   "il": "Trabzon",
   "FIELD3": 15.217
 },
 {
   "ilce": "Çarşıbaşı",
   "il": "Trabzon",
   "FIELD3": 15.596
 },
 {
   "ilce": "Beşikdüzü",
   "il": "Trabzon",
   "FIELD3": 21.87
 },
 {
   "ilce": "Maçka",
   "il": "Trabzon",
   "FIELD3": 24.232
 },
 {
   "ilce": "Sürmene",
   "il": "Trabzon",
   "FIELD3": 26.421
 },
 {
   "ilce": "Vakfıkebir",
   "il": "Trabzon",
   "FIELD3": 26.636
 },
 {
   "ilce": "Arsin",
   "il": "Trabzon",
   "FIELD3": 28.208
 },
 {
   "ilce": "Yomra",
   "il": "Trabzon",
   "FIELD3": 32.394
 },
 {
   "ilce": "Of",
   "il": "Trabzon",
   "FIELD3": 42.405
 },
 {
   "ilce": "Araklı",
   "il": "Trabzon",
   "FIELD3": 47.96
 },
 {
   "ilce": "Akçaabat",
   "il": "Trabzon",
   "FIELD3": 115.939
 },
 {
   "ilce": "Ortahisar",
   "il": "Trabzon",
   "FIELD3": 314.246
 },
 {
   "ilce": "Nazımiye",
   "il": "Tunceli",
   "FIELD3": 3.369
 },
 {
   "ilce": "Pülümür",
   "il": "Tunceli",
   "FIELD3": 3.528
 },
 {
   "ilce": "Ovacık",
   "il": "Tunceli",
   "FIELD3": 6.335
 },
 {
   "ilce": "Hozat",
   "il": "Tunceli",
   "FIELD3": 7.189
 },
 {
   "ilce": "Çemişgezek",
   "il": "Tunceli",
   "FIELD3": 8.149
 },
 {
   "ilce": "Mazgirt",
   "il": "Tunceli",
   "FIELD3": 8.243
 },
 {
   "ilce": "Pertek",
   "il": "Tunceli",
   "FIELD3": 11.699
 },
 {
   "ilce": "Tunceli",
   "il": "Tunceli",
   "FIELD3": 38.015
 },
 {
   "ilce": "Karahallı",
   "il": "Uşak",
   "FIELD3": 10.769
 },
 {
   "ilce": "Ulubey",
   "il": "Uşak",
   "FIELD3": 13.647
 },
 {
   "ilce": "Sivaslı",
   "il": "Uşak",
   "FIELD3": 21.122
 },
 {
   "ilce": "Eşme",
   "il": "Uşak",
   "FIELD3": 35.749
 },
 {
   "ilce": "Banaz",
   "il": "Uşak",
   "FIELD3": 36.609
 },
 {
   "ilce": "Uşak",
   "il": "Uşak",
   "FIELD3": 231.563
 },
 {
   "ilce": "Bahçesaray",
   "il": "Van",
   "FIELD3": 16.016
 },
 {
   "ilce": "Çatak",
   "il": "Van",
   "FIELD3": 22.465
 },
 {
   "ilce": "Saray",
   "il": "Van",
   "FIELD3": 22.682
 },
 {
   "ilce": "Gevaş",
   "il": "Van",
   "FIELD3": 28.982
 },
 {
   "ilce": "Gürpınar",
   "il": "Van",
   "FIELD3": 37.256
 },
 {
   "ilce": "Muradiye",
   "il": "Van",
   "FIELD3": 51.165
 },
 {
   "ilce": "Başkale",
   "il": "Van",
   "FIELD3": 57.408
 },
 {
   "ilce": "Çaldıran",
   "il": "Van",
   "FIELD3": 66.679
 },
 {
   "ilce": "Özalp",
   "il": "Van",
   "FIELD3": 71.265
 },
 {
   "ilce": "Edremit",
   "il": "Van",
   "FIELD3": 113.999
 },
 {
   "ilce": "Tuşba",
   "il": "Van",
   "FIELD3": 145.142
 },
 {
   "ilce": "Erciş",
   "il": "Van",
   "FIELD3": 172.823
 },
 {
   "ilce": "İpekyolu",
   "il": "Van",
   "FIELD3": 279.66
 },
 {
   "ilce": "Termal",
   "il": "Yalova",
   "FIELD3": 5.934
 },
 {
   "ilce": "Armutlu",
   "il": "Yalova",
   "FIELD3": 8.619
 },
 {
   "ilce": "Altınova",
   "il": "Yalova",
   "FIELD3": 24.333
 },
 {
   "ilce": "Çınarcık",
   "il": "Yalova",
   "FIELD3": 27.535
 },
 {
   "ilce": "Çiftlikköy",
   "il": "Yalova",
   "FIELD3": 32.423
 },
 {
   "ilce": "Yalova",
   "il": "Yalova",
   "FIELD3": 127.67
 },
 {
   "ilce": "Çandır",
   "il": "Yozgat",
   "FIELD3": 4.693
 },
 {
   "ilce": "Yenifakılı",
   "il": "Yozgat",
   "FIELD3": 5.724
 },
 {
   "ilce": "Aydıncık",
   "il": "Yozgat",
   "FIELD3": 10.936
 },
 {
   "ilce": "Kadışehri",
   "il": "Yozgat",
   "FIELD3": 13.397
 },
 {
   "ilce": "Saraykent",
   "il": "Yozgat",
   "FIELD3": 14.192
 },
 {
   "ilce": "Çayıralan",
   "il": "Yozgat",
   "FIELD3": 14.201
 },
 {
   "ilce": "Şefaatli",
   "il": "Yozgat",
   "FIELD3": 15.985
 },
 {
   "ilce": "Çekerek",
   "il": "Yozgat",
   "FIELD3": 22.729
 },
 {
   "ilce": "Boğazlıyan",
   "il": "Yozgat",
   "FIELD3": 34.193
 },
 {
   "ilce": "Sarıkaya",
   "il": "Yozgat",
   "FIELD3": 35.543
 },
 {
   "ilce": "Yerköy",
   "il": "Yozgat",
   "FIELD3": 37.247
 },
 {
   "ilce": "Akdağmadeni",
   "il": "Yozgat",
   "FIELD3": 47.309
 },
 {
   "ilce": "Sorgun",
   "il": "Yozgat",
   "FIELD3": 79.58
 },
 {
   "ilce": "Yozgat",
   "il": "Yozgat",
   "FIELD3": 96.831
 },
 {
   "ilce": "Gökçebey",
   "il": "Zonguldak",
   "FIELD3": 21.978
 },
 {
   "ilce": "Kilimli",
   "il": "Zonguldak",
   "FIELD3": 39.098
 },
 {
   "ilce": "Kozlu",
   "il": "Zonguldak",
   "FIELD3": 44.141
 },
 {
   "ilce": "Alaplı",
   "il": "Zonguldak",
   "FIELD3": 44.47
 },
 {
   "ilce": "Devrek",
   "il": "Zonguldak",
   "FIELD3": 55.889
 },
 {
   "ilce": "Çaycuma",
   "il": "Zonguldak",
   "FIELD3": 92.205
 },
 {
   "ilce": "Zonguldak",
   "il": "Zonguldak",
   "FIELD3": 126.864
 },
 {
   "ilce": "Ereğli",
   "il": "Zonguldak",
   "FIELD3": 174.151
 },
 {
   "ilce": "Bozcaada",
   "il": "Çanakkale",
   "FIELD3": 2.754
 },
 {
   "ilce": "Gökçeada",
   "il": "Çanakkale",
   "FIELD3": 8.644
 },
 {
   "ilce": "Eceabat",
   "il": "Çanakkale",
   "FIELD3": 9.151
 },
 {
   "ilce": "Lapseki",
   "il": "Çanakkale",
   "FIELD3": 25.987
 },
 {
   "ilce": "Bayramiç",
   "il": "Çanakkale",
   "FIELD3": 29.87
 },
 {
   "ilce": "Ayvacık",
   "il": "Çanakkale",
   "FIELD3": 32.187
 },
 {
   "ilce": "Ezine",
   "il": "Çanakkale",
   "FIELD3": 32.962
 },
 {
   "ilce": "Yenice",
   "il": "Çanakkale",
   "FIELD3": 33.945
 },
 {
   "ilce": "Gelibolu",
   "il": "Çanakkale",
   "FIELD3": 44.851
 },
 {
   "ilce": "Çan",
   "il": "Çanakkale",
   "FIELD3": 49.299
 },
 {
   "ilce": "Biga",
   "il": "Çanakkale",
   "FIELD3": 86.483
 },
 {
   "ilce": "Çanakkale",
   "il": "Çanakkale",
   "FIELD3": 155.657
 },
 {
   "ilce": "Bayramören",
   "il": "Çankırı",
   "FIELD3": 2.546
 },
 {
   "ilce": "Korgun",
   "il": "Çankırı",
   "FIELD3": 4.215
 },
 {
   "ilce": "Eldivan",
   "il": "Çankırı",
   "FIELD3": 5.561
 },
 {
   "ilce": "Atkaracalar",
   "il": "Çankırı",
   "FIELD3": 5.702
 },
 {
   "ilce": "Kızılırmak",
   "il": "Çankırı",
   "FIELD3": 7.523
 },
 {
   "ilce": "Yapraklı",
   "il": "Çankırı",
   "FIELD3": 8.244
 },
 {
   "ilce": "Kurşunlu",
   "il": "Çankırı",
   "FIELD3": 8.251
 },
 {
   "ilce": "Şabanözü",
   "il": "Çankırı",
   "FIELD3": 10.339
 },
 {
   "ilce": "Orta",
   "il": "Çankırı",
   "FIELD3": 12.776
 },
 {
   "ilce": "Ilgaz",
   "il": "Çankırı",
   "FIELD3": 14.428
 },
 {
   "ilce": "Çerkeş",
   "il": "Çankırı",
   "FIELD3": 17.584
 },
 {
   "ilce": "Çankırı",
   "il": "Çankırı",
   "FIELD3": 86.381
 },
 {
   "ilce": "Boğazkale",
   "il": "Çorum",
   "FIELD3": 4.064
 },
 {
   "ilce": "Laçin",
   "il": "Çorum",
   "FIELD3": 5.08
 },
 {
   "ilce": "Oğuzlar",
   "il": "Çorum",
   "FIELD3": 6.048
 },
 {
   "ilce": "Dodurga",
   "il": "Çorum",
   "FIELD3": 6.409
 },
 {
   "ilce": "Uğurludağ",
   "il": "Çorum",
   "FIELD3": 6.89
 },
 {
   "ilce": "Ortaköy",
   "il": "Çorum",
   "FIELD3": 8.155
 },
 {
   "ilce": "Kargı",
   "il": "Çorum",
   "FIELD3": 15.801
 },
 {
   "ilce": "Mecitözü",
   "il": "Çorum",
   "FIELD3": 16.233
 },
 {
   "ilce": "Bayat",
   "il": "Çorum",
   "FIELD3": 18.616
 },
 {
   "ilce": "Alaca",
   "il": "Çorum",
   "FIELD3": 33.468
 },
 {
   "ilce": "İskilip",
   "il": "Çorum",
   "FIELD3": 34.951
 },
 {
   "ilce": "Osmancık",
   "il": "Çorum",
   "FIELD3": 43.92
 },
 {
   "ilce": "Sungurlu",
   "il": "Çorum",
   "FIELD3": 51.975
 },
 {
   "ilce": "Çorum",
   "il": "Çorum",
   "FIELD3": 275.61
 },
 {
   "ilce": "Halfeti",
   "il": "Şanlıurfa",
   "FIELD3": 38.345
 },
 {
   "ilce": "Hilvan",
   "il": "Şanlıurfa",
   "FIELD3": 41.657
 },
 {
   "ilce": "Bozova",
   "il": "Şanlıurfa",
   "FIELD3": 55.631
 },
 {
   "ilce": "Harran",
   "il": "Şanlıurfa",
   "FIELD3": 78.681
 },
 {
   "ilce": "Ceylanpınar",
   "il": "Şanlıurfa",
   "FIELD3": 80.706
 },
 {
   "ilce": "Birecik",
   "il": "Şanlıurfa",
   "FIELD3": 92.355
 },
 {
   "ilce": "Akçakale",
   "il": "Şanlıurfa",
   "FIELD3": 98.897
 },
 {
   "ilce": "Suruç",
   "il": "Şanlıurfa",
   "FIELD3": 102.164
 },
 {
   "ilce": "Karaköprü",
   "il": "Şanlıurfa",
   "FIELD3": 115.733
 },
 {
   "ilce": "Viranşehir",
   "il": "Şanlıurfa",
   "FIELD3": 181.072
 },
 {
   "ilce": "Siverek",
   "il": "Şanlıurfa",
   "FIELD3": 238.979
 },
 {
   "ilce": "Haliliye",
   "il": "Şanlıurfa",
   "FIELD3": 357.504
 },
 {
   "ilce": "Eyyübiye",
   "il": "Şanlıurfa",
   "FIELD3": 363.943
 },
 {
   "ilce": "Güçlükonak",
   "il": "Şırnak",
   "FIELD3": 12.023
 },
 {
   "ilce": "Beytüşşebap",
   "il": "Şırnak",
   "FIELD3": 16.961
 },
 {
   "ilce": "Uludere",
   "il": "Şırnak",
   "FIELD3": 41.094
 },
 {
   "ilce": "İdil",
   "il": "Şırnak",
   "FIELD3": 73.348
 },
 {
   "ilce": "Şırnak",
   "il": "Şırnak",
   "FIELD3": 91.573
 },
 {
   "ilce": "Silopi",
   "il": "Şırnak",
   "FIELD3": 121.11
 },
 {
   "ilce": "Cizre",
   "il": "Şırnak",
   "FIELD3": 132.857
 }
]

# upper ve lower islemi turkce icin duzgun calismiyor bu harflerde.
# kendimiz elle karsiliklarini vermemiz gerekiyor.
upper_map = {
    ord(u'i'): u'İ',
    ord(u'ı'): u'I',
}

for index, d in enumerate(data):
    del d['FIELD3'] # baska bi yerden bulmustum. nufus bilgisi bu. gerek yok.
    d['ilce_id'] = index + 1
    for il in iller:
        if il['il'] == d['il'].translate(upper_map).upper():
            d['il_id'] = il['plaka']
            d['bolge'] = il['bolge']
            d['bolge_id'] = bolgeler[il['bolge']]


with open('data.json', 'w') as outfile:
    json.dump(data, outfile, ensure_ascii=False)
