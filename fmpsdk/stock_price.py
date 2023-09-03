from .url_methods import __return_json_v3


def stock_price_change(apikey: str, tickers: str | list) -> list[dict]:
    """
    Query FMP /stock-price-change API

    :param apikey: Your API key.
    :param symbol: Ticker of company.
    :return: A list of dictionaries.
    """
    path = f"stock-price-change/"
    if type(tickers) is not list:
        tickers = [tickers]
    tickers = ",".join(tickers)
    path += tickers
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)

