import customtkinter
import json
import tkinter as tk

customtkinter.set_default_color_theme("C:/Users/james/Desktop/Code/System_Center/autumn.json")

# Path Variables
IDEAS_DATA_FILE = 'System_Center/ideas.json'
PROJECTS_DATA_FILE = 'System_Center/projects.json'
DETAILS_DATA_FILE = 'System_Center/details.json'



# Main Window Class
class ProjectManager(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Project Manager")
        self.geometry("800x600")

        # Set frame variables
        window_width = self.winfo_screenwidth()
        left_frame_width = int(window_width * 0.2)
        right_frame_width = int(window_width * 0.8)

        # Create frames
        self.left_frame = customtkinter.CTkFrame(self, width=left_frame_width)
        self.left_frame.pack(side="left", fill="both", expand=False)
        self.right_frame = customtkinter.CTkFrame(self, width=right_frame_width)
        self.right_frame.pack(side="left", fill="both", expand=True)

        # Create left frame widgets
        self.ideas_label = customtkinter.CTkLabel(self.left_frame, text="Ideas")
        self.ideas_label.pack()
        
        self.ideas_listbox = tk.Listbox(self.left_frame, background="peach puff", font=("Arial", 14))
        self.ideas_listbox.pack(fill="both", expand=True)

        self.idea_entry = customtkinter.CTkEntry(self.left_frame)
        self.idea_entry.pack()

        self.add_button = customtkinter.CTkButton(self.left_frame, text="Add Idea", command=self.add_idea)
        self.add_button.pack()

        self.remove_button = customtkinter.CTkButton(self.left_frame, text="Remove Idea", command=self.remove_idea)
        self.remove_button.pack()

        self.addProject_button = customtkinter.CTkButton(self.left_frame, text="Add Project", command=self.add_project)
        self.addProject_button.pack()

        # Create right frame widgets
        self.projects_label = customtkinter.CTkLabel(self.right_frame, text="Projects")
        self.projects_label.pack()

        # Create option menu with project names
        projects = ['placeholder']
        self.projects_option_menu = customtkinter.CTkOptionMenu(self.right_frame, values=projects)
        self.projects_option_menu.pack()

        # Initialize/Update data
        self.load_ideas()
        self.load_projects()

    # Save projects to projects.json file
    def save_projects(projects):
        data = {'projects': projects}
        with open(PROJECTS_DATA_FILE, 'w') as file:
            json.dump(data, file)

    # Load projects from projects.json file
    def load_projects(self):
        try:
            with open(PROJECTS_DATA_FILE, 'r') as file:
                data = json.load(file)
                return data['projects']
        except FileNotFoundError:
            return []
    
    # Load ideas from ideas.json file
    def load_ideas(self):
        try:
            with open(IDEAS_DATA_FILE, 'r') as file:
                data = json.load(file)
                return data['ideas']
        except FileNotFoundError:
            print("File not found")

    # Save idea to ideas.json file
    def add_idea(self):
        ideas = list(self.ideas_listbox.get(0, tk.END))
        new_idea = self.idea_entry.get()
        if new_idea:
            ideas.append(new_idea)
            self.ideas_listbox.insert("end", new_idea)
            self.idea_entry.delete(0, tk.END)
        data = {'ideas': ideas}
        with open(IDEAS_DATA_FILE, 'w') as file:
            json.dump(data, file)
    
    # Remove idea from ideas.json file
    def remove_idea(self):
        ideas = self.ideas_listbox.get(0, tk.END)
        ideas.remove(self.ideas_listbox.get(tk.ACTIVE))
        self.ideas_listbox.delete(tk.ACTIVE)
        data = {'ideas': list(ideas)}
        with open(IDEAS_DATA_FILE, 'w') as file:
            json.dump(data, file)

    # Add project to projects.json file
    def add_project(self):
        project = self.idea_entry.get()
        self.projects_option_menu.add_value(project)
        self.idea_entry.delete(0, tk.END)
        projects = self.load_projects()
        projects.append(project)
        self.save_projects(projects)

    


# Initialize ProjectManager class
root = ProjectManager()
root.mainloop()