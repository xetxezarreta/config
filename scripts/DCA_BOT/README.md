# Coinbase DCA Bot

This is a simple and secure Python script for performing recurring buys on Coinbase Advanced Trading. It allows you to dollar-cost average (DCA) into cryptocurrencies like Bitcoin with much lower fees than the standard Coinbase platform.

This script submits a market buy order for a pre-configured amount of a specific cryptocurrency. For example, you can set it to buy €20 worth of BTC every week.

## How It Works

The script uses the official Coinbase Advanced Trade API to connect to your account and place a market buy order. It is designed to be run on a schedule (e.g., weekly, daily) to automate your investment strategy.

## Prerequisites

* **Python 3:** You must have Python 3 installed on your system.
* **Coinbase Account:** A Coinbase account with access to **Advanced Trading**.
* **API Keys:** You need to generate API keys from your Coinbase account with `trade` permissions.

## Installation

1.  **Clone or download the repository.**
2.  **Install the necessary Python library:**
    Open your terminal or command prompt and run:
    ```bash
    pip3 install coinbase-advanced-py
    ```

## Configuration

### 1. Set Up the Script

Open the `coinbase_dca.py` file and configure the following variables at the top of the file:

* `PRODUCT_ID`: The trading pair you want to use. You can find the correct Product ID on the Coinbase website. For buying Bitcoin with Euros, this is `"BTC-EUR"`.
* `QUOTE_SIZE`: The amount you want to spend for each recurring buy, in the quote currency (e.g., `"20"` for €20).

### 2. Get Your Coinbase API Keys

1.  Log in to [Coinbase](https://www.coinbase.com).
2.  Go to your profile settings and navigate to the **API** section.
3.  Click on **"+ New API Key"**.
4.  **Permissions:** Grant the `trade` permission. For security, do not grant `transfer` permissions unless you have a specific need for them.
5.  **IP Whitelisting:** (Recommended) For extra security, whitelist the IP address of the machine you will run the script from.
6.  Click **"Create"**. Coinbase will show you your **API Key** and **API Secret**.
    **Important:** Copy and save your API Secret immediately in a secure location. It will only be displayed once.

### 3. Set Environment Variables

For security, the script reads your API keys from environment variables. This prevents you from saving sensitive keys directly in the code.

* **On macOS and Linux:**
    ```bash
    export COINBASE_API_KEY="YOUR_API_KEY"
    export COINBASE_API_SECRET="YOUR_API_SECRET"
    ```
    To make these permanent, add these lines to your shell's profile file (e.g., `~/.bash_profile` or `~/.zshrc`).

* **On Windows (Command Prompt):**
    ```bash
    set COINBASE_API_KEY="YOUR_API_KEY"
    set COINBASE_API_SECRET="YOUR_API_SECRET"
    ```
    To set them permanently, search for "Environment Variables" in the Windows Start Menu and add them to your user or system variables.

## Usage

Once you have configured the script and set your environment variables, you can run it manually from your terminal:

```bash
python3 coinbase_dca.py
```

The script will connect to the Coinbase API and place the market order you configured.

## Automation

To make this a true DCA bot, you should schedule the script to run automatically.

* **On macOS and Linux (using `cron`):**
    1.  Open your crontab for editing: `crontab -e`
    2.  Add a line to schedule the script. For example, to run it every Monday at 8:00 AM, add:
        ```cron
        0 8 * * 1 /usr/bin/python3 /path/to/your/coinbase_dca.py
        ```
        Make sure to use the full, absolute path to both your python3 executable and the script.

* **On Windows (using Task Scheduler):**
    1.  Open **Task Scheduler**.
    2.  Click **"Create Basic Task..."**
    3.  Follow the wizard to set a name and trigger (e.g., "Weekly").
    4.  For the "Action," select **"Start a program"**.
    5.  For "Program/script," browse to your `python3.exe` file.
    6.  In "Add arguments (optional)," enter the full path to your `coinbase_dca.py` script.

## Disclaimer

* Trading cryptocurrency involves significant risk.
* This script is provided as-is, with no guarantees. Use it at your own risk.
* Always ensure your API keys are kept secure and have the minimum required permissions.
