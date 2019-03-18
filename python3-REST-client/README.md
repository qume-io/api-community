Qume Python3 Sample REST API Client
==================================
Example of a RESTful application for the [Qume Sandbox](https://sandbox.qume.io). Makes a call to each REST endpoint.


Quick Start
---------------

1. Edit `client.py` by entering your account details (API keys, passphrase, etc.)
2. Run `sample_application.py` after you review the script

Hints
----------------------

* Make sure you are using Python3
* To generate API keys, go to the "Accounts" page on the [Qume Sandbox](https://sandbox.qume.io)

Application Sample Output
-------------------------

The following is some of what you can expect when running this application:

```
get_market_statistics:
 {"marketStats":{"marketId":"BTCUSDQ","price":"3952.50","high":"4016.00","low":"3937.00","change":"-0.1777744","volume":"186900.00"}}
get_funding_rate:
 {fundingRate:"0.0"}
get_index_price:
 {"indexPrice":3954.6233333333334}
get_mark_price:
 {"markPrice":3950.92}
place_order:
 {"orderId":"1552771863928937015"}
place_stop_order:
 {"orderId":"1552771863928937119"}
get_open_orders:
 {"status":"OK","orders":[{"ts":"2019-03-18T08:00:26.677191688Z","id":"1552771863928797145","price":"33333","qty":"1","symbol":"BTCUSDQ","side":"SELL","originalQty":"1","type":"LIMIT","timeInForce":"UNTIL_CANCEL"},{"ts":"2019-03-18T08:00:27.358323431Z","id":"1552771863928797174","price":"14285","qty":"1","symbol":"BTCUSDQ","side":"BUY","originalQty":"1","type":"STOP_LIMIT","timeInForce":"UNTIL_CANCEL","triggerType":"MARK_PRICE","triggerPrice":"1000000"},{"ts":"2019-03-18T08:21:04.866581667Z","id":"1552771863928926640","price":"33333","qty":"1","symbol":"BTCUSDQ","side":"SELL","originalQty":"1","type":"LIMIT","timeInForce":"UNTIL_CANCEL"},{"ts":"2019-03-18T08:21:05.831673692Z","id":"1552771863928926700","price":"14285","qty":"1","symbol":"BTCUSDQ","side":"BUY","originalQty":"1","type":"STOP_LIMIT","timeInForce":"UNTIL_CANCEL","triggerType":"MARK_PRICE","triggerPrice":"1000000"},{"ts":"2019-03-18T08:22:58.146391685Z","id":"1552771863928937015","price":"33333","qty":"1","symbol":"BTCUSDQ","side":"SELL","originalQty":"1","type":"LIMIT","timeInForce":"UNTIL_CANCEL"},{"ts":"2019-03-18T08:22:58.881962422Z","id":"1552771863928937119","price":"14285","qty":"1","symbol":"BTCUSDQ","side":"BUY","originalQty":"1","type":"STOP_LIMIT","timeInForce":"UNTIL_CANCEL","triggerType":"MARK_PRICE","triggerPrice":"1000000"}]}
get_order_status:
 {"order":{"ts":"2019-03-18T08:00:26.677191688Z","id":"1552771863928797145","price":"33333","qty":"1","userId":"3aa4a5a6-6ea9-579b-943e-1cb3fc3ab7cd","symbol":"BTCUSDQ","side":"SELL","originalQty":"1","type":"LIMIT","timeInForce":"UNTIL_CANCEL"}}
delete_active_order:
 {"orderId":"1552771863928797446"}
get_trade_history:
 {"status":"OK","trades":[{"symbol":"BTCUSDQ","makerside":"BUY","makerOrderId":"1552771863928589460","takerOrderId":"1552771863928590245","price":"25355","qty":"1000","ts":"2019-03-18T07:35:29.135921844Z","id":"1552771863928590246"},{"symbol":"BTCUSDQ","makerside":"SELL","makerOrderId":"1552771863928588045","takerOrderId":"1552771863928595138","price":"25352","qty":"10","ts":"2019-03-18T07:35:58.723839758Z","id":"1552771863928595139"},{"symbol":"BTCUSDQ","makerside":"SELL","makerOrderId":"1552771863924769017","takerOrderId":"1552771863924784051","price":"25167","qty":"100","ts":"2019-03-18T00:28:50.258398541Z","id":"1552771863924784052"},{"symbol":"BTCUSDQ","makerside":"BUY","makerOrderId":"1552771863924780779","takerOrderId":"1552771863924784644","price":"25170","qty":"100","ts":"2019-03-18T00:28:53.449992721Z","id":"1552771863924784645"},{"symbol":"BTCUSDQ","makerside":"SELL","makerOrderId":"1552771863928575578","takerOrderId":"1552771863928584380","price":"25345","qty":"1000","ts":"2019-03-18T07:35:13.752137655Z","id":"1552771863928584381"},{"symbol":"BTCUSDQ","makerside":"BUY","makerOrderId":"1552771863928591272","takerOrderId":"1552771863928594459","price":"25355","qty":"10","ts":"2019-03-18T07:35:52.745495232Z","id":"1552771863928594460"}]}
edit_position_leverage:
 {leverage:"10"}
get_wallets:
 {"wallets":[{"walletId":"d1fe84c0-2223-3a2f-8c9f-d5dd5e77144c","asset":"BTC"},{"walletId":"cfe0f606-4535-35c0-9336-dfce15e10dd8","asset":"ETH"}]}
get_wallet_state:
 {"availableBalance":"99974855","balance":"99974855","orderMargin":"14815","fee":"0","positions":["BTCUSDQ"],"enabled":true}
get_all_positions:
 {"positions":[{"instrumentId":"BTCUSDQ","position":{"id":"BTCUSDQ","contract":{"id":"BTCUSDQ","notional":"0"},"orderMargin":"14815","initialMargin":"0","size":"0","entryValue":"0","leverage":"6.75","realizedPnl":"0"}}]}
```
