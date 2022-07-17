# exp=[1234,2345,6753,1346,7456]
# total=0
# for i in exp:
#     total=total+i
# print(total)
# exp=[1233,5363,1234,346,3245]
# total=0
# for i in range(len(exp)):
#     print("Month is",(i+1),"Expense:",exp[i])
#     total=total+exp[i]
# print("The total is", total)
key_location='chair'
location=['bedroom','drawing room','chair','garage']
for i in location:
    if i==key_location:
        print("found at",i)
    else:
        print("not found")