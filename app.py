import tkinter as tk
import sys

class UnitConverter(tk.Frame):
    """
    Unit Converter Application
    Supports:
        • Kilometer ↔ Miles
        • Kilogram ↔ Pounds
        • Fahrenheit ↔ Celsius
    """

    def __init__(self, root):
        # Colour Scheme
        self.colour1 = "#0e2d41"     # Background
        self.colour2 = "#e776a2"     # Heading
        self.colour3 = "#dfdfd3"     # Entry/Option Background

        # Available conversions
        self.conversions_available = [
            "km --> mi",
            "mi --> km",
            "kg --> lbs",
            "lbs --> kg",
            "°F --> °C",
            "°C --> °F"
        ]
        super().__init__(root, bg=self.colour1)
        self.pack(fill="both", expand=True)
        self.create_widgets()

    # Create all widgets
    def create_widgets(self):
        # Title
        title = tk.Label(
            self,
            text="Unit Converter",
            font=("Arial", 26, "bold"),
            bg=self.colour1,
            fg=self.colour2
        )
        title.pack(pady=(15, 20))

        # Conversion Menu
        self.conversion = tk.StringVar()
        self.conversion.set(self.conversions_available[0])
        self.option = tk.OptionMenu(
            self,
            self.conversion,
            *self.conversions_available
        )
        self.option.config(
            font=("Arial", 15),
            bg=self.colour3,
            fg=self.colour1,
            width=18,
            borderwidth=0,
            indicatoron=0,
            highlightthickness=0
        )
        self.option["menu"].config(
            font=("Arial", 13)
        )
        self.option.pack(pady=10)

        # Input Entry
        self.input_entry = tk.Entry(
            self,
            font=("Arial", 15),
            justify="center",
            bg=self.colour3,
            fg=self.colour1,
            width=15,
            relief="flat"
        )
        self.input_entry.pack(pady=20)

        # Convert Button
        convert_button = tk.Button(
            self,
            text="Convert",
            font=("Arial", 13, "bold"),
            bg=self.colour2,
            fg="white",
            width=12,
            command=self.convert
        )
        convert_button.pack()

        # Result Label
        self.result = tk.Label(
            self,
            text="",
            font=("Arial", 18, "bold"),
            bg=self.colour1,
            fg="white"
        )
        self.result.pack(pady=25)

    # Conversion Function
    def convert(self):
        try:
            value = float(self.input_entry.get())
        except ValueError:
            self.result.config(text="Please enter a valid number.")
            return
        conversion = self.conversion.get()

        # Kilometer → Miles
        if conversion == "km --> mi":
            answer = value * 0.621371
            text = f"{value} km = {answer:.2f} mi"

        # Miles → Kilometer
        elif conversion == "mi --> km":
            answer = value * 1.60934
            text = f"{value} mi = {answer:.2f} km"

        # Kilogram → Pounds
        elif conversion == "kg --> lbs":
            answer = value * 2.20462
            text = f"{value} kg = {answer:.2f} lbs"

        # Pounds → Kilogram
        elif conversion == "lbs --> kg":
            answer = value / 2.20462
            text = f"{value} lbs = {answer:.2f} kg"

        # Fahrenheit → Celsius
        elif conversion == "°F --> °C":
            answer = (value - 32) * 5 / 9
            text = f"{value} °F = {answer:.2f} °C"

        # Celsius → Fahrenheit
        elif conversion == "°C --> °F":
            answer = value * 9 / 5 + 32
            text = f"{value} °C = {answer:.2f} °F"

        else:
            text = "Conversion not supported."
        self.result.config(text=text)


# Main Program
root = tk.Tk()
root.title("Unit Converter")
operating_system = sys.platform

if "win" in operating_system:
    root.geometry("500x380")

elif "linux" in operating_system:
    root.geometry("500x400")

elif "darwin" in operating_system:
    root.geometry("500x400")

root.resizable(False, False)
UnitConverter(root)
root.mainloop()