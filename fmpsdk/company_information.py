from .url_methods import __return_json_v4


def symbol_change(apikey: str) -> list[dict]:
    """
    Query FMP /symbol_change API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol_change"
    query_vars = {"apikey": apikey}
    return __return_json_v4(path=path, query_vars=query_vars)

