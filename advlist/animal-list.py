#! /usr/bin/env python3

"""Advanced list of various animals,
    for the purpose of playing around
    with lists"""

def main():

    # create a list of animals, all of which are 3 letters long for some reason.
    animal_list = ["Fox", "Fly", "Ant", "Bee", "Cod", "Cat", "Dog", "Yak", "Cow", "Hen", "Koi", "Hog", "Jay", "Kit"]

    # print Bee (index 3) from the animal_list list
    print(animal_list[3])

    # print out animals in the 2nd, 5th, and 10th positions on the list, which should be: Ant, Cat, Koi
    #BROKEN, NEEDS FIX
    #print(animal_list[[2] [5] [10]])

main()
