import csv
from janome.tokenizer import Tokenizer
t = Tokenizer()

step = '4-1'
t_class = 'sake'

final_result = []
result_list = []

data_list = []
data_list_sl = []
score_list = []
score_list_sl_1 = []
score_list_sl_2 = []
degree_list = []
emoticon_list = []
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
    with open('情緒詞.csv', newline = '') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            score_list.append(row)
        for sls in range(1, len(score_list)):
            if score_list[sls][1] == 'sake':
                score_list_sl_1.append(score_list[sls])
        if step == '4-1' or step == '4-2bf':
            for sls in range(0, len(score_list_sl_1)):
                if score_list_sl_1[sls][0] == 'train':
                    score_list_sl_2.append(score_list_sl_1[sls])
        else:
            for sls in range(0, len(score_list_sl_1)):
                score_list_sl_2.append(score_list_sl_1[sls])
elif t_class == 'beer':
    with open('評價資料 - beer.csv', newline = '') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            data_list.append(row)
        for dls in range(1, len(data_list)):
            data_list_sl.append(data_list[dls])
    with open('情緒詞.csv', newline = '') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            score_list.append(row)
        for sls in range(1, len(score_list)):
            if score_list[sls][1] == 'beer':
                score_list_sl_2.append(score_list[sls])
with open('程度詞.csv', newline = '') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        degree_list.append(row)
with open('表情符號.csv', newline = '') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        emoticon_list.append(row)

for dls in range(0, len(data_list_sl)):
    tokens = t.tokenize(data_list_sl[dls][1], wakati = True)
    result = []
    for token in tokens:
        result.append(token)
    total = 0
    final_result = []
    for search in range(len(result)):
        found = ""
        for sls in range(0, len(score_list_sl_2)):
            if result[search] == score_list_sl_2[sls][2]:
                if score_list_sl_2[sls][2] != found:
                    if score_list_sl_2[sls][3] == "-":
                        degree_search = 0
                        for dgls in range(1, len(degree_list)):
                            try:
                                if result[search + int(degree_list[dgls][1])] == degree_list[dgls][2]:
                                    degree_search = 1
                                    if degree_list[dgls][3] == "-":
                                        total += (float(score_list_sl_2 [sls][5]) * float(degree_list[dgls][5]))
                                        break
                                    else:
                                        if result[search + int(degree_list[dgls][3])] == degree_list[dgls][4]:
                                            total += (float(score_list_sl_2[sls][5]) * float(degree_list[dgls][5]))
                                            break
                            except:
                                continue
                        if degree_search == 0:
                            total += float(score_list_sl_2[sls][5])
                    else:
                        try:
                            if result[search + int(score_list_sl_2[sls] [3])] == score_list_sl_2[sls][4]:
                                found = score_list_sl_2[sls][2]
                                degree_search = 0
                                for dgls in range(1, len(degree_list)):
                                    try:
                                        if result[search + int(degree_list[dgls][1])] == degree_list[dgls][2]:
                                            degree_search = 1
                                            if degree_list[dgls][3] == "-":
                                                total += (float(score_list_sl_2[sls][5]) * float(degree_list[dgls][5]))
                                                break
                                            else:
                                                if result[search + int(degree_list[dgls][3])] == degree_list[dgls][4]:
                                                    total += (float(score_list_sl_2[sls][5]) * float(degree_list[dgls][5]))
                                                    break
                                    except:
                                        continue
                                if degree_search == 0:
                                    total += float(score_list_sl_2[sls][5])
                        except:
                            continue
                else:
                    continue
        for els in range(1, len(emoticon_list)):
            if result[search] == emoticon_list[els][1]:
                total += int(emoticon_list[els][2])
    if total > 0:
        final_result.append('positive')
    elif total < 0:
        final_result.append('negative')
    else:
        final_result.append('none')
    final_result.append(total)
    result_list.append(final_result)

with open('result_j-afinn.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    for rls in range(len(result_list)):
        writer.writerow(result_list[rls])