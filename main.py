import tkinter as tk
from tkinter import filedialog

import pandas as pd

# Create the main window
window = tk.Tk()
window.title("CSV Data Correlation")
window.geometry("600x700")

# change background color of window to Black
window.configure(background='black')


def upload_csv():
    # Save the dataframe to a global variable
    global df
    file_path = filedialog.askopenfilename()
    df = pd.read_csv(file_path)
    headers = list(df.columns)
    # if statement to check if data has been loaded before and if true deletes existing headers
    if datapoint_dropdown.size() > 0:
        datapoint_dropdown.delete(0, tk.END)
    # Create a dropdown to select the primary datapoint
    for header in headers:
        datapoint_dropdown.insert(tk.END, header)
    return df


# Create a button to upload a CSV file
upload_button = tk.Button(text="Upload .csv file", command=upload_csv, bg="black", fg="green", activebackground="green",
                          activeforeground="black")
upload_button.pack()


# Create a dropdown to select the primary datapoint
def select_datapoint(event):
    global selected_datapoint
    # get the value from the selected datapoint
    selected_datapoint = datapoint_dropdown.get(datapoint_dropdown.curselection())
    return selected_datapoint


datapoint_label = tk.Label(text="Select primary datapoint:", bg="black", fg="green")
datapoint_label.pack()
datapoint_dropdown = tk.Listbox(bg="black", fg="green", activestyle="none", selectbackground="green",)
datapoint_dropdown.pack()

# Bind the dropdown to the "select_datapoint" function
datapoint_dropdown.bind("<<ListboxSelect>>", select_datapoint)

# Create an output window with a grew background
output_label = tk.Label(text="Output:", bg="black", fg="green")
output_label.pack()
output_text = tk.Text(bg='black', fg='green', cursor='arrow')
output_text.pack()


# Function to print the correlations
def show_correlations():
    try:
        primary_datapoint = selected_datapoint
        if var1.get() == 1:
            output_text.delete(1.0, tk.END)
        # Display the correlations and remove type data
        correlations = df.corr()[primary_datapoint].drop(primary_datapoint)
        output_text.insert(tk.END, correlations)
        output_text.insert(tk.END, "\n")
        output_text.see("end")
    except NameError:
        # create a popup window to tell user to select a datapoint
        popup = tk.Tk()
        popup.wm_title("Error")
        label = tk.Label(popup, text="Please select a datapoint")
        label.pack()
        # make popup window in the center of the app window
        popup.geometry(f"+{window.winfo_x() + 100}+{window.winfo_y() + 100}")


# create tkinter checkbox
var1 = tk.IntVar()
check_box = tk.Checkbutton(text="Delete past Correlations?", variable=var1, onvalue=1, offvalue=0, bg="black",
                           fg="green", activebackground="green", activeforeground="black")
check_box.pack()


# Create a button to display the correlations
correlations_button = tk.Button(text="Show correlations", command=show_correlations, bg="black", fg="green",
                                activebackground="green", activeforeground="black")
correlations_button.pack()

# Run the main loop
window.mainloop()
