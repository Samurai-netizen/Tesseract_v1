import asyncio
import niquests
import json

url = "https://api-seller.ozon.ru"
headers = {'Host': 'api-seller.ozon.ru', 'Client-Id': '2435732', 'Api-Key': '2ddf55f0-05e5-484e-9655-d424f72a0e82', "Content-Type": "application/json"}

async def v1_warehouse_list() -> None:
    async with niquests.AsyncSession() as s:
        method = "/v1/warehouse/list"
        print(url + method)
        r = await s.post(url + method, headers=headers)
        print(r.json())
        for item in r.json()['result']:
            print(item['name'])
        print("--------------------------------------------------------------")


async def v5_product_info_prices() -> None:
    async with niquests.AsyncSession() as s:
        method = "/v5/product/info/prices"
        print(url + method)
        payload = {
          "filter": {
            "product_id": [
              "1855823959"
            ],
            "visibility": "ALL"
          },
          "limit": 1
        }

        r = await s.post(url + method, headers=headers, json=payload)
        for item in r.json()['items']:
            print(item['price'])

        print("--------------------------------------------------------------")

async def v1_product_info_stocks_by_warehouse_fbs() -> None:
    async with niquests.AsyncSession() as s:
        method = "/v1/product/info/stocks-by-warehouse/fbs"
        print(url + method)
        # payload = {"sku": ["1855823959", "1775015354"]}
        payload = {"sku": ["1855823959"]}

        r = await s.post(url + method, headers=headers, json=payload)
        print(r.json())
        for item in r.json()['result']:
            print("В наличии, шт:", item['present'], "| Зарезервировано, шт:",  item['reserved'], "| Склад:", item['warehouse_name'])

        print("--------------------------------------------------------------")

