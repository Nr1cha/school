import ascii_magic
nick = ascii_magic.from_image_file("skull.jpeg",
columns=150,
width_ratio=2,
# mode=ascii_magic.Modes.HTML
)
# ascii_magic.to_terminal(nick)


#output
print(nick)