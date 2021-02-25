import json

# some dictionaries
p1 = { "name":"Haridas", "age":"54", "city":"San Diego", "Drink":"Coffee"}
p2 = { "name":"Asha", "age":"45", "city":"San Diego", "Drink":"Milk"}
p3 = { "name":"Nihar", "age":"17", "city":"San Diego", "Drink":"Water"}
p4 = { "name":"Narayanan", "age":"76", "city":"Palakkad", "Drink":"Green tea"}
p5 = {"name":"Roopi", "age":"66", "city":"Thrissur", "Drink":"Tea"}

# a list of dictionaries
list_of_family = [p1, p2, p3, p4,p5]
# write some code to Print List of people one by one
#print("List of people")
#print(type(list_of_family))
#print(list_of_family)
#for person in list_of_family:
#print(person['name'] + "," + str(person['age']) + "," + person['city'])
#print()



# turn list to dictionary of people in a family
family = {'family': list_of_family}
print("Dictionary of member")
List = family["family"]
for member in List:
    print("age" + ": " + member["age"] + " ,name" + ": " + member["name"] + " ,city" + ": " + member["city"]+ " ,Drink" + ": " + member["Drink"]  )
    #print(members["name"] + " , " + members["age"]+ " , " + members["city"]+ " , " + members["Drink"])

# write some code to Print People from Dictionary




# turn dictionary to JSON (aka string)
json_people = json.dumps(list_of_family)
print("Dictionary to JSON")
for char in json_people:
    print(char,end="#")
# write some code to print a space between each character of JSON
# hint use print(char, end ="-")
# INSERT CODE HERE




# turn dictionary to JSON, this can be sent via a browser
# write some code to unwind JSON using json.loads and print the people
# INSERT CODE HERE
print("JSON to Python")
print("JSON to Python")
PythonList = {"family": json.loads(json_people)}
NewList = {"Grandparents":[PythonList["family"][3],PythonList["family"][4]], "Parents":[PythonList["family"][1],PythonList["family"][2]]}
print(NewList)

for people in PythonList["family"]:
    print(people['name'] + "," + str(people['age']) + "," + people['city'])
print()

