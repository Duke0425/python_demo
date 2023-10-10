import random
import asyncio
import logging


class RandomTestAsynio:

    # ANSI colors
    _colors = (
        "\033[0m",   # End of color
        "\033[36m",  # Cyan
        "\033[91m",  # Red
        "\033[35m",  # Magenta
    )

    @classmethod
    async def make_random(cls, aColorIndex, threshold = 6):
        logging.info(cls._colors[aColorIndex] + f"Initiated makerandom({aColorIndex}).")
        random_number = random.randint(0, 10)
        while random_number < threshold:
            logging.info(cls._colors[aColorIndex] + f"makerandom({aColorIndex}) == {random_number} too low; retrying.")
            await asyncio.sleep(3)
            random_number = random.randint(0, 10)
        logging.info(cls._colors[aColorIndex] + f"---> Finished: makerandom({aColorIndex}) == {random_number}" + cls._colors[0])
        return random_number

    @classmethod
    async def main(cls):
        result = await asyncio.gather(*(cls.make_random(index, 10-index-1) for index in range(4)))
        return result

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, datefmt="%H:%M:%S")
    result = asyncio.run(RandomTestAsynio.main())
    logging.info(f"Main: get result {result}")
