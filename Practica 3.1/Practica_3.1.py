import tkinter as tk

app = tk.Tk()
app.title("Conversor de temperatura")

def reset():
    entry_F.delete(0,tk.END)
    entry_F.insert(0,0.0)
    entry_C.delete(0,tk.END)
    entry_C.insert(0,0.0)
    
def celsius_to_fahrenheit():
    celsius = float(entry_C.get())
    fahrenheit = (celsius * 9/5) + 32
    entry_F.delete(0, tk.END)
    entry_F.insert(0, f"{fahrenheit:2f}")

def fahrenheit_to_celsius():
    fahrenheit = float(entry_F.get())
    celsius = (fahrenheit - 32) * 5.0/9.0
    entry_C.delete(0, tk.END)
    entry_C.insert(0, f"{celsius:2f}") 


label_F = tk.Label(app, text="Fahrenheit:")
label_F.grid(row=0, column=0)

entry_F = tk.Entry(app)
entry_F.grid(row=0, column=1)

button_F = tk.Button(app, text="Convertir a Celsius",command=fahrenheit_to_celsius)
button_F.grid(row=0, column=2)

label_C = tk.Label(app, text="Celsius:")
label_C.grid(row=1, column=0, sticky="w")

entry_C = tk.Entry(app)
entry_C.grid(row=1, column=1)

button_C = tk.Button(app, text="Convertir a Fahrenheit", command=celsius_to_fahrenheit)
button_C.grid(row=1, column=2)

button_R= tk.Button(app,text="Restablecer", command=reset)
button_R.grid(row=2,column=1)

app.mainloop()
