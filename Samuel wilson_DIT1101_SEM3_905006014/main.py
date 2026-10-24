import customtkinter as ctk
from tkinter import messagebox


class FarmYieldCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Farm Yield Calculator")
        self.geometry("850x650")
        self.minsize(750, 550)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.plots = []

        title = ctk.CTkLabel(
            self,
            text="Farm Yield Calculator",
            font=("Arial", 26, "bold")
        )
        title.pack(pady=15)

        form = ctk.CTkFrame(self)
        form.pack(fill="x", padx=20, pady=10)

        self.crop = ctk.CTkEntry(
            form,
            placeholder_text="Crop name"
        )
        self.crop.grid(row=0, column=0, padx=8, pady=10, sticky="ew")

        self.area = ctk.CTkEntry(
            form,
            placeholder_text="Area in hectares"
        )
        self.area.grid(row=0, column=1, padx=8, pady=10, sticky="ew")

        self.yield_kg = ctk.CTkEntry(
            form,
            placeholder_text="Yield in kilograms"
        )
        self.yield_kg.grid(row=0, column=2, padx=8, pady=10, sticky="ew")

        for col in range(3):
            form.grid_columnconfigure(col, weight=1)

        buttons = ctk.CTkFrame(self)
        buttons.pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(
            buttons,
            text="Add Plot",
            command=self.add_plot
        ).grid(row=0, column=0, padx=5, pady=10, sticky="ew")

        ctk.CTkButton(
            buttons,
            text="Update Yield",
            command=self.update_yield
        ).grid(row=0, column=1, padx=5, pady=10, sticky="ew")

        ctk.CTkButton(
            buttons,
            text="Load Examples",
            command=self.load_examples
        ).grid(row=0, column=2, padx=5, pady=10, sticky="ew")

        ctk.CTkButton(
            buttons,
            text="Clear Fields",
            command=self.clear_fields,
            fg_color="gray"
        ).grid(row=0, column=3, padx=5, pady=10, sticky="ew")

        for col in range(4):
            buttons.grid_columnconfigure(col, weight=1)

        self.results = ctk.CTkTextbox(self, height=300)
        self.results.pack(fill="both", expand=True, padx=20, pady=10)

        self.summary = ctk.CTkLabel(
            self,
            text="Total plots: 0 | Total yield: 0 kg"
        )
        self.summary.pack(pady=10)

    def add_plot(self):
        crop = self.crop.get().strip()

        try:
            area = float(self.area.get())
            yield_kg = float(self.yield_kg.get())

            if not crop:
                raise ValueError("Enter a crop name.")

            if area <= 0 or yield_kg < 0:
                raise ValueError(
                    "Area must be greater than zero and yield cannot be negative."
                )

        except ValueError as error:
            messagebox.showerror("Invalid Input", str(error))
            return

        self.plots.append({
            "crop": crop,
            "area": area,
            "yield_kg": yield_kg
        })

        self.clear_fields()
        self.display_plots()

    def update_yield(self):
        if not self.plots:
            messagebox.showinfo(
                "No Plots",
                "Add a plot before updating its yield."
            )
            return

        crop = self.crop.get().strip()

        try:
            new_yield = float(self.yield_kg.get())

            if not crop:
                raise ValueError("Enter the crop name to update.")

            if new_yield < 0:
                raise ValueError("Yield cannot be negative.")

        except ValueError as error:
            messagebox.showerror("Invalid Input", str(error))
            return

        matches = [
            plot for plot in self.plots
            if plot["crop"].lower() == crop.lower()
        ]

        if not matches:
            messagebox.showinfo(
                "Crop Not Found",
                "No plot with that crop name was found."
            )
            return

        matches[-1]["yield_kg"] = new_yield

        self.clear_fields()
        self.display_plots()

        messagebox.showinfo(
            "Updated",
            f"Yield updated for {matches[-1]['crop']}."
        )

    def load_examples(self):
        self.plots = [
            {"crop": "Rice", "area": 2.0, "yield_kg": 3500.0},
            {"crop": "Cassava", "area": 1.5, "yield_kg": 4200.0},
            {"crop": "Maize", "area": 1.0, "yield_kg": 1800.0}
        ]

        self.display_plots()

    def clear_fields(self):
        self.crop.delete(0, "end")
        self.area.delete(0, "end")
        self.yield_kg.delete(0, "end")

    def display_plots(self):
        self.results.delete("1.0", "end")

        total_yield = 0

        if not self.plots:
            self.results.insert("end", "No plots added yet.\n")

        for number, plot in enumerate(self.plots, start=1):
            total_yield += plot["yield_kg"]

            productivity = plot["yield_kg"] / plot["area"]

            self.results.insert(
                "end",
                f"Plot {number}\n"
                f"Crop: {plot['crop']}\n"
                f"Area: {plot['area']:.2f} hectares\n"
                f"Yield: {plot['yield_kg']:.2f} kg\n"
                f"Productivity: {productivity:.2f} kg/hectare\n"
                f"{'-' * 40}\n"
            )

        self.summary.configure(
            text=f"Total plots: {len(self.plots)} | "
                 f"Total yield: {total_yield:.2f} kg"
        )


if __name__ == "__main__":
    app = FarmYieldCalculator()
    app.mainloop()