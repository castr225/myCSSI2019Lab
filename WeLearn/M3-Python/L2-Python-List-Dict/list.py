students = ["Alice", "javi", "Damien"]
students.append("Delilah")
print(students)

students = ["Alice", "javi", "Damien"]
students.insert(1, "Zoe")
print(students)

students = ["Alice", "javi", "Damien", "Javi"]
students.remove("Javi")
print(students)

#my_list.insert(index, element)

smith_siblings = ["Emily", "Monique", "Giovanni", "Kevin", "Kyle", "Gabby", "Dominique"]
for name in smith_siblings:
    print(name + " Smith")

print(len(smith_siblings))

smith_siblings = ["Emily", "Monique", "Giovanni", "Brianna", "Javi"]
for index in range(len(smith_siblings)):
    smith_siblings[index] = smith_siblings[index] + " Smith"

print(smith_siblings)

#my_list[start:end:step]
#step refers to how many items the program skips
names = ["Rickon", "Bran", "Arya", "Sansa", "Jon", "Robb"]
print(names[::-1])
print(names[4:2:-1])
print(names[::2])



superheroes = ["Captain Marvel", "Wonder Woman", "Storm", "Kamala Khan", "Bumblebee", "Jessica Jones"]
print(superheroes)
demoted_hero = str(raw_input("What superhero do you want to eliminate from the top 5? "))
if demoted_hero in superheroes:
    superheroes.remove(demoted_hero)
    print("Top 5 heroes:", superheroes)
else:
    print("Hero not found.")


state1 = 'New York'
abbv1 = 'NY'
state2 = 'California'
abbv2 = 'CA'
state3 = 'Texas'
abbv3 = 'TX'
print(abbv2, "is short for", state2)

labeled_states = ['NY: New York', 'CA: California', 'TX: Texas']
# to see California
print(labeled_states[1])

states = ['New York', 'California', 'Texas']
abbvs = ['NY', 'CA', 'TX']
# to see California
print(abbvs[1] + "is short for" + states[1])

states = {"NY": "New York", "CA": "California", "TX": "Texas"}
states = {
    "NY": "New York",
    "CA": "California",
    "TX": "Texas"
}
