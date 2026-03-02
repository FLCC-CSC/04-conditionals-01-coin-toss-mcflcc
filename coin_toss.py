# FILE NAME - coin_toss.py

# NAME: Mike Cintron
# DATE: 3.1.2026
# BRIEF DESCRIPTION:  Code that creates a random number - if the number is 51 or greater - then tails - else heads



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

# Don't forget to import random!!!!!

import random

random_number = random.randint(1,100)

if random_number < 51:
    print("===== Coin Flipper =====")
    print("Heads")

else:
    print("===== Coin Flipper =====")
    print("Tails")








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 
Hardest part was getting the conditional correct for the if statement.






'''

########################################
#            ATTESTATION
########################################
'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 
[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[ x] I'm solid. Totally got it.
'''
