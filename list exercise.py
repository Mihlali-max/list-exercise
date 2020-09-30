#Comparing two lists

def find_common_data(ages,ages1):
    for x in ages:
        for y in ages1:
            if x == y:
                return True
ages =[2,12,12,14,15,16,16,17,18,14,20,20]
ages1 =[2,4,12,14,15,16,16,17,18,14,20,20]

if find_common_data(ages,ages1):
    print("Have common data")
else:
    print("nothing in common")

ag=set(ages)&set(ages1)
print(ag)


