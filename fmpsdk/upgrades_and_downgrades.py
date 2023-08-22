from .url_methods import __return_json_v4


def upgrades_downgrades(apikey: str, symbol: str) -> list[dict]:
    """
    Query FMP /upgrades-downgrades API

    :param apikey: Your API key.
    :param symbol: Ticker of company.
    :return: A list of dictionaries.
    """
    path = f"upgrades-downgrades"
    query_vars = {"apikey": apikey, 'symbol': symbol}
    return __return_json_v4(path=path, query_vars=query_vars)


def upgrades_downgrades_consensus(apikey: str, symbol: str) -> list[dict]:
    """
    Query FMP /upgrades-downgrades-consensus API

    :param apikey: Your API key.
    :param symbol: Ticker of company.
    :return: A list of dictionaries.
    """
    path = f"upgrades-downgrades-consensus"
    query_vars = {"apikey": apikey, 'symbol': symbol}
    return __return_json_v4(path=path, query_vars=query_vars)