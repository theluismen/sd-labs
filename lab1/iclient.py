# IServer: Insult Client

import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.add_insult("negrata"))
print(s.add_insult("sudaca"))
print(s.add_insult("gei"))

print("Insultos:")
for i, insult in enumerate(s.get_insults()):
    print(f" {i} -> {insult}")

print(s.insult_me())

# Print list of available methods
print("Metodos:")
for i, method in enumerate(s.system.listMethods()):
    print(f" {i} -> {method}")
