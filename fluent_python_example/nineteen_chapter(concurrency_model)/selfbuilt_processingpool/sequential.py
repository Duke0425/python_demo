from fluent_python_example.nineteen_chapter.selfbuilt_processingpool.prime import is_prime, NUMBERS
from time import perf_counter
from typing import NamedTuple

class Result(NamedTuple):
    prime: bool
    elapsed: str

def check(num):
    start_time = perf_counter()
    prime = is_prime(num)
    return Result(prime=prime, elapsed=perf_counter()-start_time)

def main() -> None:
    print(f"Checking {len(NUMBERS)} number sequentially")
    t0 = perf_counter()
    for n in NUMBERS:
        prime, elapsed = check(n)
        label = 'p' if prime else ''
        print(f'{n:16} {label} {elapsed:9.6f}s')

    elapsed = perf_counter() - t0
    print(f"Total timeL: {elapsed:.2f}s")

if __name__ == '__main__':
    main()