#Name: Ryan Ma
#Date: Feb 4, 2019
#Class: ECS36A; Homework 2 Question 3
#Description:to calculate the atomic weight of molecules.
import re
import math
#dictionary function from the file atomicweights.txt
def dictElements():
    inFile = open("atomic_weights.txt")

    dict = {}
    for line in inFile:
        line.strip()
        line = line.split()
        name_element =line.pop(2)
        value = line[0]
        abbrev = line[1]
        dict[abbrev] = value
    return dict

def split_molecule(chemical_input):
    num_element= []
    new_name_element = []
    Dictionary1 = dictElements()
    #using re to split the input at each element and number ex. 'Ca4H3' = [Ca,4,H,3]
    element = re.findall('[A-Z][a-z]?|[0-9]+', chemical_input)
    # Hello [He,llo] | PoHe [Po,He]
    # if len(chemical_input) != len(element):
    #     invalid = "Invalid!"
    #     return (invalid)

    for x in range(len(element)):
        #if there is no number after the element append 1
        if not element[x].isdigit():
            if x >= len(element)-1:
                num_element.append('1')
        #else if there is a number, append that already existing number
            else:
                if element[x+1].isdigit():
                    num_element.append(element[x+1])
        #if there is not a number add one
                else:
                    num_element.append('1')
    #check the list element and append a new list of only elements [Ca,4,H,3] = [Ca,H]
    for z in element:
        if (not z.isdigit()):
            new_name_element.append(z)

        # elif z != Dictionary1.keys():
        #     invalid = "Invalid!"
        #     return (invalid)

    #returns two new lists, one with the number of elements and the elements themselves
    return num_element,new_name_element

def main():
    while True:
        try:
            chemical_input = input("Chemical composition?")
        except EOFError:
            print("\nSee ya later!")
            break
        except KeyboardInterrupt:
            print("\nSee ya later!")
            break
        Dictionary1 = dictElements()
        bool_True = True
        input_checking = re.findall("[A-Za-z][a-z]?",chemical_input)
        #we check the user input and see if it matches the keys in the dictionary
        for u in input_checking:
            if u not in Dictionary1.keys():
                bool_True = False
                print("Invalid chemical formula")
                break
        if bool_True == True:
            #initialzing all my lists here
            name_element = split_molecule(chemical_input)
            num_element = name_element[0]
            new_name_element = name_element[1]
            element_list = []
            values_list = []
            newvalues_list = []
            tempL = []
    #check the user input and see if it matches a key in the dictionary and return that key to a list
            for element in new_name_element:
                for keys in Dictionary1:
                    if element == keys:
                        element_list.append(element)



    #finds the values of the keys found in the dictionary
            for elements in element_list:
                values_list.append(Dictionary1[elements])

    #makes a new list of numbers that the user entered next to their element ex. Ca2H3 == [2,3]
            number_list = num_element
            number_list= list(map(float,num_element))
    #converts all the values to floats and appends it to a new list
            for x in values_list:
                y = float(x)
                newvalues_list.append(y)
    #multiply the numbers from both lists into a new list called tempL
            for i in range(len(newvalues_list)):
                tempL.append(number_list[i] * newvalues_list[i])

            molecular_weight = sum(tempL)
    #error handled
            if molecular_weight == 0:
                print("This is not a valid chemical formula")
            else:
                print("%.2f" % float(molecular_weight))
main()
