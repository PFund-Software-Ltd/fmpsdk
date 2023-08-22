import typing

from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __return_json_v4



def price_target(apikey: str, symbol: str) -> list[dict]:
    """
    Query FMP /price-target API

    :param apikey: Your API key.
    :param symbol: Ticker of company.
    :return: A list of dictionaries.
    """
    path = f"price-target"
    query_vars = {"apikey": apikey, 'symbol': symbol}
    return __return_json_v4(path=path, query_vars=query_vars)


def price_target_summary(apikey: str, symbol: str) -> list[dict]:
    """
    Query FMP /price-target-summary API

    :param apikey: Your API key.
    :param symbol: Ticker of company.
    :return: A list of dictionaries.
    """
    path = f"price-target-summary"
    query_vars = {"apikey": apikey, 'symbol': symbol}
    return __return_json_v4(path=path, query_vars=query_vars)


def price_target_consensus(apikey: str, symbol: str) -> list[dict]:
    """
    Query FMP /price-target-consensus API

    :param apikey: Your API key.
    :param symbol: Ticker of company.
    :return: A list of dictionaries.
    """
    path = f"price-target-consensus"
    query_vars = {"apikey": apikey, 'symbol': symbol}
    return __return_json_v4(path=path, query_vars=query_vars)
