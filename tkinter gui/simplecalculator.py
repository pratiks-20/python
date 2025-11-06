import tkinter as tk

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_label.config(text=f"Result: {num1 + num2}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x200")

tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Add", command=add_numbers, bg="lightblue").pack(pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5)

root.mainloop()
