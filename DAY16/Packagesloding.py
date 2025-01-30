import prettytable
table = prettytable.PrettyTable()

table.field_names=['pokemon Name' , 'Type']
table.add_row(["Pikachu", 'Electric'])
table.add_row(["Squritle", 'Water'])
table.add_row(["Charmander", 'Fire'])
table.align = "l"
print(table)