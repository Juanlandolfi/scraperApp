from .base_extractor import BaseExtractor
from .utils import parse_price

class KilbelExtractor(BaseExtractor):
    SITE_NAME = "Kilbel"

    async def extract(self, page):
        title = await self.get_text(page, ".titulo_producto")
        price_actual = await self.get_text(page, ".precio.aux1")
        internal_code = await self.get_text(page, ".der.precio")
        price_regular = await self.get_text(page, ".precio.anterior") 

        #convert numbers
        price_actual = parse_price(price_actual)
        price_regular = parse_price(price_regular)
        
        return {
            "site": self.SITE_NAME,
            "product_name_store": title,
            "price_actual": price_actual,
            "price_regular": price_regular or price_actual,
            "store_product_code": internal_code,
            "in_offert": price_regular is not None,
                        
        }