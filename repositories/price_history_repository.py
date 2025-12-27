from .base_repository import BaseRepository

class PriceHistoryRepository(BaseRepository):

    def save_price(self, item: dict):
        sql = """INSERT INTO product_price_history
                (
                product_name_store
                ,price_actual
                ,price_regular
                ,in_offert
                ,url
                ,store_product_code
                ,product_id
                ,fired_by_watch
                ,price_promotion
                 )
            VALUES (%s, %s, %s, 
                    %s, %s, %s, 
                    %s, %s, %s)
        """

        params = (
            item.get("product_name_store"),
            item.get("price_actual"),
            item.get("price_regular"),
            item.get("in_offert"),
            item.get("url"),
            item.get("store_product_code"),
            item.get("product_id"),
            item.get("record"),
            item.get("price_promotion")

        )

        self.execute(sql, params)
