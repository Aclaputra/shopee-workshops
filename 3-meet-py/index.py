# list
x = [['a', 'b'],['c', 'd'],['e', 'f']]
print(x)

# tuple
k = (1,2,3)
city_info = ('Singapore', 'Indonesia', 'India')
print(k)

# list indexes & slicing
test_list = ['a','b','c','d']
print(test_list[0])
print(test_list[1:3])

# data structures - list
test_list.append('e')

# dictionary
user_ages = {'alice': 21, 'bob': 23}
print(user_ages)
bpb_age = user_ages['bob']

# setting new key
user_ages['dave'] = 25

# adding elemnets
test_list.append({'alice': 22})
print(test_list)

# if else
food = 'spam'
if food == 'spam':
    print ('Ummm, my favorite!')
else:
    print("No, I won't have it. I want spam!")

# loops for
friend_list = ['Margot', 'acla', 'Prisila']

for friend in friend_list:
    invitation = 'Hi %s. Please come to my party on Saturday!' % friend
    print(invitation)

# looping over dict
friend_availability = {'Margot': True, 'Acla': True}
try:
    my_availability = friend_availability['Acla']
except KeyError:
    friend_availability['Acla'] = False
print(friend_availability)

# looping while
name = 'Acla'
chances = 5
while True:
    guess = input('Try guess my name! [Chances left: %d]' % chances)
    if guess == name:
        print('Congrats!')
        break
    chances -= 1
    if chances == 0:
        print('Maximum tries exceeded. Sorry!')
        break