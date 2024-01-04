import tkinter as tk
from tkinter import messagebox

class Harga_jual_beli_emas:
    def __init__(self, root):
        self.root = root
        self.root.title("Jual Beli Emas")
        
        self.harga_emas = {'24 Karat': {'beli': 910, 'jual': 800},
                           '23 Karat': {'beli': 867, 'jual': 725},
                           '22 Karat': {'beli': 830, 'jual': 695}}
        
        self.label_judul = tk.Label(root, text="Jual Beli Emas", font=('Arial', 24, "bold"))
        self.label_judul.pack(pady=15)
        
        self.label_karat = tk.Label(root, text="Pilih Karat Emas:", font=14)
        self.label_karat.pack()
        
        self.var_karat = tk.StringVar()
        self.var_karat.set('Pilih')  # Karat default
        self.option_menu_karat = tk.OptionMenu(root, self.var_karat, *self.harga_emas.keys())
        self.option_menu_karat.pack(pady=10)
        
        self.label_jumlah = tk.Label(root, text="Jumlah Gram Emas:", font=14)
        self.label_jumlah.pack(pady=10)
        
        self.entry_jumlah = tk.Entry(root)
        self.entry_jumlah.pack()
        
        self.btn_hitung_harga = tk.Button(root, text="Hitung Harga", command=self.hitung_harga)
        self.btn_hitung_harga.pack(pady=10)
        
    def hitung_harga(self):
        try:
            jumlah_gram = int(self.entry_jumlah.get())
            harga_karat = self.harga_emas[self.var_karat.get()]
            harga_beli = harga_karat['beli']
            harga_jual = harga_karat['jual']
            
            total_harga_beli = jumlah_gram * harga_beli
            total_harga_jual = jumlah_gram * harga_jual
            
            messagebox.showinfo("Harga Emas", 
                                f"Harga Beli Emas ({self.var_karat.get()}): Rp{total_harga_beli:.3f}\n"
                                f"Harga Jual Emas ({self.var_karat.get()}): Rp{total_harga_jual:.3f}")
            
        except ValueError:
            messagebox.showerror("Error", "Masukkan jumlah gram emas yang valid.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    app = Harga_jual_beli_emas(root)

    root.mainloop()
