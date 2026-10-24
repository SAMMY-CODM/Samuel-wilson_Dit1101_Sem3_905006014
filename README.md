Farm Yield Calculator
Project Description
The Farm Yield Calculator is a Python desktop application that helps users record farm plots and calculate crop productivity. It provides a graphical interface built with CustomTkinter.
Features
- Add a farm plot with a crop name, area in hectares, and yield in kilograms.
- Calculate and display productivity in kilograms per hectare.
- View the total number of plots and total yield.
- Update the yield for an existing crop.
- Load example records for Rice, Cassava, and Maize.
- Clear the input fields.
- Validate input and show helpful error messages.
Technologies Used
- Python
- CustomTkinter
- Tkinter message boxes
Requirements
- Python 3.10 or a compatible Python version
- customtkinter
Installation
1. Open the project in PyCharm.
2. Open the PyCharm terminal.
3. Install the required package:
   pip install customtkinter
How to Run
Run the Python file containing the application (for example, main.py) from PyCharm, or use the terminal:
python main.py
If your Python file has a different name, replace main.py with that filename.
How to Use
1. Enter a crop name.
2. Enter the farm area in hectares.
3. Enter the yield in kilograms.
4. Click Add Plot to save the plot and display its productivity.
5. Click Update Yield to change the yield for an existing crop. Enter the crop name and the new yield; the most recently added matching crop record is updated.
6. Click Load Examples to replace the current records with the sample Rice, Cassava, and Maize records.
7. Click Clear Fields to empty the input boxes without deleting saved plot records.
Productivity Calculation
The application calculates productivity using:

Productivity = Yield (kg) ÷ Area (hectares)

For example, a plot with a yield of 3,500 kg and an area of 2 hectares has a productivity of 1,750 kg/hectare.
Input Validation
- Crop name must not be empty.
- Area must be greater than zero.
- Yield cannot be negative.
- The crop must already exist in the records before its yield can be updated.
Project Files
- main.py — the Python source code for the application.
- README.md — project information and setup instructions.
Notes
Plot records are stored in memory while the application is running. They are not saved to a database or file, so records will be lost when the application closes.
