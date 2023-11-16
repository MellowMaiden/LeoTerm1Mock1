print("Hello this is a Mock exam for check the student score in each subject and overall")

print("#####TERM 1#####")
AES1=int(input("Tell me the AES score:"))
Math1=int(input("Tell me the Math1 score:"))
Physics1=int(input("Tell me the Physics 1 score:"))
Computer_programming1=int(input("Tell me the CS score"))
if AES1 >100 or AES1<0 or Math1>100 or Math1<0 or Physics1 >100 or Physics1 <0 or Computer_programming1 >100 or Computer_programming1 <0:
#This is to sure the input number is not too big or too small
    print("That is not a invaild input.")
    quit()
elif AES1 < 40 or Math1 <40 or Physics1<40 or Computer_programming1<40:
#This is to sure each subject all higher than 40 because you must get at least 40 in each subject
    print("You must get at least 40% in each subject")
    quit()
else:
    print("You all subject pass the exam.")

overall1 =int((AES1+Math1+Physics1+Computer_programming1)/4)
#This is to calculate the overall score
print (f"Your Term1 overall score is: {overall1}")
if overall1 < 40:
#If over all smaller than 40 you won't pass
    print("You overall at least 40%")
    quit()
elif overall1==100:
    print("you are smart! 100 in everything!")
elif overall1>60:
    print("you are good at term 1")

print("#####TERM 2#####")
AES2=int(input("Tell me the AES score:"))
Math2=int(input("Tell me the Math2 score:"))
Physics2=int(input("Tell me the Physics 2 score:"))
Computer_programming2=int(input("Tell me the CS2 score"))
if AES1 >100 or AES2<0 or Math2>100 or Math2<0 or Physics2 >100 or Physics2 <0 or Computer_programming2 >100 or Computer_programming2 <0:
    print("That is not a invaild input.")
    quit()
elif AES2 < 40 or Math2 <40 or Physics2<40 or Computer_programming2<40:
    print("You must get at least 40% in each subject")
    quit()
else:
    print("You all subject pass the exam.")
overall2=int((AES2+Math2+Physics2+Computer_programming2)/4)
print (f"Your Term2 overall score is: {overall2}")
if overall2 < 40:
    print("You overall at least 40%")
    quit()
if overall2==100:
    print("you are smart! 100 in everything!")
elif overall2>60:
    print("you are good at term 2")

print("#####TERM 3#####")
AES3=int(input("Tell me the AES3 score:"))
Math3=int(input("Tell me the Math3 score:"))
Physics3=int(input("Tell me the Physics 3 score:"))
Computer_programming3=int(input("Tell me the CS 3 score"))
if AES3 >100 or AES3<0 or Math3>100 or Math3<0 or Physics3 >100 or Physics3 <0 or Computer_programming3 >100 or Computer_programming3 <0:
    print("That is not a invaild input.")
    quit()
elif AES3 < 40 or Math3 <40 or Physics3<40 or Computer_programming3<40:
    print("You must get at least 40% in each subject")
    quit()
elif AES3< 60:
    print("AES3 must get 60")
    quit()
elif (Math3+Math2)/2<65:
    print("Math2 and Math3 average must get 65")
    quit()
else:
    print("You all subject pass the exam.")
overall3=int((AES2+Math2+Physics2+Computer_programming2)/4)
print (f"Your Term3 overall score is: {overall3}")
if overall3 < 40:
    print("You overall at least 40%")
    quit()
if overall3==100:
    print("Well dove you PROGRESS! And you are smart! 100 in everything!")
elif overall3>60:
    print("Well done you PROGRESS!")
quit()



