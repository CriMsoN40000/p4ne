from openpyxl import load_workbook
from matplotlib import pyplot


wb = load_workbook('/Users/alextreid/Downloads/data_analysis_lab.xlsx')
sheet = wb['Data']
sheet['A']

def getvalue(x): return x.value

list_x = list(map(getvalue, sheet['A'][1:]))
list_y = list(map(getvalue, sheet['C'][1:]))
list_z = list(map(getvalue, sheet['D'][1:]))

import matplotlib
matplotlib.use('TkAgg')
pyplot.plot(list_x, list_y, label="Tempreature")
pyplot.show

