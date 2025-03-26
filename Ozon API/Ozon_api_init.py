import asyncio
from API_requests_list import v1_warehouse_list, v5_product_info_prices, v1_product_info_stocks_by_warehouse_fbs
from Database.DB_Conn import DB_test


async def main() -> None:
    await v1_warehouse_list()
    await v5_product_info_prices()
    await v1_product_info_stocks_by_warehouse_fbs()
    await DB_test()


if __name__ == "__main__":
    asyncio.run(main())
