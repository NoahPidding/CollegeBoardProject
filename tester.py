# code here
import json

# some dictionaries
p1 = { "name":"Rivan", "age":17, "city":"San Diego", "Food":"Pizza"}
p2 = { "name":"Rini", "age":12, "city":"San Diego", "Food":"Pasta"}
p3 = { "name":"Deba", "age":53, "city":"New Delhi", "Food":"Burger" }
p4 = { "name":"Smita", "age":47, "city":"New Delhi", "Food":"Fries"}
p5 = { "name":"Rajit", "age":67, "city":"Tata", "Food":"Pizza"}

# a list of dictionaries
list_of_people = [p1, p2, p3, p4]
# write some code to Print List of people one by one
#print("List of people")
#print(type(list_of_family))
#print(list_of_family)
#for person in list_of_family:
print(person['name'] + "," + str(person['age']) + "," + person['city'])
print(person['food'])



# turn list to dictionary of people in your family
family={'memeber':list_of-family}
print("Dictionary of member")
print(type(family))
print(family)
#write some code to Print People from Dictionary




# turn dictionary to JSON (aka string)
json_people = json.dumps(list_of_family)
print("JSON")
for char in json-people:
    print(char,end="$")
print("JSON People #1")
print(type(json_people))
print(json_people)
# write ome code to Print People from Dictionary




# turn dictionary to JSON (aka string)
json_people = json.dumps(list_of_family)
# the result is a JSON file:
print("JSON People #2")
print(type(json_people))
print(json_people)
# write some code to unwind JSON using json.loads and print the people
# INSERT CODE HERE
print()


print("JSON to Python")
PythonList = json.loads(json_people)
for people in PythonList:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print(person['food'])