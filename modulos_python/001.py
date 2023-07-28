from datetime import datetime, timedelta






fmt = '%d/%m/%Y %H:%M:%S'


data_inicio = datetime.strptime('03/03/1993 20:00:00', fmt)
data_final = datetime.strptime('27/07/2023 15:43:00', fmt)
# delta = data_final - data_inicio

print(data_final.strftime('%m'), data_final.month)

