import pubmed

import unittest
def setup_with_results():
    sr = pubmed.SearchResult("stuff")
    sr.result = {'esearchresult': {'idlist': ['11111','22222','33333']}}
    return sr

class TestSearchResult(unittest.TestCase):
    def test_init(self):
        """When given a term, it is added as a property"""
        sr = pubmed.SearchResult("stuff")
        self.assertEqual(sr.term,"stuff")
        self.assertEqual(sr.result,"")

    def test_records(self):
        """Returns appropriate record objects from result IDs"""
        sr = setup_with_results()
        self.assertEqual(sr.records()[0].__class__, pubmed.Record )
        self.assertEqual(sr.records()[0].id,'11111')
        self.assertEqual(len(sr.records()),3)

def setup_record_with_result():
    sr = pubmed.Record("1234")
    sr.result = {    "uid": "27994596",    "pubdate": "2016 Dec 5",    "epubdate": "2016 Dec 5",    "source": "Front Immunol",    "authors": [        {            "name": "Li Y",            "authtype": "Author",            "clusterid": ""        },        {            "name": "Wu Y",            "authtype": "Author",            "clusterid": ""        },        {            "name": "Zheng X",            "authtype": "Author",            "clusterid": ""        },        {            "name": "Cong J",            "authtype": "Author",            "clusterid": ""        },        {            "name": "Liu Y",            "authtype": "Author",            "clusterid": ""        },        {            "name": "Li J",            "authtype": "Author",            "clusterid": ""        },        {            "name": "Sun R",            "authtype": "Author",            "clusterid": ""        },        {            "name": "Tian ZG",            "authtype": "Author",            "clusterid": ""        },        {            "name": "Wei HM",            "authtype": "Author",            "clusterid": ""        }    ],    "lastauthor": "Wei HM",    "title": "Cytoplasm-Translocated Ku70/80 Complex Sensing of HBV DNA Induces Hepatitis-Associated Chemokine Secretion.",    "sorttitle": "cytoplasm translocated ku70 80 complex sensing of hbv dna induces hepatitis associated chemokine secretion",    "volume": "7",    "issue": "",    "pages": "569",    "lang": [        "eng"    ],    "nlmuniqueid": "101560960",    "issn": "",    "essn": "1664-3224",    "pubtype": [        "Journal Article"    ],    "recordstatus": "PubMed",    "pubstatus": "3",    "articleids": [        {            "idtype": "pubmed",            "idtypen": 1,            "value": "27994596"        },        {            "idtype": "doi",            "idtypen": 3,            "value": "10.3389/fimmu.2016.00569"        },        {            "idtype": "pmc",            "idtypen": 8,            "value": "PMC5136554"        },        {            "idtype": "rid",            "idtypen": 8,            "value": "27994596"        },        {            "idtype": "eid",            "idtypen": 8,            "value": "27994596"        },        {            "idtype": "pmcid",            "idtypen": 5,            "value": "pmc-id: PMC5136554;"        }    ],    "history": [        {            "pubstatus": "received",            "date": "2016/07/14 00:00"        },        {            "pubstatus": "accepted",            "date": "2016/11/22 00:00"        },        {            "pubstatus": "entrez",            "date": "2016/12/21 06:00"        },        {            "pubstatus": "pubmed",            "date": "2016/12/21 06:00"        },        {            "pubstatus": "medline",            "date": "2016/12/21 06:01"        }    ],    "references": [    ],    "attributes": [        "Has Abstract"    ],    "pmcrefcount": "",    "fulljournalname": "Frontiers in immunology",    "elocationid": "",    "doctype": "citation",    "srccontriblist": [    ],    "booktitle": "",    "medium": "",    "edition": "",    "publisherlocation": "",    "publishername": "",    "srcdate": "",    "reportnumber": "",    "availablefromurl": "",    "locationlabel": "",    "doccontriblist": [    ],    "docdate": "",    "bookname": "",    "chapter": "",    "sortpubdate": "2016/12/05 00:00",    "sortfirstauthor": "Li Y",    "vernaculartitle": ""  }
    return sr

class TestRecord(unittest.TestCase):
    def test_init(self):
        """It sets the id property"""
        record = pubmed.Record("200")
        self.assertEqual(record.id,"200")

    def test_repeated_get(self):
        """It doesn't repeat the search if data is already there"""
        record = setup_record_with_result()
        record.result["uid"] = "9999"
        record.get()
        self.assertEqual(record.result["uid"],"9999")




if __name__ == "__main__":
    unittest.main()
