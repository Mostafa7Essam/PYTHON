#the following dict contains the amount of fruits and the earned money initially will be zero 
quantities= {
    "apple": 0,
    "orange": 0,
    "banana": 0,
    "money": 0
}


# when the system start ask to fill the quantites of fruits  
apple_q=input("what is the amount of apples : ")
apple_q=int(apple_q)
quantities["apple"]=apple_q
orang_q=input("what is the amount of orangs : ")
orang_q=int(orang_q)
quantities["orange"]=orang_q
banana_q=input("what is the amount of bananas : ")
banana_q= int(banana_q)
quantities["banana"]=banana_q

while 1:
 # asking the user to select the operation which be needed by select value between 1 and 8
 x =input("ENTR 1 FOR SELLING APPLE,2 FOR SELLING ORANGE ,3 FOR SELLING BANANA,4 FOR PRINTING THE AMOUNT OF FRUITS  AND MONEY \n 5 TO CHANGE QUANATITY OF APPLE,6 TO CHANGE QUANATITY OF ORANGE,7 TO CHANGE QUANATITY OF BANANA ,8 TO CHANGE MONEY VALUE:  ")
 x=int(x)

 #if user selct selling apple he must inter the amount of units and price of the unit 
 if x == 1:
       y =  input("what is the quantitiy")
       y=int(y)
       z=input("what is the price of the unit")
       z=int(z)
       quantities["apple"] -= 1
       quantities["money"] += y*z

 #if user selct selling orange he must inter the amount of units and price of the unit   
 elif x==2 :
       y =  input("what is the quantitiy")
       y=int(y)
       z=input("what is the price of the unit")
       z=int(z)
       quantities["orange"] -= 1
       quantities["money"] += y*z
 #if user selct selling banana he must inter the amount of units and price of the unit   
 elif x==3 :
       y =  input("what is the quantitiy")
       y=int(y)
       z=input("what is the price of the unit")
       z=int(z)
       quantities["banana"] -= 1
       quantities["money"] += y*z    
   #if user select printing quantities and money 
 elif x==4 :
       print(quantities)
   #if user select changing quantitiy of apple   
 elif x==5 :
       apple_q=input("what is the amount of apples")
       apple_q=int(apple_q)
       quantities["apple"]=apple_q
   #if user select changing quantitiy of orange  
 elif x== 6:
      orang_q=input("what is the amount of orangs")
      orang_q=int(orang_q)
      quantities["orange"]=orang_q 
   #if user select changing quantitiy of banana
 elif x== 7:  
      banana_q=input("what is the amount of bananas")
      banana_q= int(banana_q)
      quantities["banana"]=banana_q
 elif x== 8:
      n=input("ENTRE THE VALUE")
      n=int(n)
      quantities["money"]=n
  #incase of wrong value from the user    
 else:
      print("wrong value")
