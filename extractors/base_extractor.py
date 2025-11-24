class BaseExtractor:
    SITE_NAME = None

    async def extract(self, page):
        raise NotImplementedError

    async def fetch_product(self, downloader, url):
        page = await downloader.get_page(url)
        return await self.extract(page)
    
    async def get_text(self, page, selector, default=None):
        try:
            loc = page.locator(selector)
            if await loc.count() == 0:
                return default
            text = await loc.inner_text()
            return text.strip() if text else default
        except:
            return default