import asyncio
import niquests
import json

url = "https://api-seller.ozon.ru"
headers = {'Host': 'api-seller.ozon.ru', 'Client-Id': '2435732', 'Api-Key': '2ddf55f0-05e5-484e-9655-d424f72a0e82', "Content-Type": "application/json"}

async def v1_warehouse_list() -> None:
    async with niquests.AsyncSession() as s:
        method = "/v1/warehouse/list"
        print(url + method)
        payload = {"offer_id": "DOM6B", "product_id": 1855823959}
        payload = json.dumps(payload)

        r = await s.post(url + method, headers=headers, params=payload)
        print(r.json())
        for item in r.json()['result']:
            print(item['name'])
        print("--------------------------------------------------------------")


async def v5_product_info_prices() -> None:
    async with niquests.AsyncSession() as s:
        method = "/v5/product/info/prices"
        print(url + method)
        payload = {
          "cursor": "string",
          "filter": {
            "offer_id": [
              "DOM6B"
            ],
            "product_id": [
              "1855823959"
            ],
            "visibility": "ALL"
          },
          "limit": 1
        }
        payload = json.dumps(payload)

        r = await s.post(url + method, headers=headers, params=payload)
        print(r.json())

        print("--------------------------------------------------------------")

