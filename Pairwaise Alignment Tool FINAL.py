import tkinter as tk
from tkinter import ttk, messagebox
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# -------------------- Alignment Function --------------------
def run_alignment():
    seq1 = entry_seq1.get("1.0", tk.END).strip().upper()
    seq2 = entry_seq2.get("1.0", tk.END).strip().upper()
    method = combo_method.get()

    if not seq1 or not seq2:
        messagebox.showerror("Error", "Please enter both sequences!")
        return

    if method == "Global (Needleman-Wunsch)":
        alignments = pairwise2.align.globalxx(seq1, seq2)
    else:  # Local
        alignments = pairwise2.align.localxx(seq1, seq2)

    result_box.delete("1.0", tk.END)
    for a in alignments[:1]:  # Show only the best alignment
        result_box.insert(tk.END, format_alignment(*a) + "\n")

# -------------------- GUI --------------------
root = tk.Tk()
root.title("Pairwise Alignment Tool")
root.geometry("700x600")
root.configure(bg="#1e1e2f")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#1e1e2f", foreground="white", font=("Arial", 11))
style.configure("TButton", background="#3e3e5f", foreground="white", font=("Arial", 11), padding=6)
style.map("TButton", background=[("active", "#5e5e8f")])
style.configure("TCombobox", padding=5, font=("Arial", 11))

# Input
ttk.Label(root, text="Sequence 1:").pack(pady=5)
entry_seq1 = tk.Text(root, height=4, width=80, bg="#2e2e3f", fg="white", insertbackground="white")
entry_seq1.pack(pady=5)

ttk.Label(root, text="Sequence 2:").pack(pady=5)
entry_seq2 = tk.Text(root, height=4, width=80, bg="#2e2e3f", fg="white", insertbackground="white")
entry_seq2.pack(pady=5)

# Dropdown
ttk.Label(root, text="Select Alignment Type:").pack(pady=5)
combo_method = ttk.Combobox(root, values=["Global (Needleman-Wunsch)", "Local (Smith-Waterman)"])
combo_method.current(0)
combo_method.pack(pady=5)

# Button
ttk.Button(root, text="Run Alignment", command=run_alignment).pack(pady=10)

# Results
ttk.Label(root, text="Results:").pack(pady=5)
result_box = tk.Text(root, height=15, width=80, bg="#12121c", fg="#00ffcc", insertbackground="white")
result_box.pack(pady=10)

root.mainloop()
