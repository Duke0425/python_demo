
import logging

class Example:
    pass


class Compare:

    @staticmethod
    def compare_by_symbol_eq(aObjectA, aObjectB):
        return aObjectA == aObjectB

    @staticmethod
    def compare_by_keyword_is(aObjectA, aObjectB):
        return aObjectA is aObjectB


def main():
    logging.basicConfig(level=logging.DEBUG)
    num_a = {'dicr': 1}
    num_b = {'dicr': 1}
    result_eq = Compare.compare_by_symbol_eq(num_a, num_b)
    result_is = Compare.compare_by_keyword_is(num_a, num_b)
    logging.info(f"result_eq:{result_eq} // result_is:{result_is}")

if __name__ == '__main__':
    main()