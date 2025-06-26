#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple and secure Python script to perform recurring buys on Kraken.

This script is designed for dollar-cost averaging (DCA) by submitting
market orders for a specified amount in a given currency (e.g., EUR).
"""

import os
import time
import krakenex
from decimal import Decimal

# --- Configuration ---
# The asset pair to trade. You can find these on the Kraken website.
# Note: Kraken uses specific naming, e.g., "XBT/EUR" for Bitcoin in Euros.
ASSET_PAIR = "XBT/EUR"

# The amount of quote currency (e.g., EUR) to spend on each purchase.
# For example, to buy 20€ worth of BTC, set this to "20".
QUOTE_SIZE = "20"


def place_market_order(k, pair, quote_size):
    """
    Places a market buy order on Kraken.

    Args:
        k: The krakenex.API object.
        pair: The asset pair to trade (e.g., "XBT/EUR").
        quote_size: The amount of quote currency to spend.

    Returns:
        The order response from the Kraken API, or None if the order failed.
    """
    print(f"Placing a market buy order for {quote_size} EUR of {pair}...")

    try:
        # Kraken's add_order for market buys requires 'volume'.
        # We calculate the volume by getting the current ticker price.
        ticker = k.query_public('Ticker', {'pair': pair})
        if ticker.get('error'):
            print(f"Error getting ticker info: {ticker['error']}")
            return None

        # Get the current ask price to calculate volume
        # The ticker result is a dict where the key is the pair's altname
        pair_altname = list(ticker['result'].keys())[0]
        ask_price = Decimal(ticker['result'][pair_altname]['a'][0])
        volume = Decimal(quote_size) / ask_price

        # The 'cost' parameter is not universally supported, so calculating
        # volume is the most reliable method for market orders.
        order_data = {
            "pair": pair,
            "type": "buy",
            "ordertype": "market",
            "volume": f"{volume:.8f}",  # Format volume to 8 decimal places
            "validate": True # Use 'validate': True to test the order first
        }

        # First, validate the order without executing
        test_run = k.query_private('AddOrder', order_data)
        if test_run.get('error'):
            print("Error validating the order.")
            print(f"Error response: {test_run.get('error')}")
            return None
        
        print("Order validated successfully. Now placing the actual order.")

        # If validation is successful, remove the 'validate' key and place the order
        del order_data['validate']
        order_response = k.query_private('AddOrder', order_data)

        if not order_response.get('error'):
            print("Order placed successfully!")
            print(f"Order Description: {order_response['result']['descr']['order']}")
            print(f"Transaction IDs: {', '.join(order_response['result']['txid'])}")
            return order_response
        else:
            print("Failed to place order.")
            print(f"Error response: {order_response.get('error')}")
            return None

    except Exception as e:
        print(f"An error occurred while placing the order: {e}")
        return None


def main():
    """
    The main function of the script.
    """
    # It is highly recommended to use environment variables for your API keys
    # for security reasons. Do not hardcode them in your script.
    # Make sure your API key has "Create & Modify Orders" permission.
    api_key = os.environ.get("KRAKEN_API_KEY")
    api_secret = os.environ.get("KRAKEN_PRIVATE_KEY")

    if not api_key or not api_secret:
        print("Error: KRAKEN_API_KEY and KRAKEN_PRIVATE_KEY environment variables are not set.")
        print("Please set these variables with your Kraken API key and private key.")
        return

    # Initialize the Kraken API client
    try:
        k = krakenex.API(key=api_key, secret=api_secret)
        # Check connection by fetching account balance
        balance = k.query_private('Balance')
        if balance.get('error'):
             print(f"Error connecting to Kraken API: {balance.get('error')}")
             return
        print("Successfully connected to the Kraken API.")
    except Exception as e:
        print(f"Error connecting to Kraken API: {e}")
        return

    # Place the market order
    place_market_order(k, ASSET_PAIR, QUOTE_SIZE)


if __name__ == "__main__":
    main()
