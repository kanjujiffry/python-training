# website_1=["Facebook","mmanitha","123"]
# website_2=["Instagram","mmanitha1","456"]
# website_3=["Linkedin","mmanitha2","789"]
# website_4=["Gmail","mmanitha3","1011"]
#
# count =True
# while count:
#     choice=int(input("what website you want to see?\n1.Facebook\n2.Instagram\n3.Linkedin\n4.Gmail\n"))
#     if choice == 1:
#         print("Facebook username is", website_1[1])
#         print("Facebook Password is", website_1[2])
#     elif choice == 2:
#         print("Instagram username is", website_2[1])
#         print("Instagram password is", website_2[2])
#     elif choice == 3:
#         print("Linkedin username is", website_3[1])
#         print("Linkedin password is", website_3[2])
#     elif choice == 4:
#         print("Gmail username is", website_4[1])
#         print("Gmail password is", website_4[2])
#
#     again=str(input("Do you wish to continue? Y/N\n"))
#     if again in ("Y"):
#         count =True
#     elif again == "N":
#         print("")
#         break
# #
web1 ="facebook"
acc1 ="theshortcut"
pass1 ="12345"

web2 ="Twitter"
acc2= "thescut"
pass2="5432"
ctn =True
while ctn:
    print("what website's account and password do you want to see?")
    print("1.Facebook")
    print("2 twitter")
    answer1= int(input(">> "))
    if answer1 ==1:
        print("this the facebook account:{}".format(acc1))
        print("this the facebook account:{}".format(pass1))
    elif answer1 ==1:
        print("this the facebook account:{}".format(acc2))
        print("this the facebook account:{}".format(pass2))
    else:
        print("there is no such thing,read again")
    wish =input("Do you wish to continue? y/n")
    if wish.lower()== 'yes' or wish.lower() =='y':
        ctn =True
    else:
        ctn=False
        break
