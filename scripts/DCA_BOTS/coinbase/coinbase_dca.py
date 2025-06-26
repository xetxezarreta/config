#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple and secure Python script to perform recurring buys on Coinbase
Advanced Trading.

This script is designed for dollar-cost averaging (DCA) by submitting
market orders for a specified amount in a given currency (e.g., EUR).
"""

import os
import uuid
from coinbase.rest import RESTClient

# --- Configuration ---
# The product to trade. You can find product IDs on the Coinbase website.
# For example, for Bitcoin in Euros, the product ID is "BTC-EUR".
PRODUCT_ID = "BTC-EUR"

# The amount of quote currency (e.g., EUR) to spend on each purchase.
# For example, to buy 20€ worth of BTC, set this to "20".
QUOTE_SIZE = "20"


def place_market_order(client, product_id, quote_size):
    """
    Places a market buy order on Coinbase Advanced Trading.

    Args:
        client: The Coinbase RESTClient object.
        product_id: The ID of the product to trade (e.g., "BTC-EUR").
        quote_size: The amount of quote currency to spend.

    Returns:
        The order response from the Coinbase API, or None if the order failed.
    """
    try:
        # Generate a unique client order ID for each order.
        # This helps prevent accidental duplicate orders.
        client_order_id = str(uuid.uuid4())

        print(f"Placing a market buy order for {quote_size} EUR of {product_id}...")

        order = client.market_order_buy(
            client_order_id=client_order_id,
            product_id=product_id,
            quote_size=quote_size,
        )

        if order and order.get('success'):
            print("Order placed successfully!")
            print(f"Order ID: {order['order_id']}")
            return order
        else:
            print("Failed to place order.")
            print(f"Error response: {order.get('error_response')}")
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
    api_key = os.environ.get("COINBASE_API_KEY")
    api_secret = os.environ.get("COINBASE_API_SECRET")

    if not api_key or not api_secret:
        print("Error: COINBASE_API_KEY and COINBASE_API_SECRET environment variables are not set.")
        print("Please set these variables with your Coinbase API key and secret.")
        return

    # Initialize the Coinbase REST client
    try:
        client = RESTClient(api_key=api_key, api_secret=api_secret)
        print("Successfully connected to the Coinbase API.")
    except Exception as e:
        print(f"Error connecting to Coinbase API: {e}")
        return

    # Place the market order
    place_market_order(client, PRODUCT_ID, QUOTE_SIZE)


if __name__ == "__main__":
    main()
