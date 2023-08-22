import typing

from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3


def most_active(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock_market/actives/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"stock_market/actives"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def most_gainer(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock_market/gainers/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"stock_market/gainers"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def most_loser(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock_market/losers/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"stock_market/losers"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def market_hours(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /market-hours/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"market-hours"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def sectors_performance(apikey: str, limit: int = DEFAULT_LIMIT) -> list[dict]:
    """
    Query FMP /sectors_performance/ API

    :param apikey: Your API key.
    :param limit: Number of rows to return
    :return: A list of dictionaries.
    """
    path = f"sectors-performance"
    query_vars = {"apikey": apikey, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_sectors_performance(apikey: str, limit: int = DEFAULT_LIMIT) -> list[dict]:
    """
    Query FMP /historical-sectors-performance/ API

    :param apikey: Your API key.
    :param limit: Number of rows to return
    :return: A list of dictionaries.
    """
    path = f"historical-sectors-performance"
    query_vars = {"apikey": apikey, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)
