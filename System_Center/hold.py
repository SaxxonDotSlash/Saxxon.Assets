import tkinter as tk
from tkinter import ttk
import json

IDEAS_DATA_FILE = 'System_Center/ideas.json'
PROJECTS_DATA_FILE = 'System_Center/projects.json'
DETAILS_DATA_FILE = 'System_Center/details.json'

def save_data_ideas():
    ideas = ideas_listbox.get(0, tk.END)
    data = {'ideas': list(ideas)}
    with open(IDEAS_DATA_FILE, 'w') as file:
        json.dump(data, file)

def load_data_ideas():
    try:
        with open(IDEAS_DATA_FILE, 'r') as file:
            data = json.load(file)
            for idea in data.get('ideas', []):
                ideas_listbox.insert(tk.END, idea)
    except FileNotFoundError:
        pass

def save_data_projects():
    data = {'projects': projects}
    with open(PROJECTS_DATA_FILE, 'w') as file:
        json.dump(data, file)

def load_data_projects():
    try:
        with open(PROJECTS_DATA_FILE, 'r') as file:
            data = json.load(file)
            for project in data.get('projects', []):
                projects.append(project)
                projects_combobox['values'] = projects
    except FileNotFoundError:
        pass

def save_project_details(details):
    try:
        with open(DETAILS_DATA_FILE, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data[details['Project Name']] = details

    with open(DETAILS_DATA_FILE, 'w') as file:
        json.dump(data, file)

def load_project_details(project_name):
    try:
        with open(DETAILS_DATA_FILE, 'r') as file:
            data = json.load(file)
            return data.get(project_name, {})
    except FileNotFoundError:
        return {}

def add_idea():
    idea = idea_entry.get()
    ideas_listbox.insert(tk.END, idea)
    idea_entry.delete(0, tk.END)
    save_data_ideas()

def remove_idea():
    selected_index = ideas_listbox.curselection()
    if selected_index:
        ideas_listbox.delete(selected_index)
        save_data_ideas()

def addProject():
    selected_index = ideas_listbox.curselection()
    if selected_index:
        selected_idea = ideas_listbox.get(selected_index)
        projects.append(selected_idea)
        projects_combobox['values'] = projects
        ideas_listbox.delete(selected_index)
        save_data_ideas()
        save_data_projects()
        print(f"Added project: {selected_idea}")

def on_project_selected(event):
    selected_project = projects_combobox.get()
    display_project_details(selected_project)

def display_project_details(project_name):
    #Project Overview
    details = load_project_details(project_name)
    project_name_var.set(details.get("Project Name", ""))
    project_manager_var.set(details.get("Project Manager", ""))
    start_date_var.set(details.get("Start Date", ""))
    end_date_var.set(details.get("End Date", ""))
    project_description_var.set(details.get("Project Description", ""))

    #Project Goals and Objectives
    goals_var.set(details.get("Goals", ""))
    objectives_var1.set(details.get("Objectives", ""))
    objectives_var2.set(details.get("Objectives", ""))
    objectives_var3.set(details.get("Objectives", ""))
    objectives_var4.set(details.get("Objectives", ""))
    objectives_var5.set(details.get("Objectives", ""))
    
    #Scope Statement
    in_scope_var.set(details.get("In Scope", ""))
    out_scope_var.set(details.get("Out Scope", ""))

    #Deliverables
    deliverables_var1.set(details.get("Deliverables", ""))
    deliverables_var2.set(details.get("Deliverables", ""))
    deliverables_var3.set(details.get("Deliverables", ""))


def save_details():
    details = {
        #Project Overview
        "Project Name": project_name_var.get(),
        "Project Manager": project_manager_var.get(),
        "Start Date": start_date_var.get(),
        "End Date": end_date_var.get(),
        "Project Description": project_description_var.get(),

        #Project Goals and Objective
        "Goals": goals_var.get(),
        "Objectives": objectives_var1.get(),
        "Objectives": objectives_var2.get(),
        "Objectives": objectives_var3.get(),
        "Objectives": objectives_var4.get(),
        "Objectives": objectives_var5.get(),

        #Scope Statement
        "In Scope": in_scope_var.get(),
        "Out Scope": out_scope_var.get(),

        #Deliverables
        "Deliverables": deliverables_var1.get(),
        "Deliverables": deliverables_var2.get(),
        "Deliverables": deliverables_var3.get(),
    }
    save_project_details(details)

# Create the main window
root = tk.Tk()
root.title("Project Manager")
root.geometry("800x600")

window_width = root.winfo_screenwidth()
left_frame_width = int(window_width * 0.25)
right_frame_width = int(window_width * 0.75)

# Create the left section
left_frame = tk.Frame(root, width=left_frame_width)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

ideas_label = tk.Label(left_frame, text="Ideas")
ideas_label.pack()

ideas_listbox = tk.Listbox(left_frame)
ideas_listbox.pack(fill=tk.BOTH, expand=True)

idea_entry = tk.Entry(left_frame)
idea_entry.pack()

add_button = tk.Button(left_frame, text="Add Idea", command=add_idea)
add_button.pack()

remove_button = tk.Button(left_frame, text="Remove Idea", command=remove_idea)
remove_button.pack()

addProject_button = tk.Button(left_frame, text="Add Project", command=addProject)
addProject_button.pack()

# Create the right section
right_frame = tk.Frame(root, width=right_frame_width)
right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

projects_label = tk.Label(right_frame, text="Projects")
projects_label.pack()

projects = []  # List to store projects

projects_combobox = ttk.Combobox(right_frame, values=projects)
projects_combobox.pack()
projects_combobox.bind("<<ComboboxSelected>>", on_project_selected)

# Variables to hold project details
project_name_var = tk.StringVar()
project_manager_var = tk.StringVar()
start_date_var = tk.StringVar()
end_date_var = tk.StringVar()
project_description_var = tk.StringVar()
goals_var = tk.StringVar()
objectives_var1 = tk.StringVar()
objectives_var2 = tk.StringVar()
objectives_var3 = tk.StringVar()
objectives_var4 = tk.StringVar()
objectives_var5 = tk.StringVar()
in_scope_var = tk.StringVar()
out_scope_var = tk.StringVar()
deliverables_var1 = tk.StringVar()
deliverables_var2 = tk.StringVar()
deliverables_var3 = tk.StringVar()


# Display project details
tk.Label(right_frame, text="Project Name").pack()
tk.Entry(right_frame, textvariable=project_name_var).pack()

tk.Label(right_frame, text="Project Manager").pack()
tk.Entry(right_frame, textvariable=project_manager_var).pack()

tk.Label(right_frame, text="Start Date").pack()
tk.Entry(right_frame, textvariable=start_date_var).pack()

tk.Label(right_frame, text="End Date").pack()
tk.Entry(right_frame, textvariable=end_date_var).pack()

tk.Label(right_frame, text="Project Description").pack()
tk.Entry(right_frame, textvariable=project_description_var).pack()

save_button = tk.Button(right_frame, text="Save", command=save_details)
save_button.pack()

# Load data from the JSON files into the listbox and combobox
load_data_ideas()
load_data_projects()

# Start the main event loop
root.mainloop()