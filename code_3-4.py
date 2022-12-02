import csv

step = 1
t_class = 'sake'
care_zero = False

result_list = []
result_list_sl = []
result_list_jafinn = []
result_list_asari = []

if t_class == 'sake':
    with open('評價資料 - sake.csv', newline = '') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            result_list.append(row)
        if step == 1:
            for dls in range(1, len(result_list)):
                if result_list[dls][0] == 'train':
                    result_list_sl.append(result_list[dls])
        else:
            for dls in range(1, len(result_list)):
                if result_list[dls][0] == 'train':
                    result_list_sl.append(result_list[dls])
else:
    with open('評價資料 - beer.csv', newline = '') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            result_list.append(row)
        for dls in range(1, len(result_list)):
            result_list_sl.append(result_list[dls])

if t_class == 'sake':
    if step == 1:
        with open('result_j-afinn_s41.csv', newline = '') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                result_list_jafinn.append(row)
    else:
        with open('result_j-afinn_s42bf.csv', newline = '') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                result_list_jafinn.append(row)
else:
    with open('result_j-afinn_b41.csv', newline = '') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            result_list_jafinn.append(row)

if t_class == 'sake':
    if step == 1:
        with open('result_asari_s41.csv', newline = '') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                result_list_asari.append(row)
    else:
        with open('result_asari_s42.csv', newline = '') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                result_list_asari.append(row)
else:
    with open('result_asari_b41.csv', newline = '') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            result_list_asari.append(row)

file = open('index.html', 'w')
file.write("<!DOCTYPE html>\n")
file.write("<script src='https://code.jquery.com/jquery-3.5.1.min.js'></script>\n")
file.write("<script src='https://code.highcharts.com/highcharts.js'></s cript>\n")
file.write("<html>\n")
file.write("<head>\n")
file.write("<title>Test</title>\n")
file.write("</head>\n")
file.write("<body>\n")
file.write("<div id='container' style='width:100%; height:100%;'>\n")
file.write("<script>\n")
file.write("var data = {\n")
file.write("chart: {type: 'line'},\n")
file.write("title: {text: '情緒分析結果'},\n")
file.write("xAxis: {categories: [")

for i in range(1, 100):
    file.write("'" + str(i) + "', ")
file.write("'100'")

file.write("]},\n")
file.write("yAxis: {title: {text: '情緒分數'}},\n")
file.write("plotOptions: {line: {dataLabels: {enabled: false}, enableMo useTracking: false}},\n")
file.write("series: [{\n")
file.write("name: '專家評分', data: [")

for i in range(len(result_list_sl) - 1):
    file.write(str(result_list_sl[i][2]) + ", ")
file.write(result_list_sl[99][2])

file.write("]}, {\n")
file.write("name: 'J-AFINN + Asari', data: [")

for i in range(len(result_list_jafinn) - 1):
    if not care_zero:
        if float(result_list_jafinn[i][1]) > 0.0 and result_list_asari[i][0] == "positive":
            file.write(str(result_list_jafinn[i][1]) + ", ")
        elif float(result_list_jafinn[i][1]) < 0.0 and result_list_asari[i][0] == "negative":
            file.write(str(result_list_jafinn[i][1]) + ", ")
        elif float(result_list_jafinn[i][1]) == 0.0:
            file.write(str(result_list_jafinn[i][1]) + ", ")
        else:
            if result_list_asari[i][0] == "positive":
                file.write(str(float(result_list_asari[i][1]) * 7.524) + ", ")
            else:
                file.write(str(float(result_list_asari[i][1]) * -7.524) + ", ")
    else:
        if float(result_list_jafinn[i][1]) > 0.0 and result_list_asari[i][0] == "positive":
            file.write(str(result_list_jafinn[i][1]) + ", ")
        elif float(result_list_jafinn[i][1]) < 0.0 and result_list_asari[i][0] == "negative":
            file.write(str(result_list_jafinn[i][1]) + ", ")
        else:
            if result_list_asari[i][0] == "positive":
                file.write(str(float(result_list_asari[i][1]) * 7.524) + ", ")
            else:
                file.write(str(float(result_list_asari[i][1]) * -7.524) + ", ")
if not care_zero:
    if float(result_list_jafinn[99][1]) > 0.0 and result_list_asari[99] [0] == "positive":
        file.write(str(result_list_jafinn[99][1]))
    elif float(result_list_jafinn[99][1]) < 0.0 and result_list_asari[99][0] == "negative":
        file.write(str(result_list_jafinn[99][1]))
    elif float(result_list_jafinn[99][1]) == 0.0:
        file.write(str(result_list_jafinn[99][1]))
    else:
        if result_list_asari[99][0] == "positive":
            file.write(str(float(result_list_asari[99][1]) * 7.524))
        else:
            file.write(str(float(result_list_asari[99][1]) * -7.524))
else:
    if float(result_list_jafinn[99][1]) > 0.0 and result_list_asari[99] [0] == "positive":
        file.write(str(result_list_jafinn[99][1]))
    elif float(result_list_jafinn[99][1]) < 0.0 and result_list_asari[99][0] == "negative":
        file.write(str(result_list_jafinn[99][1]))
    else:
        if result_list_asari[99][0] == "positive":
            file.write(str(float(result_list_asari[99][1]) * 7.524))
        else:
            file.write(str(float(result_list_asari[99][1]) * -7.524))

file.write("]}]\n")
file.write("}\n")
file.write("$('#container').highcharts(data);\n")
file.write("</script>\n")
file.write("</div>\n")
file.write("</body>\n")
file.write("</html>\n")
file.close