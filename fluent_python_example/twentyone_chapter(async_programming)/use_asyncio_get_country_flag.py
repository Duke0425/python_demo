"""
使用asyncio , httpx 异步获取国家的国旗图片
"""
import asyncio
from httpx import AsyncClient
import sys
sys.path.insert(0, "e:\\duke_summary_python\\fluent_python_example\\twenty_chapter")
from flag import BASE_URL, save_flag, main


async def download_one(client: AsyncClient, cc: str) -> str:
    img = await get_flag(client, cc)
    save_flag(img, f"{cc}.gif")
    print(cc, end="", flush=True)
    return cc

async def get_flag(client: AsyncClient, cc: str) -> bytes:
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = await client.get(url, timeout=6.1, follow_redirects=True)
    return resp.read() 

def download_many(cc_list: list[str]) -> int:
    return asyncio.run(supervisor(cc_list))

async def supervisor(cc_list: list[str]) -> int:
    async with AsyncClient() as client:
        to_do = [download_one(client, cc) for cc in sorted(cc_list)]
        res = await asyncio.gather(*to_do)
    return len(res)


if __name__ == '__main__':
    main(download_many)
