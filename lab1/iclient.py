# IServer: Insult Client

import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')

print("Adding: Negrata - "  + s.add_insult("Negrata") )
print("Adding: Sudaca - "   + s.add_insult("Sudaca") )
print("Adding: Panchito - " + s.add_insult("Panchito") )
print()

print("Insultos:")
for i, insult in enumerate(s.get_insults()):
    print(f" {i} -> {insult}")
print()

print("Insulto Random: " + s.insult_me())
print()

# Print list of available methods
print("Metodos:")
for i, method in enumerate(s.system.listMethods()):
    print(f" {i} -> {method}")
