# d= {"name":"ABC","email":"abc@gmail.com"}

# for i in d:
#     print(i)

# for k, i in d.items():
#     print(f"key is {k} and value is {i}")


phonebook = {
    "Dipesh":9803643491,
    "surya":9846517546,
    "sandeep":9845613248,
    "ashish":9840033688
}

for i in phonebook:
    print(i)

print(phonebook.get("surya"))