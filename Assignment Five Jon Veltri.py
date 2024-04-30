# Jonathan Veltri
# Assignment 5 Lists

import random

def randomListCreation(intList):
    for x in range(0, 10):
        randomInt = random.randint(1,100)
        intList.append(randomInt)
    
def printStatements(intList):
    print(f"\nThe list is: {intList}")

    print("\nThe 1st, 5th, and 10th elements in the list are: ", end="")
    print(f"{intList[0]}, {intList[4]}, {intList[9]} \n")

    print("Every number at an even index are: ", end="")
    # I looked it up and it says 0 is an even number
    print(f"{intList[0]}, {intList[2]}, {intList[4]}, {intList[6]}, {intList[8]} \n")
    # These are all even indexs

    print("Every even number in the list is: ", end="")
    for number in intList:
        if number % 2 == 0:
            print(number, end=" ")


    print("\n\nThe smallest number in the list is: ", end="")
    smallest = 101
    count = 0
    indexsOfSmallest = []
    for number in intList:
        if number < smallest:
            indexsOfSmallest = []
            smallest = number
            indexsOfSmallest.append(count)
        elif number == smallest:
            indexsOfSmallest.append(count)
        count += 1
    print(smallest)
    print("And the index(s) of this number is: ", end="")
    for index in indexsOfSmallest:
        print(index, end=" ")
    print()


    print("\nThe biggest number in the list is: ", end="")
    biggest = 0
    count = 0
    indexsOfBiggest = []
    for number in intList:
        if number > biggest:
            indexsOfBiggest = []
            biggest = number
            indexsOfBiggest.append(count)
        elif number == biggest:
            indexsOfBiggest.append(count)
        count += 1
    print(biggest)
    print("And the index(s) of this number is: ", end="")
    for index in indexsOfBiggest:
        print(index, end=" ")
    print("\n")


    total = 0
    for number in intList:
        total += number
    average = total / 10
    biggerThanAverage = []
    count = 0
    countBigger = 0
    for number in intList:
        if number > average:
            countBigger += 1
            biggerThanAverage.append(number)
        count += 1
    print(f"There are {countBigger} number(s) greater than the average of {average}")
    print("They are: ", end="")
    for number in biggerThanAverage:
        print(number, end=" ")
    print("\n")


    add = True
    altSum = 0
    for number in intList:
        if add == True:
            altSum += number
            add = False
        else:
            altSum -= number
            add = True
    print(f"The alternating sum of all numbers is: {altSum}\n")

    reverseList = intList
    reverseList.reverse()
    print(f"The list in reversed order is: {reverseList}\n")
        
    descendList = intList
    descendList.sort()
    descendList.reverse()
    print(f"The list in descending order is: {descendList}\n")

def main():
    intList = []
    randomListCreation(intList)
    printStatements(intList)
    exit()

if __name__ == "__main__":
    main()