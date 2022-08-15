from math import pow
import logging

class CPFCalculator:

    _MaxLoanAmount = 4 * pow(10, 5)

    def __init__(self, aMothlyConBase, aTotalMonths):
        self.MyMonthlyContributionBase = aMothlyConBase
        self.MyTotalMonths = aTotalMonths

    def current_loan_amount(self):
        totalLoanAmount = 0
        for month in range(1, self.MyTotalMonths + 1):
            monthLoanAmount =  self.MyMonthlyContributionBase * month * 0.9
            totalLoanAmount += monthLoanAmount
            logging.info(f"Month: {month}, monthLoanAmount: {monthLoanAmount}")
        logging.info(f"totalLoanAmount: {totalLoanAmount}")
        return totalLoanAmount

    def number_of_months_from_the_maximum_loan_amount(self):
        currentLoanAmount = self.current_loan_amount()

        month = self.MyTotalMonths
        increaseMonth = 0
        while currentLoanAmount < CPFCalculator._MaxLoanAmount:
            month += 1
            increaseMonth += 1
            monthLoanAmount =  self.MyMonthlyContributionBase * month * 0.9
            currentLoanAmount += monthLoanAmount
            logging.info(f"month {month}, monthLoanAmount:{monthLoanAmount}, ====== currentLoanAmount {currentLoanAmount}")
        
        logging.info(f"{increaseMonth} months required")

    def change_monthly_base_cal_months(self, aNewMonthlyBase):
        increaseMonth = 0
        totalLoanAmount = 0
        while totalLoanAmount < CPFCalculator._MaxLoanAmount:
            increaseMonth += 1
            newLoanAmount = oldLoanAmount = totalLoanAmount = 0
            for month in range(1, increaseMonth):
                newLoanAmount += aNewMonthlyBase * increaseMonth * 0.9
            for month in range(increaseMonth + 1, self.MyTotalMonths + increaseMonth + 1):
                oldLoanAmount +=  self.MyMonthlyContributionBase * month * 0.9
            totalLoanAmount = newLoanAmount + oldLoanAmount
            logging.info(f"After {increaseMonth} months,  totalAmount: {totalLoanAmount}")
            
        logging.info(f"aNewMonthlyBase: {aNewMonthlyBase}, {increaseMonth} months required, totalAmount:{totalLoanAmount}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    cpfCalculator = CPFCalculator(1200, 14)
    cpfCalculator.current_loan_amount()
    # cpfCalculator.number_of_months_from_the_maximum_loan_amount()
    cpfCalculator.change_monthly_base_cal_months(1800)
