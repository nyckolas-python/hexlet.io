#!/usr/bin/env python
# pip3 install aiohttp


# 1. asyncio фреймворк для создания событийных цыклов
# 2. Пример простой асинхронной програмы
# 3. Синтаксис async/await на замену @asyncio.coroutune and yield from
# 4. Пример асинхронного скачиания файлов

# Event loop:
#     coroutine > Task (Future)

import asyncio


@asyncio.coroutine
def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        
        yield from asyncio.sleep(0.1) # yield from == await


# @asyncio.coroutine # from Python < 3.7 async / await
async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f"{count} seconds have passed")
        count += 1
        
        await asyncio.sleep(1) # Python < 3.5 yield from == await


# @asyncio.coroutine # from Python < 3.7 async / await
async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await  asyncio.gather(task1, task2) # yield from == await


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    asyncio.run(main())