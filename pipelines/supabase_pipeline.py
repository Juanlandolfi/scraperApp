from database.db_connection import get_db
from pipelines.base_pipeline import BasePipeline
from repositories.price_history_repository import PriceHistoryRepository


class SupabasePipeline(BasePipeline):

    def __init__(self):
        self.repo = PriceHistoryRepository()

    
    async def process_item(self, item: dict):
        self.repo.save_price(item)
       