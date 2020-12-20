
print("Hello Koala")
print(10)
print("10")

print(10 == "10")

msg = "Hello Koala"

print(msg[:5])
print(msg[0:5])
print(msg[6:])
print(msg[::-1])


msg = msg.lower()
print(msg)
print(msg.isupper())
print(msg.capitalize())

print(msg.isalnum())
print(msg.isnumeric())


msg = 1
print(str(msg).zfill(4))

msg = "HelloWorld1"
print(msg.isascii())
print(msg.isalnum())
print(msg.isalpha())


print("abc" + "def")
print(msg+"abc")

print("==" * 50)

msg = "Hello Koala"
print(msg.split(" "))
print(msg.replace("Koala", "Ryan"))
print(" ".join(msg.split(" ")))
print(msg.endswith("Koala"))
print(msg.startswith("Hi"))

msg = "Hi    Hello   "
print(msg + "||")
print(msg.strip() + "||")

if " Hel" in msg:
    print("' Hel' in msg!")

print(msg.count("H"))
print(f"{msg}")
print("{}".format(msg))
print("{:,}".format(10000000))

msg = "헬로 코알라이언!"
print(msg)
msg = msg.encode("utf-8")
print(msg)
msg = msg.decode("utf-8")
print(msg)
