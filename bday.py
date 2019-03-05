#helped by James in the CS Tutor
#Name: Ryan Ma
#Date: Feb 4, 2019
#Class: ECS36A; Homework 2 Question 3
#Description:The birthday problem asks how many people must be in a room so that the probability of two of them having the same birthday is 0.5.
# 41 many people are needed so that the probability of two of them with a birthday in common is over 0.9
# 23 people are needed to the probability of two of them with a birthday in common is over .5

import random
#function to check if the length of the list is equal to the duplicate list
def hasduplicates(l):
    return len(l)!= len(set(l))
#creates a list of random numbers
def onetest(count):
    l = []
    for x in range(count):
        random_number = random.randint(1,365)
        l.append(random_number)
    return(hasduplicates(l))
#finds the probability of how many duplicates there are
def probab(count,num):
    count_true = 0
    for x in range(num):
        if onetest(count) == True:
            count_true +=1
    return count_true/num
def main():
    count = 2
    return_value =0
    while return_value < 0.9:
        count = count + 1
        return_value = probab(count, num=5000)
        print("For", count,"people, the probablility of 2 birthdays is", return_value)

main()
