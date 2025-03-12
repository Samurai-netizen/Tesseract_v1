import asyncio
import niquests
import json


async def v1_warehouse_list() -> None:
    async with niquests.AsyncSession() as s:
        url = "https://api-seller.ozon.ru"
        method = "/v1/warehouse/list"
        print(url + method)
        headers = {'Host': 'api-seller.ozon.ru', 'Client-Id': '2435732', 'Api-Key': '2ddf55f0-05e5-484e-9655-d424f72a0e82', "Content-Type": "application/json"}
        payload = {"offer_id": "DOM6B", "product_id": 1855823959}
        payload = json.dumps(payload)

        r = await s.post(url + method, headers=headers, params=payload)
        print(r.json())
        for item in r.json()['result']:
            print(item['name'])
        print("--------------------------------------------------------------")


