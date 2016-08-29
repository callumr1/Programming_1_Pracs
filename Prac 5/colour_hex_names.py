

colour_hex_names = {"Alice Blue": "#f0f8ff", "Azure": "#f0ffff", "Beige": "#f5f5dc", "Blue": "#0000ff", "Brown": "#ff4040",
              "Cadet Blue": "#98f5ff", "Chartreuse": "#7fff00", "Chocolate": "#d2691e", "Cyan": "#00ffff",
              "Pink": "#ff1493"}

colour = input("Enter a colour name: ").title()
while colour.title() != "":
    if colour in colour_hex_names:
        print("The hex code for {} is {}".format(colour, colour_hex_names[colour]))
    else:
        print("Invalid colour")
    colour = input("Enter a colour name: ").title()