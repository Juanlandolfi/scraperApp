import asyncio
from core.browser import BrowserManager
from core.downloader import Downloader
from extractors.factory import get_extractor
from pipelines.supabase_pipeline import SupabasePipeline
from jobs.product_jobs import JOBS
from jobs.jobs_getter import load_jobs, site_mapper
async def main():

    JOBS = load_jobs()

    pipeline = SupabasePipeline() 

    async with BrowserManager() as context:
        downloader = Downloader(context)

        for site_id, jobs in JOBS.items():
            site = site_mapper(site_id)
            extractor = get_extractor(site)
            for job in jobs:
                url = job.get('url')
                data = await extractor.fetch_product(downloader, url)
                data.update({'url': url, 
                             'product_id': job.get('product_id'),
                             "record": job.get('record_id')
                             })
                print(data)

                await pipeline.process_item(data)
        

asyncio.run(main())
