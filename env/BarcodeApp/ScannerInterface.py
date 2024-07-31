import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from BarcodeApp.BarcodeScanner import BarcodeReader

class BarcodeScannerGUI():
    def __init__(self, root):
        self.root = root
        self.root.title("Barcode Scanner GUI")

        self.result_label = tk.Label(root, text="Scanned Barcode: ")
        self.result_label.pack(pady=20)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=20)

        self.upload_button = tk.Button(root, text="Upload Barcode Image", command=self.upload_image)
        self.upload_button.pack(pady=20)

    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")]
        )
        if file_path:
            image = Image.open(file_path)
            image.thumbnail((300,300))
            img = ImageTk.PhotoImage(image)
            self.image_label.config(image=img)
            self.image_label.image = img

            barcodeInfo = BarcodeReader(file_path)
            self.result_label.config(text=f"Scanned Barcode: {barcodeInfo}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BarcodeScannerGUI(root)
    root.mainloop()