import asyncio
from API_requests_list import v1_warehouse_list


async def main() -> None:
    await v1_warehouse_list()


if __name__ == "__main__":
    asyncio.run(main())
