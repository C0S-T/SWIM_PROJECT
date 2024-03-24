import statistics
FN = "Darius-13-100m-Fly.txt"
FOLDER = 'swimdata/'

swimmer,age,meters,style = FN.removesuffix('.txt').split('-')
print(f'{swimmer},{age},{meters},{style}')
with open(FOLDER + FN, 'r') as f:
    data = f.read().strip().split(',')
convert_time=[]
for i in data:
    first = i
    mins,rest = first.split(':')
    seconds,hundredths = rest.split('.')
    convert_time.append((int(mins)*60*100) + (int(seconds)*100) + (int(hundredths)))
print(f'time : {convert_time}')
c= round((statistics.mean(convert_time))/100,2)
print(f'Mean time : {c}')
min_secs,hund = str(c).split('.')
min = int(min_secs) // 60
sec = int(min_secs) - (min*60)
average = str(min)+":"+str(sec)+"."+ hund
print(f'Average Time : {average}')
