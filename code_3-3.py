import csv
from asari.api import Sonar
sonar = Sonar()

step = '4-1'
t_class = 'sake'

data_list = []
data_list_sl = []
if t_class == 'sake':
    with open('評價資料 - sake.csv', newline = '') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            data_list.append(row)
        if step == '4-1':
            for dls in range(1, len(data_list)):
                if data_list[dls][0] == 'train':
                    data_list_sl.append(data_list[dls])
        else:
            for dls in range(1, len(data_list)):
                if data_list[dls][0] == 'test':
                    data_list_sl.append(data_list[dls])
elif t_class == 'beer':
    with open('評價資料 - beer.csv', newline = '') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            data_list.append(row)
        for dls in range(1, len(data_list)):
            data_list_sl.append(data_list[dls])

with open('result_asari.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    for dls in range(0, len(data_list_sl)):
        final_result = []
        result_list = []
        output = sonar.ping(text = data_list_sl[dls][1])
        result_1 = output['top_class']
        if output['top_class'] == 'negative':
            result_2 = output['classes'][0]['confidence']
        else:
            result_2 = output['classes'][1]['confidence']
        final_result.append(result_1)
        final_result.append(result_2)
        result_list.append(final_result)
        writer.writerow(result_list[0])