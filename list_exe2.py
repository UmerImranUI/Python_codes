# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# city=input("Enter the city name: ")
# str(city)
# if city in india:
#     print("The",str(city),"is in india")
# elif city in pakistan:
#     print("The",str(city),"is in pakistan")
# elif city in bangladesh:
#     print("The",str(city),"is in bengladesh")
# else:
#     print("no")
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city1 = input("Enter the first city name: ")
city2 = input("Enter the second city name: ")
if city1 in pakistan and city2 in pakistan:
    print("Both are in pakistan")
elif city1 in india and city2 in india:
    print("Both are in india")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both are in bangladesh")
else:
    print("They don't belong to the same country")
