import tkinter as tk
from tkinter import messagebox

class SimpleNoteApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Note App")

        # Frame untuk bagian input
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(pady=10)

        self.label = tk.Label(self.input_frame, text="Masukkan Catatan:")
        self.label.pack(side=tk.LEFT)

        self.entry = tk.Entry(self.input_frame, width=40)
        self.entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.input_frame, text="Tambah", command=self.add_note)
        self.add_button.pack(side=tk.LEFT)

        # Frame untuk area teks dan canvas
        self.text_frame = tk.Frame(master)
        self.text_frame.pack(pady=10)

        self.text_area = tk.Text(self.text_frame, height=10, width=50)
        self.text_area.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(self.text_frame, width=200, height=100, bg="white")
        self.canvas.pack(side=tk.RIGHT, padx=10)

        # Tombol untuk membersihkan catatan
        self.clear_button = tk.Button(master, text="Bersihkan Catatan", command=self.clear_notes)
        self.clear_button.pack(pady=5)

        # Tombol untuk menggambar di canvas
        self.draw_button = tk.Button(master, text="Gambar Kotak", command=self.draw_square)
        self.draw_button.pack(pady=5)

    def add_note(self):
        note = self.entry.get()
        if note:
            self.text_area.insert(tk.END, note + "\n")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Catatan tidak boleh kosong!")

    def clear_notes(self):
        self.text_area.delete('1.0', tk.END)

    def draw_square(self):
        self.canvas.create_rectangle(50, 25, 150, 75, fill="blue")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleNoteApp(root)
    root.mainloop()
