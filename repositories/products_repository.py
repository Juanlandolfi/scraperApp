from .base_repository import BaseRepository

class ProductsRepository(BaseRepository):

    def get_active_products(self):
        sql = """
            SELECT record_id, store_id, product_id, sku, url
            FROM products_on_watch
            WHERE is_active = TRUE
        """
        return self.fetch_all(sql)
