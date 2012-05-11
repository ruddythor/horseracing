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
 print
 
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
 while bet>money:
  bet=input("You do not have that much cash. How much would you like to wager?\n>>")
 while bet<0:
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
 start1= ("-"*horsemovementvalues[h1])+">"
 start2= ("-"*horsemovementvalues[h2])+">"
 start3= ("-"*horsemovementvalues[h3])+">"
 start4= ("-"*horsemovementvalues[h4])+">"
 start5= ("-"*horsemovementvalues[h5])+">"
# h1go=h1+"\n"+"-"+h1go
# h2go=h2+"\n"+"-"+h2go
# h3go=h3+"\n"+"-"+h3go
# h4go=h4+"\n"+"-"+h4go
# h5go=h5+"\n"+"-"+h5go
 global actualwin
 actualwin="" 


 while len(h1go)<75 and len(h2go)<75 and len(h3go)<75 and len(h4go)<75 and len(h5go)<75:
   print h1+"\n"+h1go
   print h2+"\n"+h2go
   print h3+"\n"+h3go
   print h4+"\n"+h4go
   print h5+"\n"+h5go
   print
   print
   print
   print
   time.sleep(.15)
   h1go += start1
   h2go += start2
   h3go += start3
   h4go += start4
   h5go += start5

 winner = []
 if len(h1go)>=75 or len(h2go)>=75 or len(h3go)>=75 or len(h4go)>=75 or len(h5go)>=75:
  if len(h1go)>=75:
   winner.append(horse1)
  elif len(h2go)>=75:
   winner.append(horse2)
  elif len(h3go)>=75:
   winner.append(horse3)
  elif len(h4go)>=75:
   winner.append(horse4)
  elif len(h5go)>=75:
   winner.append(horse5)

 actualwin=random.choice(winner)
 actualwin=str.lower(actualwin)
 print " ********  %s won!! ********" % actualwin



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

