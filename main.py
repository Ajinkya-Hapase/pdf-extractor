import tkinter as tk
import os
import shutil
from PyPDF2 import PdfReader
from tkinter import filedialog

def main():

    def on_button1_click():
        folder_path = filedialog.askdirectory()  # Open system dialog to select folder
        if folder_path:
            output_folder = "Success"  # Replace with the actual output folder path
            not_available_folder = "Failed"

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            if not os.path.exists(not_available_folder):
                os.makedirs(not_available_folder)

            search_strings = ["No Matching Data", "No chartable data found", "No data found", "java",
                              "The content-script (rows) contained no data"]

            for filename in os.listdir(folder_path):
                if filename.endswith(".pdf"):
                    file_path = os.path.join(folder_path, filename)
                    with open(file_path, "rb") as file:
                        pdf = PdfReader(file)
                        text = ""

                        for page in pdf.pages:
                            text += page.extract_text()
                        if any(string in text for string in search_strings):
                            output_text.insert(tk.END, f"Copying {filename} to {output_folder}\n")
                            shutil.copy(file_path, output_folder)
                        else:
                            output_text.insert(tk.END, f"Copying {filename} to {not_available_folder}\n")
                            shutil.copy(file_path, not_available_folder)

            output_text.insert(tk.END, "PDF files copied successfully\n")
        else:
            output_text.insert(tk.END, "No folder selected\n")

    def on_button2_click():
        root.destroy()

    root = tk.Tk()
    root.geometry("600x500")
    root.resizable(False, False)
    root.title("PDF Separator")

    label = tk.Label(root, text="PDF Validator", font=("Arial", 18, "bold"))
    label.pack(pady=20)

    button1 = tk.Button(root, text="Download Emails", command=on_button1_click, font=("Arial", 12), bd=2, width=15)
    button1.pack(pady=10)

    button1 = tk.Button(root, text="Validate PDF", command=on_button1_click, font=("Arial", 12), bd=2, width=15)
    button1.pack(pady=10)

    button2 = tk.Button(root, text="Exit", command=on_button2_click, font=("Arial", 12), bd=2, width=15)
    button2.pack(pady=5)

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    output_text = tk.Text(root, yscrollcommand=scrollbar.set)
    output_text.pack(pady=20)

    scrollbar.config(command=output_text.yview)

    root.mainloop()


if __name__ == "__main__":
    main()
