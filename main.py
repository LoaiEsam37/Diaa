import json
import time
from colorama import Fore
import requests
from src.fetch import fetch


def main():

    try:
        requests.get("https://www.google.com")
    except:
        exit(Fore.RED + "[ ERR ] Check your internet Connection and try again")
    with open("./Items.txt", "r") as f:
        item_codes = f.read().split("\n")

    with open("./src/Token.json", "r") as f:
        token = json.load(f)["authorization"]

    EXIST = 0
    for item_code in item_codes:
        res = fetch(token, item_code)
        if res.status_code == 401:
            exit(Fore.RED + "[ ERR ] Token is invaild")
        try:
            available = res.json()[
                "results"][0]["primaryVariant"]["isAvailableToSeller"]
            if available:
                EXIST += 1
                print(Fore.GREEN +
                      f"[ OK ] {item_code} Exists - {res.status_code}")
            else:
                print(
                    Fore.RED + f"[ ERR ] {item_code} doesn`t Exist - {res.status_code}")
        except:
            print(
                Fore.RED + f"[ ERR ] {item_code} doesn`t Exist - {res.status_code}")

        time.sleep(3)

    print("\n\n")
    print(Fore.WHITE + f"{EXIST} Items Exist out of {len(item_codes)}\n")


if __name__ == "__main__":
    main()
