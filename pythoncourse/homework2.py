leave_home = 6*60+52
easy_pace = (8*60)+15
print(easy_pace)
tempo = ((7*60)+12)*3
print(tempo)
get_home = easy_pace*2+tempo
print( get_home/60)
total_time=get_home/60

get_home_hour=(leave_home+ total_time)/60
print('%d' %get_home_hour)
get_home_min=(leave_home+ total_time)%60
print('%d.%d' %(get_home_hour,get_home_min))
