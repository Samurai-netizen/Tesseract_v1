import asyncio
import niquests
import json

from config import HEADERS

url = "https://api-seller.ozon.ru"
headers = HEADERS

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

async def v1_product_info_stocks_by_warehouse_fbs(sku):
    async with niquests.AsyncSession() as s:
        method = "/v1/product/info/stocks-by-warehouse/fbs"
        print(url + method)
        # payload = {"sku": ["1855823959", "1775015354"]}
        payload = {"sku": [f"{sku}"]}

        r = await s.post(url + method, headers=headers, json=payload)
        print(r.json())
        output = []
        for item in r.json()['result']:
            tmp = ("В наличии, шт:", item['present'], "| Зарезервировано, шт:",  item['reserved'], "| Склад:", item['warehouse_name'])
            output.append(tmp)

        print("--------------------------------------------------------------")
        return output

