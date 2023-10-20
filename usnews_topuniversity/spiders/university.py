import scrapy
import jmespath


class UniversitySpider(scrapy.Spider):
    name = "university"
    allowed_domains = ["usnews.com"]

    def start_requests(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        }
        self.start = True
        self.url = "https://www.usnews.com/education/best-global-universities/search?format=json&page="
        url = self.url + str(1)
        yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        # extract data
        data = response.json()
        # collect the university information using jmespath
        items = data.get("items", [])
        for item in items:
            yield dict(
                name=jmespath.search("name", item),
                city=jmespath.search("city", item),
                country=jmespath.search("country_name", item),
                ranks=jmespath.search("ranks[0].value", item),
                score=jmespath.search("stats[0].value", item),
                url=jmespath.search("url", item),
            )
        # iterate trough it, start from 2
        if self.start:
            self.start = False
            max_page = data["total_pages"] + 1
            for i in range(2, max_page):
                url = self.url + str(i)
                yield scrapy.Request(url, headers=self.headers, callback=self.parse)
