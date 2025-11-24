def parse_price(price: str | None) -> float:
    if price is None: return None
    return float(price.replace("$", "").replace(".","").replace(",",".").strip())