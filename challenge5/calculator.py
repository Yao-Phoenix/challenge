#!/usr/bin/env python3
import sys, csv, queue
from getopt import getopt, GetoptError
from configparser import ConfigParser
from multiprocessing import Process, Queue
from collections import namedtuple
from datetime import datetime

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


class Args(object):
    def __init__(self):
        '''
        self.options = self._options()

    def _options(self):
    '''
        try:
            opts, args = getopt(sys.argv[1:], 'hC:c:d:o:', ['help'])
        except GetoptError:
            print('Parameter Error')
            exit()
        options = dict(opts)
        if len(options) == 1 and list(options.keys())[0] in ['-h', '-help']:
            print('Usage: calculator.py -C cityname -c configfile -d \
                    userdata -o resultdata')
            exit()
        self.city_path = options['-C']
        self.config_path = options['-c']
        self.userdata_path = options['-d']
        self.export_path = options['-o']
        '''    
        return options

    def _value_after_option(self, option):
        value = self.options.get(option)
        return value

    @property
    def city_path(self):
        return self._value_after_option('-C')

    @property
    def config_path(self):
        return self._value_after_option('-c')

    @property
    def userdata_path(self):
        return self._value_after_option('-d')

    @property
    def export_path(self):
        return self._value_after_option('-o')
'''
args = Args()

class Config(object):
    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config = ConfigParser()
        config.read(args.config_path)
        if args.city_path and args.city_path.upper() in config.sections():
            return config[args.city_path.upper()]
        else:
            return config['DEFAULT']
        
    def _get_config(self, key):
        try:
            return float(self.config[key])
        except (ValueError, KeyError):
            print('Config Error')
            exit()

    @property
    def social_insurance_baseline_low(self):
        return self._get_config('JiShuL')

    @property
    def social_insurance_baseline_high(self):
        return self._get_config('JiShuH')

    @property
    def social_insurance_total_rate(self):
        return sum([
            self._get_config('YangLao'),
            self._get_config('YiLiao'),
            self._get_config('ShiYe'),
            self._get_config('GongShang'),
            self._get_config('ShengYu'),
            self._get_config('GongJiJin'),
            ])

config = Config()

class UserData(Process):
    def __init__(self, userdata_queue):
        super().__init__()
        self.userdata_queue = userdata_queue

    def _read_users_data(self):
        userdata = []
        with open(args.userdata_path) as f:
            for line in f.readlines():
                employee_id, string_income = line.strip().split(',')
                try:
                    income = int(string_income)
                except:
                    print('Parameter Error')
                    exit()
                userdata.append((employee_id, income))
        return userdata

    def run(self):
        for item in self._read_users_data():
            self.userdata_queue.put(item)
    

class IncomeTaxCalculator(Process):
    def __init__(self, userdata_queue, export_queue):
        super().__init__()
        self.userdata_queue = userdata_queue
        self.export_queue = export_queue

    @classmethod
    def calc_social_insurance_money(cls, income):
        if income < config.social_insurance_baseline_low:
            return config.social_insurance_baseline_low * \
                    config.social_insurance_total_rate
        elif income > config.social_insurance_baseline_high:
            return config.social_insurance_baseline_high * \
                    config.social_insurance_total_rate
        else:
            return income * config.social_insurance_total_rate

    @classmethod
    def calc_social_tax_and_remain(cls, income):
        social_insurance_money = cls.calc_social_insurance_money(income)
        real_income = income - social_insurance_money
        taxable_part = real_income - INCOME_TAX_START_POINT

        for item in INCOME_TAX_QUICK_Lookup_TABLE:
            if taxable_part > item.start_point:
                tax = taxable_part * item.tax_rate - item.quick_subtractor
                return '{:.2f}'.format(tax), '{:.2f}'.format(real_income - tax)

        return '0.00', '{:.2f}'.format(real_income)

    def calculate(self, employee_id, income):
            social_insurance_money = '{:.2f}'.format(
                    self.calc_social_insurance_money(income))
            tax, remain = self.calc_social_tax_and_remain(income)
            
            return [employee_id, income, social_insurance_money, tax, \
                    remain, datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
    def run(self):
        while True:
            try:
                employee_id, income = self.userdata_queue.get(timeout=1)
            except queue.Empty:
                return
            result = self.calculate(employee_id, income)

            self.export_queue.put(result)

class IncomeTaxExport(Process):
    def __init__(self, export_queue):
        super().__init__()
        self.export_queue = export_queue

        self.file = open(args.export_path, 'w', newline='')
        self.writer = csv.writer(self.file)

    def run(self):
        while True:
            try:
                item = self.export_queue.get(timeout=1)
            except:
                self.file.close()
                return

            self.writer.writerow(item)

if __name__ == '__main__':
    userdata_queue = Queue()
    export_queue = Queue()

    userdata = UserData(userdata_queue)
    calculator = IncomeTaxCalculator(userdata_queue, export_queue)
    export = IncomeTaxExport(export_queue)

    userdata.start()
    calculator.start()
    export.start()

    userdata.join()
    calculator.join()
    export.join()
