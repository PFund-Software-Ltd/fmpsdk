import typing

from .url_methods import __return_json_v3, __return_json_v4


def historical_social_sentiment(apikey: str, symbol: str) -> list[dict]:
    """
    Query FMP /historical/social-sentiment API

    :param apikey: Your API key.
    :param symbol: Ticker of company.
    :return: A list of dictionaries.
    """
    path = f"historical/social-sentiment"
    query_vars = {"apikey": apikey, 'symbol': symbol}
    return __return_json_v4(path=path, query_vars=query_vars)


def stock_grade(apikey: str, symbol: str, limit: int = 500) -> list[dict]:
    """
    Query FMP /grade API

    :param apikey: Your API key.
    :param symbol: Ticker of company.
    :return: A list of dictionaries.
    """
    path = f"grade/{symbol}"
    query_vars = {"apikey": apikey, 'limit': limit}
    return __return_json_v3(path=path, query_vars=query_vars)


def earnings_surprises(
    apikey: str, symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /earnings-surprises/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"earnings-surprises/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)