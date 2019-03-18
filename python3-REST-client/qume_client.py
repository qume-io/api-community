import time
import hashlib
import hmac
import json
import requests
import logging
import http.client as http_client

class qume_api_methods(object):

    def __init__(self, api_path, api_key, api_secret, api_passphrase, show_raw_request, timeout=10):
        self.api_path = api_path
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase
        self.timeout = timeout
        self.show_raw_request = show_raw_request

    # returns market statistics for a given contract market
    def get_market_statistics(self, market_id):
        endpoint = "/v1/instruments"
        post_url_string = "/%s" % market_id
        return self.make_request("GET", endpoint, post_url_string=post_url_string)

    # returns the funding rate for a given contract market
    def get_funding_rate(self, market_id):
        endpoint = "/v1/instruments"
        post_url_string = "/%s" % market_id + "/fundingRate"
        return self.make_request("GET", endpoint, post_url_string=post_url_string)

    # returns the funding rate for a given contract market
    def get_index_price(self, market_id):
        endpoint = "/v1/instruments"
        post_url_string = "/%s" % market_id + "/indexPrice"
        return self.make_request("GET", endpoint, post_url_string=post_url_string)

    # returns the funding rate for a given contract market
    def get_mark_price(self, market_id):
        endpoint = "/v1/instruments"
        post_url_string = "/%s" % market_id + "/markPrice"
        return self.make_request("GET", endpoint, post_url_string=post_url_string)

    # returns a user's active orders
    def get_open_orders(self):
        endpoint = "/v1/orders"
        return self.make_request("GET", endpoint)

    # places an order
    def place_order(self, symbol, side, price, qty, type, time_in_force, post_only, stop_trigger=None, stop_price=None):
        endpoint = "/v1/orders"
        post_body = { "symbol": symbol, "side": side, "price": price, "qty": qty, "type": type, "timeInForce": time_in_force, "postOnly": post_only, "triggerType": stop_trigger, "triggerPrice": stop_price }
        post_body_json = json.dumps(post_body)
        return self.make_request("POST", endpoint, post_body=post_body_json)

    # returns the status of an active order
    def get_active_order_status(self, order_id):
        endpoint = "/v1/orders"
        post_url_string = "/%s" % order_id
        return self.make_request("GET", endpoint, post_url_string=post_url_string)

    # deletes an active order
    def delete_active_order(self, order_id):
        endpoint = "/v1/orders"
        post_url_string = "/%s" % order_id
        return self.make_request("GET", endpoint, post_url_string=post_url_string)

    # returns the complete trade history
    def get_trade_history(self):
        endpoint = "/v1/trades"
        return self.make_request("GET", endpoint)

    # edits leverage for a given position
    def edit_position_leverage(self, symbol, desired_leverage):
        endpoint = "/v1/positions"
        post_url_string = "/%s" % symbol + "/leverage"
        post_body = { "portfolio": symbol, "leverage": desired_leverage }
        post_body_json = json.dumps(post_body)
        return self.make_request("PUT", endpoint, post_url_string=post_url_string, post_body=post_body_json)

    # returns all wallets
    def get_wallets(self):
        endpoint = "/v1/wallets"
        return self.make_request("GET", endpoint)

    # returns the state of each wallet
    def get_wallet_state(self, symbol):
        endpoint = "/v1/wallets"
        post_url_string = "/%s" % symbol
        return self.make_request("GET", endpoint, post_url_string=post_url_string)

    # returns all positions for a given market
    def get_all_positions(self, symbol):
        endpoint = "/v1/wallets"
        post_url_string = "/%s" % symbol + "/positions"
        return self.make_request("GET", endpoint, post_url_string=post_url_string)

    ##### utility functions #####

    # signs a message
    def sign_message(self, endpoint, timestamp, post_url_string, post_body):
        message = bytes(str(post_body) + timestamp + endpoint + post_url_string, encoding='utf-8')
        secret = bytes(self.api_secret, encoding='utf-8')
        signature = hmac.new(secret, message, hashlib.sha256).hexdigest()
        return signature

    # generates a unix timestamp in milliseconds
    def generate_unix_time_milliseconds(self):
        return str(int(time.time()) * 1000)


    # sends an HTTP request
    def make_request(self, request_type, endpoint, post_url_string="", post_body=""):

        # show raw HTTP request
        if self.show_raw_request:
            http_client.HTTPConnection.debuglevel = 1
            logging.basicConfig()
            logging.getLogger().setLevel(logging.DEBUG)
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True

        # create authentication headers
        timestamp = self.generate_unix_time_milliseconds()
        signature = self.sign_message(endpoint, timestamp, post_url_string, post_body)
        http_headers = {'X-QUME-SIGNATURE': signature, 'X-QUME-TIMESTAMP': timestamp, 'X-QUME-PASSPHRASE': self.api_passphrase, 'X-QUME-API-KEY' : self.api_key}
        url = self.api_path + endpoint + post_url_string

        if request_type == "GET":
            r = requests.get(url, headers=http_headers)
        elif request_type == "POST":
            payload = post_body
            r = requests.post(url, headers=http_headers, data=payload)
        elif request_type == "PUT":
            payload = post_body
            r = requests.put(url, headers=http_headers, data=payload)

        return r.text
