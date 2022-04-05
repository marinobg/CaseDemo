import re

def convert_price_to_clean(price: str) -> str:
    """
    Removes special characters from a price value represented in USD.
    Input: Price as a string with special characters
    Output: Price as a string without special characters such as $ and ,
    """
    return re.sub(r"[\$,]", "", price)