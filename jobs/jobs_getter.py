from repositories.products_repository import ProductsRepository
from typing import Dict, List


repo = ProductsRepository()

def load_jobs() -> Dict[str, List[dict]]:
    rows = repo.get_active_products()

    jobs = {}

    for record_id, store_id, product_id, sku, url in rows:
        # You can map store_id → site identifier
        site = str(store_id)

        if site not in jobs:
            jobs[site] = []

        jobs[site].append({
            "url": url,
            "product_id": product_id,
            "sku": sku,
            "store_id": store_id,
            "record_id": record_id,
        })

    return jobs


def site_mapper(site_id: str) -> str:
    # TODO REPLACE DICTIONARY LOGIC WITH TABLE IN DATABASE. CREATE COMPANIES REPOSITORY.
    sites = {
        '1': 'Kilbel'
    }

    return sites.get(site_id, 'Unkown')

