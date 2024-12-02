"""
一个asynicio 示例: 探测域名
"""
import asyncio
import socket
from keyword import kwlist

MAX_KEYWORD = 4

async def probe(domain: str) -> tuple:
    loop = asyncio.get_running_loop()
    try:
        await loop.getaddrinfo(domain, None)
    except socket.gaierror:
        return (domain, False)
    return domain, True

async def main():
    names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD)
    domains = (f"{name}.dev".lower() for name in names)
    coros = [probe(domain) for domain in domains]
    for coro in asyncio.as_completed(coros):
        domain, found = await coro
        mark = '+' if found else ''
        print(f'{mark} {domain}')

"""                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
for 关键字处理可迭代对象. await 处理 可异步调用对象

两种可异步调用对象:
1. 原生协程: 通过调用原生协程函数得到
2. asyncio.Task 通常由把协程对象传给asyncio.create_task()得到

异步上下文管理器: 上下文管理拥有__enter__ __exit__ 魔法方法, 而异步上下文管理器, __aenter__, __aexit__. 
     PostgreSQL 数据库的连接和操作就可以使用异步上下文管理器, 来实现并发操作
"""


if __name__ == '__main__':
    asyncio.run(main())
