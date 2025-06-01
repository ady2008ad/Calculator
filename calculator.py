import tkinter as tk

#create the main window
root=tk.Tk()
root.title("Simple Calculator")

#run the app

#Display Entry
entry=tk.Entry(root, width=20, font=("Arial",24))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Function to handle button clicks
def button_click(symbol):
    current = entry.get()
    if symbol == '=':
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, symbol)

# Add buttons to the grid
row = 1
col = 0
for button in buttons:
    action = lambda x=button: button_click(x)
    tk.Button(root, text=button, padx=20, pady=20, command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1
tk.Button(root, text="C", padx=20, pady=20, command=lambda: entry.delete(0, tk.END)).grid(row=row, column=0, columnspan=4, sticky="we")
root.mainloop()