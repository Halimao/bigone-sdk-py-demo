from bigone.client import BigOneClient

cli = BigOneClient("", "")
print(cli.get_trades("BTC-USDT"))