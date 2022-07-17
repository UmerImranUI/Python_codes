d={'China':143, 'India':136, 'USA':32, 'Pakistan':21}
print1=input("do you want to print,add,remove? ")


if print1 =='print':
    for key in d:
        print("Country is: ", key, "population :", d[key],"crore")

elif print1 == 'add':
    add = input("Do you want to add the country? then type the name or type no ")

    for find in d:
        if add == find:
            print("It exists")
        else:

            population=int(input("Enter the population"))
            d[add]=population
            break
    for key in d:
        print("Country is: ", key, "population :", d[key], "crore")
elif print1 == 'remove':
    remove = input("which country you want to remove?")
    for find2 in d:
        if remove==find2:
            del d[remove]
            for key in d:
                print("Country is: ", key, "population :", d[key], "crore")
            break
elif print1 == 'query':
    country=input("which country?")
    for find3 in d:
        if country==find3:
            print(d[country],"crore")