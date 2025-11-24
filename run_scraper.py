import asyncio
from core.browser import BrowserManager
from core.downloader import Downloader
from extractors.factory import get_extractor
from pipelines.supabase_pipeline import SupabasePipeline
from jobs.product_jobs import JOBS

async def main():

    pipeline = SupabasePipeline() 

    async with BrowserManager() as context:
        downloader = Downloader(context)

        for site, urls in JOBS.items():
            extractor = get_extractor(site)
            for url in urls:
                data = await extractor.fetch_product(downloader, url)
                data.update({'url': url})
                print(data)

                await pipeline.process_item(data)
        

asyncio.run(main())
