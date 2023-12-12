import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd

# Function to insert data into CSV
def insert_data():
    new_data = entry.get()
    if new_data:
        with open('data.csv', 'a') as file:
            file.write(new_data + '\n')
        messagebox.showinfo("Success", "Data inserted successfully!")
        entry.delete(0, tk.END)
        plot_chart()

# Function to delete data from CSV
def delete_data():
    delete_item = entry.get()
    if delete_item:
        data = pd.read_csv('data.csv')
        data = data[data['Data'] != delete_item]
        data.to_csv('data.csv', index=False)
        messagebox.showinfo("Success", "Data deleted successfully!")
        entry.delete(0, tk.END)
        plot_chart()

# Function to plot chart from CSV data
def plot_chart():
    data = pd.read_csv('data.csv')
    plt.figure(figsize=(6, 4))
    plt.bar(data['Data'], data.index)
    plt.xlabel('Data')
    plt.ylabel('Index')
    plt.title('Data Visualization')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Creating the GUI
root = tk.Tk()
root.title("CSV Data Manipulation")

label = tk.Label(root, text="Enter Data:")
label.pack()

entry = tk.Entry(root)
entry.pack()

insert_button = tk.Button(root, text="Insert Data", command=insert_data)
insert_button.pack()

delete_button = tk.Button(root, text="Delete Data", command=delete_data)
delete_button.pack()

plot_button = tk.Button(root, text="Plot Chart", command=plot_chart)
plot_button.pack()

root.mainloop()
