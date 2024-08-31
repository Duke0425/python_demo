import sys
from time import perf_counter
from typing import NamedTuple
from multiprocessing import Process, SimpleQueue, cpu_count
from multiprocessing import queues

from prime import is_prime, NUMBERS

class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: str

JobQueue = queues.SimpleQueue[int]
ResultsQueue = queues.SimpleQueue[PrimeResult]

def check(num: int) -> PrimeResult:
    start_time = perf_counter()
    prime = is_prime(num)
    return PrimeResult(n = num, prime=prime, elapsed=perf_counter()-start_time)

def start_job(procs: int, jobs: JobQueue, results: ResultsQueue) -> None:
    for num in NUMBERS:
        jobs.put(num)
    for _ in range(procs):
        p = Process(target=worker, args=(jobs, results))
        p.start()
        jobs.put(0)

def worker(jobs: JobQueue, results: ResultsQueue):
    while n := jobs.get():
        results.put(check(n))
    results.put(PrimeResult(0, False, 0))

def main() -> None:
    if len(sys.argv) < 2:
        procs = cpu_count()
    else:
        procs = sys.argv[1]

    print(f"Checking {len(NUMBERS)} number multiprocessing")
    results: ResultsQueue = SimpleQueue()
    jobs:JobQueue  = SimpleQueue()

    t0 = perf_counter()
    start_job(procs, jobs, results)
    checked = report(procs, results)
    elapsed = perf_counter() - t0
    print(f"Total time: {checked} checks in {elapsed:.2f}s")

def report(procs: int, results: ResultsQueue) -> int:
    checked = 0
    procs_count = 0
    while procs_count < procs: 
        result: PrimeResult = results.get()
        if result.n == 0:
            procs_count += 1
        else:
            checked += 1
            label = 'p' if result.prime else ''
            print(f'{result.n:16} {label} {result.elapsed:9.6f}s')
    return checked

if __name__ == '__main__':
    main()
