import cairosvg
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from PIL import Image

root = tk.Tk()
root.title("IMAGE TO PNG CONVERTER")
root.geometry("500x350")

File = tk.StringVar(value="No file has been selected")
Format = tk.StringVar(value="Format: None")

def File_Select():
    file_path = filedialog.askopenfilename(
        title="Upload an Image File",
        filetypes=[
            ("All Supported", "*.svg;*.webp"),
            ("SVG files", "*.svg"),
            ("WebP files", "*.webp")
        ]
    )
    if file_path:
        File.set(file_path)
        ext = os.path.splitext(file_path)[1].upper().replace(".", "")
        if ext in ["SVG", "WEBP"]:
            Format.set(f"Detected Format: {ext}")
        else:
            Format.set("Format: Unsupported")

def File_Convert():
    FilePath = File.get()

    if FilePath == "No file has been selected":
        messagebox.showwarning("No file", "No file has been selected")
        return

    default_name = os.path.splitext(os.path.basename(FilePath))[0] + ".png"
    save_path = filedialog.asksaveasfilename(
        title="Save PNG as",
        defaultextension=".png",
        initialfile=default_name,
        filetypes=[("PNG files", "*.png")]
    )

    if not save_path:
        return

    try:
        if FilePath.lower().endswith('.svg'):
            cairosvg.svg2png(url=FilePath, write_to=save_path, scale=2.0)
        elif FilePath.lower().endswith('.webp'):
            with Image.open(FilePath) as img:
                img.save(save_path, "PNG")
        
        messagebox.showinfo("Success", f"Saved to:\n{save_path}")
    except Exception as e:
        messagebox.showerror("Conversion failed", str(e))

# Layout
title_label = tk.Label(root, text="Image to PNG Converter", font=("Impact", 14))
title_label.pack(pady=15)

choose_button = tk.Button(root, text="Choose File", command=File_Select)
choose_button.pack(pady=20)

file_label = tk.Label(root, textvariable=File, wraplength=350, fg="gray")
file_label.pack(pady=25)

format_label = tk.Label(root, textvariable=Format, wraplength=350, fg="gray")
format_label.pack(pady=10)

convert_button = tk.Button(root, text="Convert to PNG", command=File_Convert, bg="#1EA823", fg="white")
convert_button.pack(pady=30)

root.mainloop()





