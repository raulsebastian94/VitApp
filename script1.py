import datetime
from collections import defaultdict
import pandas as pd

med_list = []


dic = defaultdict(dict)



class Medication:




    def __init__(self, name, strength, unit_measurement, date_rx_written, date_rx_filled, num_filled, num_remaining):
        self.name = name

        self.strength = strength

        self.unit_measurement = unit_measurement

        self.date_rx_written = date_rx_written

        self.date_rx_filled = date_rx_filled

        self.num_filled = num_filled

        self.num_remaining = num_remaining



    def update_dic(self):

        dic["Name"] = []
        dic["Name"].append(self.name)
        dic[self.name]['Strength'] = []
        dic[self.name]['Strength'].append(self.strength)
        dic[self.name]['Unit of Measurement'] = []
        dic[self.name]['Unit of Measurement'].append(self.unit_measurement)
        dic[self.name]['Date Written'] = []
        dic[self.name]['Date Written'].append(self.date_rx_written)
        dic[self.name]['Date Filled'] = []
        dic[self.name]['Date Filled'].append(self.date_rx_filled)
        dic[self.name]['Quantity Filled'] = []
        dic[self.name]['Quantity Filled'].append(self.num_filled)
        dic[self.name]['Quantity Remaining'] = []
        dic[self.name]['Quantity Remaining'].append(self.num_remaining)





var1 = Medication('Adderall', '20', 'mg', '2018-07-21', '2018-07-22', '30', '24')
var2 = Medication('Xanax', '1', 'mg', '2018-07-21', '2018-07-22', '30', '24')

var1.update_dic()
print(dic.iterrows())






















