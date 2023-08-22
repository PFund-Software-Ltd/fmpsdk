import typing

from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __return_json_v4


def economic_indicator(apikey: str, name: str, from_date: str, to_date: str) -> list:
    """
    Query FMP /economic API

    :param apikey: Your API key.
    :param name: Indicator name.
    :param from_date (yyyy-mm-dd): Get historical data starting from this date.
    :param to_date (yyyy-mm-dd): Get historical data to this date.
    :return: A list.
    """
    path = f"economic"
    query_vars = {"apikey": apikey, 'name': name, 'from': from_date, 'to': to_date}
    return __return_json_v4(path=path, query_vars=query_vars)
