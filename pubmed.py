import urllib2
import urlparse
import json
import random

search_url_base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
pubmed_url_base = "https://www.ncbi.nlm.nih.gov/pubmed/"
summary_url_base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
username = "Search Result"
emojis = [
    ":hankey:",
    ":+1:",
    ":blue_heart:",
    ":sunny:",
    ":cat:",
    ":hamster:",
    ":rabbit:",
    ":dog:",
    ":mouse:",
    ":wolf:",
    ":musical_notes:",
    ":pig:",
    ":tulip:",
    ":maple_leaf:",
    ":sunflower:",
    ":mushroom:",
    ":octocat:",
    ":pizza:",
    ":cherries:",
    ":checkered_flag:",
    ":izakaya_lantern:",
    ":smiling_imp:",
    ":metal:",
    ":heart_eyes_cat:",
]

class Record:

    def __init__(self,id):
        self.id = str(id)
        self.result = ""

    def get(self):
        if not self.result:
            url = summary_url_base.rstrip("/") + "?db=pubmed&id=" + urllib2.quote(self.id) + "&retmode=json"
            request = urllib2.urlopen(url)
            result_json = request.read()
            self.result = json.loads(result_json)["result"][self.id]
        return self.result

    def title(self):
        self.get()
        return self.result["title"]

    def source(self):
        self.get()
        return self.result["source"]

    def to_url(self):
        return urlparse.urljoin(pubmed_url_base,self.id)

    def author_string(self):
        self.get()
        return self.result["sortfirstauthor"] + "..." + self.result["lastauthor"]

    def slack_payload(self):
        self.get()
        if self.title() and self.source():
            return json.dumps({ "attachments": [{"title": self.title(),
                                                "title_link": self.to_url(),
                                                "text": self.author_string(),
                                                "fields": [{"title": self.source()}]
                                                }],
                                "icon_emoji": random.choice(emojis),
                                "username": username
                                })

class SearchResult:

    def __init__(self, term):
        self.term = term
        self.result = ""

    def search(self):
        search_url = search_url_base.rstrip("/") + "?db=pubmed&term=" + urllib2.quote(self.term) + "&retmode=json"
        request = urllib2.urlopen(search_url)
        result_json = request.read()
        self.result = json.loads(result_json)
        return self.result

    def ids_from_result(self):
        if not self.result:
            self.search()
        id_list = self.result['esearchresult']['idlist']
        return id_list

    def to_url(self,id):
        return urlparse.urljoin(pubmed_url_base,id)

    def urls_from_result(self):
        id_list = self.ids_from_result()
        return [pubmed_url_base + a for a in id_list]

    def records(self):
        return [Record(elem) for elem in self.ids_from_result()]
