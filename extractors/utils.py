import re 

def parse_price(price: str | None) -> float:
    if price is None: return None
    match = re.search(r"\$\s*([\d\.,]+)", price)
    if not match:
        return None
    price = match.group(1)
    return float(price.replace(".", "").replace(",", "."))