class Downloader:
    def __init__(self, context):
        self.context = context

    async def get_page(self, url, retries=3):
        for _ in range(retries):
            try:
                page = await self.context.new_page()
                await page.goto(url, wait_until="domcontentloaded", timeout=25000)
                return page
            except Exception:
                continue
        raise Exception(f"Failed to load {url}")
