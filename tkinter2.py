import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_db():
    conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nama_siswa TEXT NOT NULL,
            biologi INTEGER NOT NULL,
            fisika INTEGER NOT NULL,
            inggris INTEGER NOT NULL,
            prediksi_fakultas TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

create_db()

def prediksi_fakultas(biologi, fisika, inggris):
    if biologi > fisika and biologi > inggris:
        return "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        return "Teknik"
    elif inggris > biologi and inggris > fisika:
        return "Bahasa"
    else:
        return "Tidak dapat ditentukan"

def submit_nilai():
    nama = entry_nama.get().strip()
    try:
        bio = int(entry_bio.get())
        fis = int(entry_fis.get())
        ing = int(entry_ing.get())
    except ValueError:
        messagebox.showerror("Error", "Nilai harus berupa angka!")
        return

    if not nama:
        messagebox.showerror("Error", "Nama siswa tidak boleh kosong!")
        return

    hasil_prediksi = prediksi_fakultas(bio, fis, ing)

    conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO nilai_siswa(nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    """, (nama, bio, fis, ing, hasil_prediksi)) 
    conn.commit()
    conn.close()

    messagebox.showinfo("Hasil Prediksi", f"Prediksi Fakultas: {hasil_prediksi}")

    entry_nama.delete(0, tk.END)
    entry_bio.delete(0, tk.END)
    entry_fis.delete(0, tk.END)
    entry_ing.delete(0, tk.END)


def on_enter(e):
    btn_submit["bg"] = "#50fa7b"
    btn_submit["fg"] = "black"

def on_leave(e):
    btn_submit["bg"] = "#44475a"
    btn_submit["fg"] = "black"

root = tk.Tk()
root.title("Aplikasi Prediksi Fakultas")
root.geometry("400x450")
root.config(bg="#282a36")

title_label = tk.Label(root, text="Form Prediksi Fakultas Siswa", font=("Arial", 14, "bold"), bg="#282a36", fg="#f8f8f2")
title_label.pack(pady=20)

frame_input = tk.Frame(root, bg="#282a36")
frame_input.pack(pady=5)

label_nama = tk.Label(frame_input, text="Nama Siswa:", font=("Arial", 10), bg="#282a36", fg="#f8f8f2")
label_nama.grid(row=0, column=0, sticky="w", pady=5)
entry_nama = tk.Entry(frame_input, font=("Arial", 10), width=25)
entry_nama.grid(row=0, column=1, pady=5, padx=10)

label_bio = tk.Label(frame_input, text="Nilai Biologi:", font=("Arial", 10), bg="#282a36", fg="#f8f8f2")
label_bio.grid(row=1, column=0, sticky="w", pady=5)
entry_bio = tk.Entry(frame_input, font=("Arial", 10), width=25)
entry_bio.grid(row=1, column=1, pady=5, padx=10)

label_fis = tk.Label(frame_input, text="Nilai Fisika:", font=("Arial", 10), bg="#282a36", fg="#f8f8f2")
label_fis.grid(row=2, column=0, sticky="w", pady=5)
entry_fis = tk.Entry(frame_input, font=("Arial", 10), width=25)
entry_fis.grid(row=2, column=1, pady=5, padx=10)

label_ing = tk.Label(frame_input, text="Nilai Inggris:", font=("Arial", 10), bg="#282a36", fg="#f8f8f2")
label_ing.grid(row=3, column=0, sticky="w", pady=5)
entry_ing = tk.Entry(frame_input, font=("Arial", 10), width=25)
entry_ing.grid(row=3, column=1, pady=5, padx=10)

btn_submit = tk.Button(root, text="Submit Nilai", command=submit_nilai, font=("Arial", 11, "bold"), 
                       bg="#44475a", fg="black", width=20, relief="flat", cursor="hand2")
btn_submit.pack(pady=25)

btn_submit.bind("<Enter>", on_enter)
btn_submit.bind("<Leave>", on_leave)

root.mainloop()