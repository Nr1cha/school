import ascii_magic
nick = ascii_magic.from_image_file("skull.jpeg",columns=50,char="\"")
# ascii_magic.to_terminal(nick)


#output
print(nick)