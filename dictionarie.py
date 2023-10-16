# phone_no = {
#     "ram": '12345',
#     "shyam": '5425',
#     "ram": "3232323"
# }
#
# print(phone_no)
#
#
# phone_no = dict({
#     "ram": '12345',
#     "shyam": '5425',
#     "ram": "3232323"
# })
# print(phone_no)
#
# phone_no = dict([("ram",'12345'),("shyam",'5425'),("ram","3232323")])
# print(phone_no)

phone_no = {
    "ram": '12345',
    "shyam": '5425',
    "ram": "3232323"
}

print(phone_no)

phone_no["ram"] = "1111"
print(phone_no)




emp = {
    "ram":{"phone":1111, "work":"developer"},
    "shyam":"222",
}
print(emp["ram"]["work"])
print(emp.get("ram").get("work"))

del emp["shyam"]
print(emp)