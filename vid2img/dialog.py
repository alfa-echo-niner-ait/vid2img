import tkinter as tk
import ttkbootstrap as tb

class AboutDialog(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("About vid2img")
        self.geometry("400x300")
        self.content = """
        Test...
        This is a custom dialog..
        """

        # Create a Text widget to display the content
        self.text = tk.Text(self, wrap="word", font=("Arial", 12))
        self.text.pack(expand=False, padx=10, pady=10)
        self.text.insert("1.0", self.content)

        # Add an OK button to close the dialog
        ok_button = tb.Button(self, text="Close", bootstyle="danger", command=self.destroy)
        ok_button.pack(pady=5)
