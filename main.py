lis = [
    { "name" : "Nandini", "age" : 20},
    { "name" : "Manjeet", "age" : 20 },
    { "name" : "Nikhil" , "age" : 19 }
]
print("Printing the list using lambda function in descending order: ")
print(sorted(lis, key = lambda i:i["age"], reverse = True))