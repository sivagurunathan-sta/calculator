Here's a **detailed explanation** of what each part of the white and dark blue themed calculator code does — broken down step-by-step so you fully understand how it works:

---

## 🔧 1. **Importing Tkinter**

```python
import tkinter as tk
```

* `tkinter` is the built-in Python library used for creating GUI applications.
* We use the `tk` alias to access its classes and methods easily.

---

## 🏗️ 2. **Defining the Calculator Class**

```python
class CalculatorApp:
    def __init__(self, root):
```

* This defines a class `CalculatorApp` which holds all the logic for the calculator.
* `__init__` initializes the GUI components.

---

## 🖼️ 3. **Creating the Main Window**

```python
self.root = root
self.root.title("Blue-Themed Calculator")
self.root.geometry("400x550")
self.root.resizable(False, False)
self.root.configure(bg="#1e3d59")  # Dark Blue
```

* Sets up the main app window (title, size, background color).
* Makes it non-resizable for better layout control.

---

## ✏️ 4. **Creating the Display Entry**

```python
self.input_text = tk.StringVar()
self.input_field = tk.Entry(...)
```

* `input_text` is a variable that updates the screen (user input and result).
* `Entry` is used to show the expression and output like a calculator display.
* Font is set to large and bold, background is white, text is dark blue.

---

## 🎛️ 5. **Creating Button Container Frame**

```python
self.button_container = tk.Frame(self.root, bg="#1e3d59")
```

* A frame that holds all the calculator buttons.
* Keeps UI organized (display and buttons are separated).

---

## ➕ 6. **Handling Expressions**

```python
def add_to_expression(self, value):
    self.expression += str(value)
    self.input_text.set(self.expression)
```

* Adds digits/operators to the current expression when a button is pressed.

```python
def clear_expression(self):
    self.expression = ""
    self.input_text.set("")
```

* Clears the expression when `C` is pressed.

```python
def calculate(self):
    try:
        result = str(eval(self.expression))
        self.input_text.set(result)
        self.expression = result
    except Exception:
        self.input_text.set("Error")
        self.expression = ""
```

* `eval()` evaluates the math expression (e.g., "5+3\*2").
* Shows the result or displays `Error` if input is invalid.

---

## ⌨️ 7. **Creating Buttons**

```python
buttons = [
    ["C", "/", "*", "←"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "", ""]
]
```

* This 2D list defines the layout and labels of all calculator buttons.

---

## 🔲 8. **Button Generation Loop**

```python
for row in buttons:
    row_frame = tk.Frame(...)
    for label in row:
        ...
        btn = tk.Button(..., command=lambda l=label: self.on_button_click(l))
```

* For each row in `buttons`, a new row frame is created.
* For each label in that row, a button is created and styled.
* `lambda l=label:` ensures each button knows what it should do when clicked.

---

## 🧠 9. **Button Logic Handler**

```python
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
```

* Defines what happens when each type of button is clicked:

  * `C` clears everything.
  * `←` deletes the last character.
  * `=` performs calculation.
  * Other buttons (numbers/operators) are added to the input.

---

## 🚀 10. **Main Application Runner**

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
```

* This is the entry point.
* Creates the main window (`root`) and runs the app using `mainloop()`.

---

## ✅ Summary of Components:

| Component     | Description                                      |
| ------------- | ------------------------------------------------ |
| `tk.Tk()`     | Main app window                                  |
| `Entry`       | Text display for numbers/results                 |
| `Frame`       | Organizes the layout (rows of buttons)           |
| `Button`      | Clickable calculator buttons                     |
| `eval()`      | Evaluates math expressions                       |
| `StringVar()` | Tracks and updates input display                 |
| Color Scheme  | White buttons, dark blue background, light hover |

---

