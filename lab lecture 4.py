#convert these objects!

#1
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]
#single list comprehension that turns 2 into 1, eliminates 3, turns 4 into 2, 
#remove inner list, turn 6 into 3, turn 8 into 4, and eliminate 9
#only two operations to make this happen in a single list comprehension
end_list = [item//2 for sublist in start_list for item in sublist if item % 2 == 0]
print(end_list)

#2
import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime(1999, 2, 23),
#              'Sarah':datetime(2001, 9, 1),
#              'Zach': datetime(2005, 8, 8)}
#turn date strings into datetime objects
#using single dictionary comprehension
end_dict = {key.capitalize():datetime.strptime(value, "%m/%d/%Y") for key, value in start_dict.items()}
print(end_dict)

