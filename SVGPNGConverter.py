import cairosvg
import tkinter as tk
from tkinter import filedialog, messagebox
import os

root = tk.Tk()
root.title("SVG TO PNG CONVERTER")
root.geometry("500x350")

File = tk.StringVar(value="No file has been selected")

def File_Select():
        file_path = filedialog.askopenfilename(
                title="Upload the SVG File",
                filetypes=[("SVG files", "*.svg")]
        )
        if file_path:
                File.set(file_path)

 
def File_Convert():
        SVGPath = File.get()
 
        if SVGPath == "No file has been Selected":
                messagebox.showwarning("No file", "No file has been selected")
                return
 
        default_name = os.path.splitext(os.path.basename(SVGPath))[0] + ".png"
        save_path = filedialog.asksaveasfilename(
        title="Save PNG as",
        defaultextension=".png",
        initialfile=default_name,
        filetypes=[("PNG files", "*.png")]
        )
 
        if not save_path:
                return
 
        try:
            cairosvg.svg2png(url=SVGPath, write_to=save_path, scale=2.0)
            messagebox.showinfo("Success", f"Saved to:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Conversion failed", str(e))
 
 
 
# Layout
title_label = tk.Label(root, text="SVG to PNG Converter", font=("Impact", 14,))
title_label.pack(pady=15)
 
choose_button = tk.Button(root, text="Choose SVG File", command=File_Select)
choose_button.pack(pady=20)
 
file_label = tk.Label(root, textvariable=File, wraplength=350, fg="gray")
file_label.pack(pady=25)
 
convert_button = tk.Button(root, text="Convert to PNG", command=File_Convert, bg="#1EA823", fg="white")
convert_button.pack(pady=30)
 
root.mainloop()






