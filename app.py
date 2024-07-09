import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get()) / 100  
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)
        
        result = f"Your BMI is: {bmi:.2f}\n"
        
        if bmi < 18.5:
            result += "Underweight"
        elif 18.5 <= bmi < 25:
            result += "Normal weight"
        elif 25 <= bmi < 30:
            result += "Overweight"
        else:
            result += "Obese"
        
        result_label.config(text=result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for height and weight.")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

tk.Label(root, text="Height (cm):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()

tk.Label(root, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
