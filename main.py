import time
import random

def main():
    print("[SniperBot] Sniperbot gestart.")

    while True:
        try:
            print("[SniperBot] Zoekt nieuwe tokens...")

            koopprijs = koop_token()
            wacht_op_winst(koopprijs)
            verkoop_token(koopprijs)

            print("[SniperBot] Wacht op nieuwe kansen...")
            time.sleep(30)

        except Exception as e:
            print(f"[SniperBot] Fout opgetreden: {e}")
            time.sleep(10)

def koop_token():
    koopprijs = round(random.uniform(0.001, 0.005), 6)
    print(f"[SniperBot] Koopt token met 0.01 SOL aan prijs {koopprijs} SOL.")
    return koopprijs

def wacht_op_winst(koopprijs):
    print("[SniperBot] Wacht op 5x winst...")
    target_price = round(koopprijs * 5, 6)

    current_price = koopprijs
    while current_price < target_price:
        # Simuleer prijsstijging
        current_price += round(random.uniform(0.0001, 0.001), 6)
        print(f"[SniperBot] Huidige prijs: {current_price} SOL (doel: {target_price} SOL)")
        time.sleep(2)

    print(f"[SniperBot] 5x winst bereikt! ({current_price} SOL)")

def verkoop_token(koopprijs):
    verkoopprijs = round(koopprijs * 5, 6)
    winst = round(verkoopprijs - koopprijs, 6)
    print(f"[SniperBot] Verkoopt token bij {verkoopprijs} SOL. Winst: {winst} SOL.")

if __name__ == "__main__":
    main()
