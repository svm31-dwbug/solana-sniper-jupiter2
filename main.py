import os
import time

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
BUY_AMOUNT_SOL = 0.01
SELL_MULTIPLIER = 20

def log(msg):
    print(f"[SniperBot] {msg}")

def mock_buy():
    log(f"Koopt token met {BUY_AMOUNT_SOL} SOL via Jupiter DEX...")
    return {"token": "XYZ", "amount": 1000, "buy_price": 0.0001}

def mock_sell(token_info):
    sell_price = token_info['buy_price'] * SELL_MULTIPLIER
    log(f"Verkoopt {token_info['amount']} {token_info['token']} bij prijs {sell_price} SOL.")

def run_bot():
    log("Sniperbot gestart.")
    token_info = mock_buy()
    log("Wacht op 20x winst...")
    time.sleep(3)  # mock wachttijd
    mock_sell(token_info)
    log("Sniperbot klaar.")

if __name__ == "__main__":
    run_bot()
