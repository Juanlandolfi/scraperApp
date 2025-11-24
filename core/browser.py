from playwright.async_api import async_playwright

class BrowserManager:
    async def __aenter__(self):
        self.pw = await async_playwright().start()
        self.browser = await self.pw.chromium.launch(headless=True)
        self.context = await self.browser.new_context(
                                            user_agent=(
                                                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                                "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                                            ),
                                            locale="es-AR",
                                            timezone_id="America/Argentina/Buenos_Aires"
                                        )
        return self.context

    async def __aexit__(self, *args):
        await self.context.close()
        await self.browser.close()
        await self.pw.stop()