from scrapy.spiders import XMLFeedSpider


class XmlfeedSpider(XMLFeedSpider):
    name = 'xmlfeed'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/feed.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        item = {}
        #item['url'] = selector.select('url').get()
        #item['name'] = selector.select('name').get()
        #item['description'] = selector.select('description').get()
        return item
