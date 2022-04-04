import re

def convert_price_to_clean(price: str) -> str:
    return re.sub(r"[\$,]", "", price)