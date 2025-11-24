from database.db_connection import get_db
from pipelines.base_pipeline import BasePipeline

class SupabasePipeline(BasePipeline):
    
    async def process_item(self, item: dict):
        with get_db() as cursor:
            cursor.execute(
                """
                 INSERT INTO product_price_history (product_name_store, price_actual, price_regular, in_offert,url, store_product_code)
                    VALUES ("%s, %s, %s, %s, %s, %s)
                """,
                (
                    item.get('product_name_store'),
                    item.get('price_actual'),
                    item.get('price_regular'),
                    item.get('in_offert'),
                    item.get('url'),
                    item.get('store_product_code')
                )

            )