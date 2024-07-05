from prettytable import PrettyTable

table1 = PrettyTable()

#adding by columns

table1.add_column("Pokemon Name",
["Pikachu","Squirtle","Charmander"])
table1.add_column("Type", ["Electric", "Water", "Fire"])

print(table1)