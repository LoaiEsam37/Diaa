import requests
from colorama import Fore


def fetch(token, item_code):

    s = requests.session()

    try:
        res = s.post("https://merchant.api.taager.com/api/variant-groups/search",
                     json={"pageSize": 12, "page": 1, "query": item_code, "sortBy": "closestMatch",
                           "lockedOnly": False, "onlyGroupsOnSale": False, "merchantLockedOnly": False,
                           "onlyDiscountedAsSecondInPlacement": False, "countable": True},
                     headers={
                         "authorization": token,
                         "country": "EGY",
                         "platform": "web",
                         "ui-session-key": "C6I2S5VdXpCkt2E5DtXydcBxfJhiG0Rx",
                         "version": "1.186.0"
                     })
    except:
        print(
            Fore.RED + f"[ ERR ] {item_code} has an Unkown Error - {res.status_code}")

    return res
