import random
import time
import string
print """







         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   ~~~~~~~~~   Welcome to the Joshtucky Derby!!   ~~~~~~~~~~
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~







                         Press enter
"""
go=raw_input("")
print """





The horses you can choose from are:
* The Long Mile * 
* Slimy the Salamander * 
* Jockey This * 
* Magenta Rage Machine * 
* You Shoulda Put a Ring on It*
"""




global money
money=1000
def thebet():
 horse1="The Long Mile"
 horse2="Slimy the Salamander"
 horse3="Jockey This"
 horse4="Magenta Rage Machine"
 horse5="You Shoulda Put a Ring on It"

 h1="The Long Mile"
 h2="Slimy the Salamander"
 h3="Jockey This"
 h4="Magenta Rage Machine"
 h5="You Shoulda Put a Ring on It"

 grouphigh=[]
 groupmid=[]
 grouplow=[]



#to be made into a function
# if h1moveval==6:
#  grouphigh.append(horse1)
# elif h1moveval==5:
#  groupmid.append(horse1)
# elif h1moveval==4:
#  grouplow.append(horse1)
# elif h1moveval==3:
#  grouplow.append(horse1)



 highodds=random.randint(4,4)
 medodds=random.randint(4,5)
 lowodds=random.randint(5,6)

 oddsoptions=[highodds, medodds, lowodds]

 h1moveval=random.choice(oddsoptions)
 if h1moveval==6:
  grouphigh.append(horse1)
 elif h1moveval==5:
  groupmid.append(horse1)
 elif h1moveval==4:
  grouplow.append(horse1)
 elif h1moveval==3:
  grouplow.append(horse1)
 h2moveval=random.choice(oddsoptions)
 if h2moveval==6:
  grouphigh.append(horse2)
 elif h2moveval==5:
  groupmid.append(horse2)
 elif h2moveval==4:
  grouplow.append(horse2)
 elif h2moveval==3:
  grouplow.append(horse2)
 h3moveval=random.choice(oddsoptions)
 if h3moveval==6:
  grouphigh.append(horse3)
 elif h3moveval==5:
  groupmid.append(horse3)
 elif h3moveval==4:
  grouplow.append(horse3)
 elif h3moveval==3:
  grouplow.append(horse3)
 h4moveval=random.choice(oddsoptions)
 if h4moveval==6:
  grouphigh.append(horse4)
 elif h4moveval==5:
  groupmid.append(horse4)
 elif h4moveval==4:
  grouplow.append(horse4)
 elif h4moveval==3:
  grouplow.append(horse4)
 h5moveval=random.choice(oddsoptions)
 if h5moveval==6:
  grouphigh.append(horse5)
 elif h5moveval==5:
  groupmid.append(horse5)
 elif h5moveval==4:
  grouplow.append(horse5)
 elif h5moveval==3:
  grouplow.append(horse5)

 print "These are slow movers:"
 for x in grouplow:
  print "\t"+x
 print
 print "These are mid movers:"
 for x in groupmid:
  print "\t"+x
 print
 print "These are high movers:"
 for x in grouphigh:
  print "\t"+x
 horsesmove={h1moveval:horse1, h2moveval:horse2, h3moveval:horse3, h4moveval:horse4, h5moveval:horse5}
 movevalues=[h1moveval, h2moveval, h3moveval, h4moveval, h5moveval]
 movevalues.sort()

 

 
 global money
 global pickahorse
 pickahorse=raw_input("Pick a horse to win.\n>>")
 print
 print "You have up to $%i to wager." % money
 global bet
 bet=input("How much would you like to wager?\n>>")
 if bet>money:
  bet=input("You do not have that much cash. How much would you like to wager?\n>>")
 elif bet<0:
  bet=input("You cannot bet that amount. How much would you like to wager?\n>>")
 print
 print
 print
 print

 horsemovementvalues={h1:h1moveval, h2:h2moveval, h3:h3moveval, h4:h4moveval, h5:h5moveval}

 #def rndm_move_modifier():
 # x=random.randint(1,10)
 # 
 # after index reaches X
 # movevalue goes to Y
 print
 print
 h1go= ("-"*horsemovementvalues[h1])+">"
 h2go= ("-"*horsemovementvalues[h2])+">"
 h3go= ("-"*horsemovementvalues[h3])+">"
 h4go= ("-"*horsemovementvalues[h4])+">"
 h5go= ("-"*horsemovementvalues[h5])+">"
 h1=h1+"\n"+"-"+h1go
 h2=h2+"\n"+"-"+h2go
 h3=h3+"\n"+"-"+h3go
 h4=h4+"\n"+"-"+h4go
 h5=h5+"\n"+"-"+h5go
 global actualwin
 actualwin="" 


 while len(h1)<95 and len(h2)<95 and len(h3)<95 and len(h4)<95 and len(h5)<95:
   print h1
   print h2
   print h3
   print h4
   print h5
   print
   print
   print
   print
   time.sleep(.15)
   h1 += h1go
   h2 += h2go
   h3 += h3go
   h4 += h4go
   h5 += h5go 

 winner = []
 if len(h1)>=95 or len(h2)>=95 or len(h3)>=95 or len(h4)>=95 or len(h5)>=95:
  if len(h1)>=95:
   winner.append(horse1)
  elif len(h2)>=95:
   winner.append(horse2)
  elif len(h3)>=95:
   winner.append(horse3)
  elif len(h4)>=95:
   winner.append(horse4)
  elif len(h5)>=95:
   winner.append(horse5)

 actualwin=random.choice(winner)
 actualwin=str.lower(actualwin)
 print " ****  %s won!! ****" % actualwin



 print
 #print horsemovementvalues
 print
 print
 print
 print
 print


 if pickahorse==actualwin:
  money=money+bet
 elif pickahorse!=actualwin:
  money=money-bet
 print "You now have $%i" %money 


while money >0:
 thebet()

