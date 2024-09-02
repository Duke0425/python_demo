import itertools
import time
from threading import Thread, Event

def spin(aChar: str, aEvent: Event) -> None:
    for spinChar in itertools.cycle(r"/|\-"):
        status = f"\r{spinChar} {aChar}"
        print(status, end="", flush=True)
        if aEvent.wait(0.1):
            break
    blanks = ' ' * len(status)
    print(f"\r{blanks}\r", end="")

def timewait() -> int:
    time.sleep(3)
    return 42

def supervizor() -> str:
    done = Event()
    thread = Thread(target=spin, args=("thinking~", done))
    thread.start()
    result = timewait()
    done.set()
    thread.join()
    return result

def main() -> None:
    result = supervizor()
    print(f"Answer: {result}")

if __name__ == '__main__':
    main()