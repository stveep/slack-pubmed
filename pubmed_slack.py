import pubmed
from urllib2 import Request, urlopen
search_terms = ["PARP1", "synthetic lethality"]
slack_webhook = "https://hooks.slack.com/services/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"

for term in search_terms:
    search = pubmed.SearchResult(term)
    for record in search.records():
        print record.slack_payload()
        request = Request(slack_webhook, record.slack_payload())
        # urlopen(request).read().decode()
