from .base_extractor import BaseExtractor
from .utils import parse_price
from typing import Any, Dict
from playwright.async_api import Page


class KilbelExtractor(BaseExtractor):
    SITE_NAME = "kilbel"

    async def extract(self, page: Page, rules: dict = None) -> Dict[str, Any]:
        '''Returns the Item to be loaded to database'''

        title = await self.get_text(page, ".titulo_producto")
        internal_code = await self.get_text(page, ".der.precio")
        price_actual = await self.get_text(page, ".precio.aux1")
        price_regular = await self.get_text(page, ".precio.anterior") 
        price_promotion = await self.get_text(page, ".precio.destacado") 

        #convert numbers
        price_actual = parse_price(price_actual)
        price_regular = parse_price(price_regular)
        price_promotion = parse_price(price_promotion)
        
        return {
            "site": self.SITE_NAME,
            "product_name_store": title,
            "price_actual": price_actual,
            "price_regular": price_regular or price_actual,
            "store_product_code": internal_code,
            "in_offert": price_regular is not None,
            "price_promotion": price_promotion
                        
        }