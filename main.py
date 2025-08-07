import time
import datetime


def fetch_exchange_rate():
    now = datetime.datetime.now()
    print(f"[{now}] Fetching exchange rates...")
    time.sleep(2)
    print("USD -> EGP = 30.90 ")
    print("EUR -> EGP = 33.20 ")
    print("Done.")


if __name__ == "__main__":
    fetch_exchange_rate()