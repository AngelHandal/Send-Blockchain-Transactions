import hashlib
import tkinter as tk
from tkinter import messagebox

class AHCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


window = tk.Tk()
window.title("AH Portal")
window.geometry("400x300")


window.configure(bg="black")


contacts = ["Darlene", "Reynold", "William", "Julian", "Vanessa", "Bob"]
balance = 10.2

# Historial de transacciones 
blockchain = []


space_br = tk.Label(window, text="", bg="black")
space_br.pack()


balance_lbl = tk.Label(window, text="BALANCE", fg="white", bg="black", font=("Arial", 25))
balance_lbl.pack(pady=10)


my_balance = tk.Label(window, text=str(balance) + " AH", fg="white", bg="black", font=("Arial", 25))
my_balance.pack(pady=10)

def show_contacts():

    window_contacts = tk.Toplevel(window)
    window_contacts.title("Select a Contact")

    select_contact = tk.StringVar()
    select_contact.set(contacts[0])  # default value

    list_contacts = tk.OptionMenu(window_contacts, select_contact, *contacts)
    list_contacts.pack(padx=20, pady=10)


    amount_lbl = tk.Label(window_contacts, text="Amount to Transfer (AH):", fg="white", bg="black")
    amount_lbl.pack()
    
    amount_entry = tk.Entry(window_contacts)
    amount_entry.pack()


    def make_transfer():
        global balance
        selected_contact = select_contact.get()
        amount = amount_entry.get()

        try:
            amount = float(amount)
            if amount <= 0:
                messagebox.showerror("Error", "The quantity must be greater than zero.")
            elif amount > balance:
                messagebox.showerror("Error", "You do not have enough funds to make the transfer.")
            else:
                
                new_balance = balance - amount
                message = f"You have send {amount} AH To {selected_contact}"
                messagebox.showinfo("Message", message)
                window_contacts.destroy()
                
                balance = new_balance
                my_balance.config(text=str(balance) + " AH")
                
                new_block = AHCoinBlock(blockchain[-1].block_hash if blockchain else "Initial Text", [message])
                blockchain.append(new_block)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")


    btn_transfer = tk.Button(window_contacts, text="Transfer", command=make_transfer, bg="green", fg="white")
    btn_transfer.pack(pady=10)


def show_history():
    window_history = tk.Toplevel(window)
    window_history.title("Transaction History as a Blockchain")

    for i, block in enumerate(blockchain):
        message = f"Block {i + 1}:\n"
        message += f"Data: {block.block_data}\n"
        message += f"Hash: {block.block_hash}\n"
        message += "\n"

        block_label = tk.Label(window_history, text=message, fg="black", bg="white", font=("Arial", 12))
        block_label.pack(padx=20, pady=10)


space_br = tk.Label(window, text="", bg="black")
space_br.pack()


btn_show_contacts = tk.Button(window, text="Transfer", command=show_contacts, bg="gold", fg="black", font=("Arial", 18))
btn_show_contacts.pack()

space_br = tk.Label(window, text="", bg="black")
space_br.pack()


btn_historial = tk.Button(window, text="History", command=show_history, bg="blue", fg="white", font=("Arial", 18))
btn_historial.pack()


window.mainloop()