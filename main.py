from tkinter import *


def button_clicked():
    new_text = miles_input.get()
    km_result_lab.config(text=str(float(new_text) * 1.60934))


window = Tk()
window.title(" Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=10)

# Labels
km_result_lab = Label(text="0", font=("Arial", 12, "bold"))
km_result_lab.grid(column=2, row=1)

miles_leb = Label(text="Miles", font=("Arial", 12, "bold"))
miles_leb.grid(column=3, row=0)
is_equal_to_leb = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_to_leb.grid(column=0, row=1)
km_leb = Label(text="KM", font=("Arial", 12, "bold"))
km_leb.grid(column=3, row=1)
# Entry
miles_input = Entry(width=10)
miles_input.grid(column=2, row=0)
# Button
calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=2, row=3)

window.mainloop()
