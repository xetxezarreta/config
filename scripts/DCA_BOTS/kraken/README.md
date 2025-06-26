# Kraken DCA Bot

This is a simple and secure Python script for performing recurring buys on Kraken. It allows you to dollar-cost average (DCA) into cryptocurrencies by automating your investment strategy.

This script submits a market buy order for a pre-configured amount of a specific currency. For example, you can set it to buy €20 worth of BTC every week.

## How It Works

The script uses the `krakenex` Python library to connect to your Kraken account via the official API. It places a market buy order for a specified amount (e.g., €20). Since the Kraken API requires a `volume` for market orders, the script first fetches the current ticker price to calculate the correct volume of the asset to buy with your specified amount.

## Prerequisites

* **Python 3:** You must have Python 3 installed on your system.
* **Kraken Account:** A Kraken account with some funds to trade.
* **API Keys:** You need to generate API keys from your Kraken account with the necessary permissions.

## Installation

1.  **Clone or download the script.**
2.  **Install the necessary Python library:**
    Open your terminal or command prompt and run:
    ```bash
    pip3 install krakenex
    ```

## Configuration

### 1. Set Up the Script

Open the Python script file and configure the following variables at the top of the file:

* `ASSET_PAIR`: The trading pair you want to use. You can find these on the Kraken website. Note that Kraken uses specific naming conventions (e.g., `"XBT/EUR"` for Bitcoin in Euros).
* `QUOTE_SIZE`: The amount you want to spend for each recurring buy, in the quote currency (e.g., `"20"` for €20).

### 2. Get Your Kraken API Keys

1.  Log in to your [Kraken](https://www.kraken.com) account.
2.  Click on your profile name in the top-right corner and select **Security > API**.
3.  Click the **"+ Add key"** button.
4.  **Permissions:** Grant the following permissions:
    * `Query Funds` (allows the script to check your balance)
    * `Create & Modify Orders` (allows the script to place buy orders)
    For better security, do not grant `Withdraw Funds` permissions.
5.  **IP Whitelisting:** (Recommended) For extra security, you can whitelist the IP address of the machine you will run the script from if it's static.
6.  Click **"Generate key"**. Kraken will show you your **API Key** and **Private Key**.
    **Important:** Copy and save your **Private Key** immediately in a secure location. It will only be displayed once.

### 3. Set Environment Variables

For security, the script reads your API keys from environment variables. This prevents you from saving sensitive keys directly in the code.

* **On macOS and Linux:**
    ```bash
    export KRAKEN_API_KEY="YOUR_API_KEY"
    export KRAKEN_PRIVATE_KEY="YOUR_PRIVATE_KEY"
    ```
    To make these permanent, add these lines to your shell's profile file (e.g., `~/.bash_profile` or `~/.zshrc`).

* **On Windows (Command Prompt):**
    ```bash
    set KRAKEN_API_KEY="YOUR_API_KEY"
    set KRAKEN_PRIVATE_KEY="YOUR_PRIVATE_KEY"
    ```
    To set them permanently, search for "Environment Variables" in the Windows Start Menu and add them to your user or system variables.

## Usage

Once you have configured the script and set your environment variables, you can run it manually from your terminal:

```bash
python3 kraken_dca.py
```

The script will connect to the Kraken API, validate, and then place the market order you configured.

## Automation

To make this a true DCA bot, you should schedule the script to run automatically.

* **On macOS and Linux (using `cron`):**
    1.  Open your crontab for editing: `crontab -e`
    2.  Add a line to schedule the script. For example, to run it every Monday at 8:00 AM, add:
        ```cron
        0 8 * * 1 /usr/bin/python3 /path/to/your/kraken_dca.py
        ```
        Make sure to use the full, absolute path to both your python3 executable and the script.

* **On Windows (using Task Scheduler):**
    1.  Open **Task Scheduler**.
    2.  Click **"Create Basic Task..."**
    3.  Follow the wizard to set a name and trigger (e.g., "Weekly").
    4.  For the "Action," select **"Start a program"**.
    5.  For "Program/script," browse to your `python3.exe` file.
    6.  In "Add arguments (optional)," enter the full path to your `kraken_dca.py` script.

## Disclaimer

* Trading cryptocurrency involves significant risk.
* This script is provided as-is, with no guarantees. Use it at your own risk.
* Always ensure your API keys are kept secure and have the minimum required permissions.
