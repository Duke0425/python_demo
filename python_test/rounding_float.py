from decimal import Decimal, ROUND_HALF_UP
Decimal('1.875').quantize(Decimal('0'), rounding=ROUND_HALF_UP)
Decimal('0.125').quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
Decimal('0.13')

from decimal import Decimal, ROUND_HALF_UP
origin_num = Decimal('11.245')
answer_num = origin_num.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
print(answer_num)