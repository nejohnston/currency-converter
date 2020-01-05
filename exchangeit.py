"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Nicholas Johnston
Date:   January 3rd 2020
"""

import currency

src = input('3-letter code for original currency: ')
dst = input('3-letter code for the new currency: ')
amt = input('Amount of the original currency: ')
values = currency.exchange(src, dst, float(amt))
exchange_amt = round(values, 3)
print('You can exchange {0} {1} for {2} {3}.'.format(
    amt, src, str(exchange_amt), dst))
