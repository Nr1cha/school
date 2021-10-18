import ascii_magic
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nick = None
try:
    nick = ascii_magic.from_url("https://universe.byu.edu/wp-content/uploads/2015/11/Modern-Sailor-Cougar1-300x279.jpg",
        columns=100,
        width_ratio=2,
    # mode=ascii_magic.Modes.HTML
    )
except OSError as e:
    print(f"could not load the image, server said: {e.code}")
# ascii_magic.to_terminal(nick)
print(nick)


#output