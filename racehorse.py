import random
import time
import string
print """







         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ~~~~~~~~~~   Welcome to the Joshtucky Derby!!   ~~~~~~~~~~
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~







                         Press enter
"""
go=raw_input("")
print """





The horses you can choose from are:
\t* The Long Mile * 
\t* Slimy the Salamander * 
\t* Jockey This * 
\t* Magenta Rage Machine * 
\t* You Shoulda Put a Ring on It*
"""




global money
money=1000
def horsegenerating():
 global horse1
 global horse2
 global horse3
 global horse4
 global horse5
 global allhorses
 allhorses=("the long mile", "slimy the salamander", "jockey this", "magenta rage machine", "you shoulda put a ring on it")

# print allhorses
 horse1="The Long Mile"
 horse2="Slimy the Salamander"
 horse3="Jockey This"
 horse4="Magenta Rage Machine"
 horse5="You Shoulda Put a Ring on It"
 global grouplow, groupmid, grouphigh
 grouphigh=[]
 groupmid=[]
 grouplow=[]
 def groupbymoverate(x, y):
  if x==6:
   grouphigh.append(y)
  elif x==5:
   groupmid.append(y)
  elif x==4:
   grouplow.append(y)
  elif x==3:
   grouplow.append(y)

#this defines the possible movement values horses can have
 slowhorse=random.randint(3,4)
 midhorse=random.randint(3,5)
 fasthorse=random.randint(4,6)

#this just selects the move rate for each horse, then
#groups the horses by how fast they move. 
#the grouping allows you to make an informed bet
 oddsoptions=[slowhorse, midhorse, fasthorse]

 horse1moveval=random.choice(oddsoptions)
 groupbymoverate(horse1moveval, horse1)
 horse2moveval=random.choice(oddsoptions)
 groupbymoverate(horse2moveval, horse2)
 horse3moveval=random.choice(oddsoptions)
 groupbymoverate(horse3moveval, horse3)
 horse4moveval=random.choice(oddsoptions)
 groupbymoverate(horse4moveval, horse4)
 horse5moveval=random.choice(oddsoptions)
 groupbymoverate(horse5moveval, horse5)

 print "These horses pay 4:1 odds:"
 for x in grouplow:
  print "\t"+x
 print
 print "These horses pay 3:1 odds:"
 for x in groupmid:
  print "\t"+x
 print
 print "These horses pay 2:1 odds:"
 for x in grouphigh:
  print "\t"+x
 print
 
 horsesmove={horse1moveval:horse1, horse2moveval:horse2, horse3moveval:horse3, horse4moveval:horse4, horse5moveval:horse5}
 movevalues=[horse1moveval, horse2moveval, horse3moveval, horse4moveval, horse5moveval]
 movevalues.sort()
 global horsemovementvalues
 horsemovementvalues={horse1:horse1moveval, horse2:horse2moveval, horse3:horse3moveval, horse4:horse4moveval, horse5:horse5moveval}


def makeyourbets():
 global money
 global pickahorse
 pickahorse=raw_input("Pick a horse to win.\n>>")
 pickahorse=str.lower(pickahorse)
 while pickahorse not in allhorses:
  pickahorse=raw_input("Pick a horse to win.\n>>")
  pickahorse=str.lower(pickahorse)
 
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

def therace():
 #def rndm_move_modifier():
 # x=random.randint(1,10)
 # 
 # after index reaches X
 # movevalue goes to Y
 global horsemovementvalues
 global horse1
 global horse2
 global horse3
 global horse4
 global horse5
 print
 print
 horse1go= ("-"*horsemovementvalues[horse1])+">"
 horse2go= ("-"*horsemovementvalues[horse2])+">"
 horse3go= ("-"*horsemovementvalues[horse3])+">"
 horse4go= ("-"*horsemovementvalues[horse4])+">"
 horse5go= ("-"*horsemovementvalues[horse5])+">"
 start1= ("-"*horsemovementvalues[horse1])+">"
 start2= ("-"*horsemovementvalues[horse2])+">"
 start3= ("-"*horsemovementvalues[horse3])+">"
 start4= ("-"*horsemovementvalues[horse4])+">"
 start5= ("-"*horsemovementvalues[horse5])+">"

 global actualwin
 actualwin="" 

 while len(horse1go)<75 and len(horse2go)<75 and len(horse3go)<75 and len(horse4go)<75 and len(horse5go)<75:
   print horse1+"\n"+horse1go
   print horse2+"\n"+horse2go
   print horse3+"\n"+horse3go
   print horse4+"\n"+horse4go
   print horse5+"\n"+horse5go
   print
   print
   print
   print
   time.sleep(.15)
   horse1go += start1
   horse2go += start2
   horse3go += start3
   horse4go += start4
   horse5go += start5

 winner = []
 if len(horse1go)>=75 or len(horse2go)>=75 or len(horse3go)>=75 or len(horse4go)>=75 or len(horse5go)>=75:
  if len(horse1go)>=75:
   winner.append(horse1)
  elif len(horse2go)>=75:
   winner.append(horse2)
  elif len(horse3go)>=75:
   winner.append(horse3)
  elif len(horse4go)>=75:
   winner.append(horse4)
  elif len(horse5go)>=75:
   winner.append(horse5)

 actualwin=random.choice(winner)
 print " ********  %s won!! ********" % actualwin
 actualwin=str.lower(actualwin)

 print "\n\n\n\n"
 global grouplow, groupmid, grouphigh

 global money
# print grouplow, groupmid, grouphigh, "THESE ARE THE GROUPS"
 grouplow=[x.lower() for x in grouplow]
 groupmid=[x.lower() for x in groupmid]
 grouphigh=[x.lower() for x in grouphigh]
# print pickahorse, actualwin
 if pickahorse==actualwin and pickahorse in grouplow:
  money=money+bet+bet+bet
 elif pickahorse==actualwin and pickahorse in groupmid:
  money=money+bet+bet
 elif pickahorse==actualwin and pickahorse in grouphigh:
  money=money+bet
 elif pickahorse!=actualwin:
  money=money-bet
 else:
  print "SOmething went wrong jim"
 print "You now have $%i" %money 


while money >0:
 horsegenerating()
 makeyourbets()
 therace()

