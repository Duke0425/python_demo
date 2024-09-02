import itertools
import asyncio

async def spin(aChar: str) -> None:
    for spinChar in itertools.cycle(r"/|\-"):
        status = f"\r{spinChar} {aChar}"
        print(status, end="", flush=True)
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break

    blanks = ' ' * len(status)
    print(f"\r{blanks}\r", end="")

async def timewait() -> int:
    await asyncio.sleep(3)
    return 42

async def supervizor() -> str:
    task = asyncio.create_task(spin('thinking!'))
    result = await timewait()
    task.cancel()
    return result

def main() -> None:
    result = asyncio.run(supervizor())
    print(f"Answer: {result}")

if __name__ == '__main__':
    main()