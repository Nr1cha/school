# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

from cgitb import text
import tkinter as tk
import number_entry as numy


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Area of a Circle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and each
# widget is an object, the code to make a GUI usually has many variables
# to store the many objects. Because there are so many variable names,
# programmers often adopt a naming convention to help a programmer keep
# track of all the variables. One popular naming convention is to type a
# three letter prefix in front of the names of all variables that store
# GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Age:" # *: rename age to radius 
    lbl_radius = tk.Label(frm_main, text="Radius:")

    # Create a integer entry box where the user will enter her age.
    ent_radius = numy.IntEntry(frm_main, 1, 90, width=5) #*: rename age to radius

    # Create a label that displays "Area:" #!: rates needs to be area
    lbl_area = tk.Label(frm_main, text="Area:")

    # Create labels that will display the results.
    # lbl_slow = tk.Label(frm_main, width=4)
    # lbl_fast = tk.Label(frm_main, width=4)

    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(  row=0, column=0, padx=3, pady=3)
    ent_radius.grid(  row=0, column=1, padx=3, pady=3)
    lbl_area.grid(row=0, column=2, padx=(30,3), pady=3)
    # lbl_slow.grid( row=0, column=3, padx=3, pady=3)
    # lbl_fast.grid( row=0, column=4, padx=3, pady=3)
    btn_clear.grid(row=1, column=0, padx=3, pady=3, columnspan=5, sticky="W")


    # This function will be called each time the user releases a key.
    def calculate(event): #!function that calculates what is needed
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the radius.
            radius = ent_radius.get() #*: change age to radius

            # Compute the area from radius. #! this is the math portion
            area = 3.14 * radius ** 2

            # Compute the user's slowest and
            # fastest beneficial heart rates.
            # slow = max_rate * 0.65
            # fast = max_rate * 0.85

            # Display the slowest and fastest benficial
            # heart rates for the user to see.
            # lbl_slow.config(text=f"{slow:.0f}")
            # lbl_fast.config(text=f"{fast:.0f}")
            lbl_area.config(text=f"{area}")

        except ValueError:
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and fastest labels.
            # lbl_slow.config(text="")
            # lbl_fast.config(text="")
            lbl_area.config(text=f"")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_radius.delete(0, tk.END)
        lbl_area.config(text="")
        # lbl_slow.config(text="")
        # lbl_fast.config(text="")
        ent_radius.focus()


    # Bind the calculate function to the age entry box
    # so that the calculate function will be called when
    # the user changes the text in the entry box.
    ent_radius.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_radius.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
