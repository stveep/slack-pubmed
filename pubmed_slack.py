import pubmed
from urllib2 import Request, urlopen
import os
search_terms = ["Breast cancer"]

slack_webhook = os.environ.get("SLACK_WEBHOOK_URL")
max_results = 1

for term in search_terms:
    search = pubmed.SearchResult(term)
    for record in search.records()[0:max_results]:
        print record.slack_payload()
        request = Request(slack_webhook, record.slack_payload())
        urlopen(request).read().decode()
