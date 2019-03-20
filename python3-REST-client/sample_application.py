from qume_client import qume_api_methods
import ast

api_path = "https://api.qume.io"
timeout = 20

# insert account-specific api keys
api_key = "59e8a668-2232-48e0-871c-58f7d1baff24"
api_secret = "2f49f047db8c5017f1a571463ead3ed4"
api_passphrase = "example"

# initialize instance of client
qume_client = qume_api_methods(api_path, api_key=api_key, api_secret=api_secret, api_passphrase=api_passphrase, show_raw_request=False, timeout=timeout)

def test_api_methods():
    '''
    Tests each endpoint from the Qume REST API.
    '''

    # get market statistics for a given market
    result = qume_client.get_market_statistics("BTCUSDQ")
    print("get_market_statistics:\n", result)

    # get funding rate for a given market
    result = qume_client.get_funding_rate("BTCUSDQ")
    print("get_funding_rate:\n", result)

    # get index price for a given market
    result = qume_client.get_index_price("BTCUSDQ")
    print("get_index_price:\n", result)

    # get mark price for a given market
    result = qume_client.get_mark_price("BTCUSDQ")
    print("get_mark_price:\n", result)

    # place a limit order
    symbol = "BTCUSDQ"
    side = "BUY"
    price = 3000.00
    qty = 1
    type = "LIMIT"
    time_in_force = "UNTIL_CANCEL"
    post_only = False
    result = qume_client.place_order(symbol, side, price, qty, type, time_in_force, post_only)
    print("place_order:\n", result)

    # place a stop order
    symbol = "BTCUSDQ"
    side = "SELL"
    price = 7000.00
    qty = 1
    type = "STOP_LIMIT"
    time_in_force = "UNTIL_CANCEL"
    post_only = False
    stop_price = 100
    stop_trigger = "MARK_PRICE"
    result = qume_client.place_order(symbol, side, price, qty, type, time_in_force, post_only, stop_trigger, stop_price)
    print("place_stop_order:\n", result)

    # get open orders
    result = qume_client.get_open_orders()
    print("get_open_orders:\n", result)

    # get the status of an order
    active_orders = ast.literal_eval(result)
    order_id = active_orders.get('orders')[0].get('id') # paste another order id here, right now just gets a random order
    result = qume_client.get_active_order_status(order_id)
    print("get_order_status:\n", result)

    # delete an order
    # order_id_to_delete = active_orders.get('orders')[0].get('id') # paste another order id here, right now just deletes a random order
    order_id_to_delete = "1552447424432139200"
    result = qume_client.delete_active_order(order_id_to_delete)
    print("delete_active_order:\n", result)

    # get historical trades for a user
    result = qume_client.get_trade_history()
    print("get_trade_history:\n", result)

    # edit the current leverage for a given position
    result = qume_client.edit_position_leverage("BTCUSDQ", 10.00)
    print("edit_position_leverage:\n", result)

    # get all wallets
    result = qume_client.get_wallets()
    print("get_wallets:\n", result)

    # get the state of a wallet
    result = qume_client.get_wallet_state("BTC")
    print("get_wallet_state:\n", result)

    # get all positions for a user
    result = qume_client.get_all_positions("BTC")
    print("get_all_positions:\n", result)

# Run the test function
test_api_methods()
