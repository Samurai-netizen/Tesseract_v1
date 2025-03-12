import asyncio
from API_requests_list import v1_warehouse_list, v5_product_info_prices


async def main() -> None:
    await v1_warehouse_list()
    await v5_product_info_prices()


if __name__ == "__main__":
    asyncio.run(main())
