#creating a dictionary to each user include the data of the user
user1={
  "ID":"MOSTAFA",
  "Password" : 1245369,
  "MONEY" :60000000
}
user2={
  "ID":"AHMED ",
  "Password" : 199829,
  "MONEY" :50000000
}
user3={
  "ID":"AMR ",
  "Password" : 445369,
  "MONEY" :40000000
}
user4={
  "ID":"SAAD ",
  "Password" : 148569,
  "MONEY" :650000000
}
while 1:
 x=input("ENTR 1 FOR DEPOSITE , ENTRE 2 FOR WITHDRAW")
 x=int(x)
 if x==1 :
    id=input("Entre your ID : ")
    if id ==  "MOSTAFA" :
      password=input("Entr your password : ")
      password=int(password)
      if password == 1245369 :
         value=input("what is the value you need to deposite : ")
         value =float(value)
         user1["MONEY"]+=value
      else:
         print("wronge password")
    elif id ==  "AMR" :
      password=input("Entr your password : ")
      password=int(password)
      if password == 445369 :
         value=input("what is the value you need to deposite : ")
         value =float(value)
         user2["MONEY"]+=value
      else:
         print("wronge password")     
    elif id ==  "SAAD" :
      password=input("Entr your password : ")
      password=int(password)
      if password == 148569 :
         value=input("what is the value you need to deposite : ")
         value =float(value)
         user3["MONEY"]+=value
      else:
         print("wronge password")       
 elif x==2 :
    id=input("Entre your ID : ")
    if id ==  "MOSTAFA" :
      password=input("Entr your password : ")
      password=int(password)
      if password == 1245369 :
         value=input("what is the value you need to withdraw : ")
         value =float(value)
         if value <user1["MONEY"] : 
            user1["MONEY"]-=value
         else:
            print("no Enough money in your account ")   
      else:
         print("wronge password")
    elif id ==  "AMR" :
      password=input("Entr your password : ")
      password=int(password)
      if password == 445369 :
         value=input("what is the value you need to withdraw : ")
         value =float(value)
         if value <user2["MONEY"] : 
          user2["MONEY"]-=value
         else:
           print("no Enough money in your account ")  
         
      else:
         print("wronge password")     
    elif id ==  "SAAD" :
      password=input("Entr your password : ")
      password=int(password)
      if password == 148569 :
         value=input("what is the value you need to withdraw : ")
         value =float(value)
         if value <user3["MONEY"] :
          user3["MONEY"]-=value
         else:
             print("no Enough money in your account ")
      else:
         print("wronge password")                