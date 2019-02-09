# tupple
# tup = ("Hello",1,3,4.5,Ture)
# tup2 =(10,20,30,False,Ture)
# tup_len=len(tup)
# tup3 = tup + tup2
# print(tup3)
#
# print(20 in tup3)
# lst =["jacky chan","chuck norris",]

#dictionary
dictionary= {
"key1": "value 1",
"key2": "Cool",
"theShortCut": "great"
}
dictionary['key1']="new value"
print(dictionary)

guess_number = int(input("choose your number,please!"))

print(guess_number)

right_answer =3
if guess_number == right_answer:
    print("super! ")
else:
    print("no, worg")
# 2 method
#else if statment
guess_number = int(input("choose your number,please!"))

print(guess_number)

right_answer =3
if guess_number == 1:
    print("no,no,higher ")
elif guess_number == 2:
    print("no, almost there")
elif guess_number == right_answer:
    print("yaya")
else:
    print("nnooo")
    # loop
    # whileloop
count=0
while count< 10:
    print(count)
    count += 1
        # count=count+1
        # count= count_1
print('done !')
         # for loop5
the_list=[1,2,34,5]
for a in the_list:
    if a in the_list[0:3]:
        print(a)
    else:
        print("naahh")
