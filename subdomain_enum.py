import requests
import tkinter as tk
from tkinter import scrolledtext, messagebox

def fetch_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            subdomains = set(entry["name_value"] for entry in data)
            return subdomains
        else:
            return None
    except Exception as e:
        return None

def run_enumeration():
    domain = entry.get()
    if not domain:
        messagebox.showerror("Error", "Please enter a domain!")
        return

    subdomains = fetch_subdomains(domain)
    
    if subdomains:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "\n".join(sorted(subdomains)))
        result_text.config(state=tk.DISABLED)

        # Save results to a file
        with open("subdomains.txt", "w") as f:
            for sub in sorted(subdomains):
                f.write(sub + "\n")
        
        messagebox.showinfo("Success", "Subdomains saved in 'subdomains.txt'")
    else:
        messagebox.showwarning("No Results", "No subdomains found.")

# GUI Setup
root = tk.Tk()
root.title("Subdomain Enumeration Tool")
root.geometry("500x400")

tk.Label(root, text="Enter Domain:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=5)

tk.Button(root, text="Find Subdomains", command=run_enumeration, font=("Arial", 12)).pack(pady=10)

result_text = scrolledtext.ScrolledText(root, width=50, height=15, state=tk.DISABLED)
result_text.pack(pady=5)

root.mainloop()
