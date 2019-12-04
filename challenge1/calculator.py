#!/usr/bin/env python3
import sys
from collections import namedtuple

IncomeTaxQuickLookupItem = namedtuple(
        'IncomeTaxQuickLookupItem',
        ['start_point', 'tax_rate', 'quick_subtractor']
        )

INCOME_TAX_START_POINT = 5000

INCOME_TAX_QUICK_Lookup_TABLE = [
        IncomeTaxQuickLookupItem(80000, 0.45, 15160),
        IncomeTaxQuickLookupItem(55000, 0.35, 7160),
        IncomeTaxQuickLookupItem(35000, 0.3, 4410),
        IncomeTaxQuickLookupItem(25000, 0.25, 2660),
        IncomeTaxQuickLookupItem(12000, 0.2, 1410),
        IncomeTaxQuickLookupItem(3000, 0.1, 210),
        IncomeTaxQuickLookupItem(0, 0.03, 0)
        ]

try:
    income = int(sys.argv[1])
except ValueError:
    print('Parameter Error')
    exit()

real_income = income - INCOME_TAX_START_POINT

if real_income <= 0:
    print('0.00')
else:
    for item in INCOME_TAX_QUICK_Lookup_TABLE:
        if real_income > item.start_point:
            result = real_income * item.tax_rate - item.quick_subtractor
            print('{:.2f}'.format(result))
            break
