import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Siva Calculator")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#093aec")  # Dark Blue

        self.expression = ""

        self.display_frame()
        self.button_frame()
        self.create_buttons()

    def display_frame(self):
        self.input_text = tk.StringVar()
        self.input_field = tk.Entry(self.root, textvariable=self.input_text,
                                    font=('Arial', 26, 'bold'), bd=0,
                                    bg="#ffffff", fg="#093aec", justify="right")
        self.input_field.pack(expand=True, fill="both", ipadx=8, ipady=25, padx=20, pady=20)

    def button_frame(self):
        self.button_container = tk.Frame(self.root, bg="#093aec")  # Dark Blue
        self.button_container.pack(expand=True, fill="both")

    def add_to_expression(self, value):
        self.expression += str(value)
        self.input_text.set(self.expression)

    def clear_expression(self):
        self.expression = ""
        self.input_text.set("")

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception:
            self.input_text.set("Error")
            self.expression = ""

    def create_buttons(self):
        buttons = [
            ["C", "/", "*", "←"],
            ["7", "8", "9", "-"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "="],
            ["0", ".", "", ""]
        ]

        for row in buttons:
            row_frame = tk.Frame(self.button_container, bg="#093aec")
            row_frame.pack(expand=True, fill="both")
            for label in row:
                if label == "":
                    tk.Label(row_frame, text="", bg="#093aec").pack(side="left", expand=True, fill="both", padx=5, pady=5)
                    continue
                btn = tk.Button(row_frame, text=label, font=("Arial", 20, 'bold'),
                                bg="#ffffff", fg="#093aec",
                                activebackground="#c5e1f7", activeforeground="#093aec",
                                bd=0, relief="flat",
                                command=lambda l=label: self.on_button_click(l))
                btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)

    def on_button_click(self, label):
        if label == "C":
            self.clear_expression()
        elif label == "=":
            self.calculate()
        elif label == "←":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        else:
            self.add_to_expression(label)


# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
