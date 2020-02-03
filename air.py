#
with open('air.txt') as file_air:
    lines = file_air.readlines()
str_ = ''
list_str = []
for line in lines:
    str_ += line.strip().replace('.', '').replace(',', '').replace(' ', '').lower()

for i in str_:
    list_str.append(i)
 
list_d = {}.fromkeys(list_str, 0)
for a in list_str:
    list_d[a] += 1
max_value = max(list_d.values())
final_dict = {k:v for k, v in list_d.items() if v == max_value}
print(list_d)
print('Max Value: ')
print(final_dict)

file_air.close()