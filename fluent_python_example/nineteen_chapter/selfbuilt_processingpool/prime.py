import math
import random

SEQUENCE = range(2, int(math.pow(10, 16)-1))
NUMBERS = random.sample(SEQUENCE, 20)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True

def main() -> None:
    is_prime(5_000_111_000_222_021)

if __name__ == '__main__':
    main()