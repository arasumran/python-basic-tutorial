import re
import sys
import os
def find_similar_string():
    list_string = ["heble", "hebele", "hebale", "hebile", "deneme"]
    for i in list_string:
        if re.search("heb[eai]le", i):
            print("\n", i)

    print("*******************************************************")
    print("list of values :", *list_string, sep=',')
    print ("\n[] keyword is works result :")


    a = ["23BH56","TY76Z","4Y7UZ","TYUDZ","34534"]

    for t in a:
        if re.match("[0-9]", t):# this option will match in a list with starting number a[0,2,4]--> will display in console
            print("\n", t)

    print("********************************************************")
    print("list of values :", *a, sep=',')
    print ("\n[] keyword is works result :")


    for i in a:
        """
        first [A-Z] means in the list string with start A-Z(uppercase is important)
        second[A-Z] means in the list string with second character will must A-Z
        third is must be number
        """
        if re.match("[A-Z][A-Z][0-9]", i):
            print("\n",i)
    print("**********************************************************")
    print("list of values :", *a, sep=',')
    print ("\n. keyword is works result :")



    for i in a:
        # . means character of sting can be start any type of character but only one character
        # [] -->  means seconds  character of string must be 0-9 or a-z(lowercase is important)l

        if re.match(".[0-9a-z]", i):
            print("\n", i)
    print("**********************************************************")

    for_star_regex = ["st", "sat", "saat", "saaat", "falanca"]
    # * means before intialize character 0 to n it will be for ex a character can be 0 or n times
    print("list of values :", *for_star_regex, sep=',')
    print ("\n* keyword is works result :")


    for i in for_star_regex:
        if re.match("sa*t", i):
            print("\n", i)

    print("**********************************************************")

    liste = ["ahmet", "mehmet", "met", "kezban"]
    # + means give me all string with ending met keyword but not give me if met only string just have to be keyword on string
    print("list of values :", *liste, sep=',')
    print ("\n+ keyword is works result :")


    for i in liste:
        if re.match(".+met",i):
            print("\n", i)

    print("**********************************************************")
    # ? means give me intialize  character 0 to 1 only
    print("list of values :", *for_star_regex, sep=',')
    print ("\n? keyword is works result :")

    for i in for_star_regex:
        if re.match("sa?t",i):
            print("\n", i)

    print("**********************************************************")




if __name__ == "__main__":

    find_similar_string()