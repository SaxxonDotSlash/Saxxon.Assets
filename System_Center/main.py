import customtkinter
from PIL import Image, ImageTk
import json
import tkinter as tk
from customtkinter import CTkImage


# Set the default color theme
customtkinter.set_default_color_theme("C:/Users/james/Desktop/Code/System_Center/autumn.json")

# Path Variables
IDEAS_DATA_FILE = 'System_Center/ideas.json'
PROJECTS_DATA_FILE = 'System_Center/projects.json'
DETAILS_DATA_FILE = 'System_Center/details.json'

# Get the screen size
def get_screen_size():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    print(screen_width, screen_height)

class LoginWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x200")

        #Username and Password Entry/Labels
        self.label = customtkinter.CTkLabel(self, text="Username")
        self.label.pack()
        self.username_entry = customtkinter.CTkEntry(self)
        self.username_entry.pack() 

        self.label = customtkinter.CTkLabel(self, text="Password")
        self.label.pack()
        self.password_entry = customtkinter.CTkEntry(self, show="*")
        self.password_entry.pack()

        #Error Label
        self.error_label = customtkinter.CTkLabel(self, text="")
        self.error_label.pack()

        #Login Button
        self.login_button = customtkinter.CTkButton(self, text="Login", command=self.login)
        self.login_button.pack()
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Check if the credentials are correct
        if username == "admin" and password == "password":  ###CHANGE THIS TO CHECK AGAINST ENCRYPTED FILE###
            # Destroy the login window and open the main window
            self.destroy()
            self.open_main_window()
        else:
            self.error_label.configure(text="Invalid Credentials")
            
    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.mainloop()
    


# Main Window Class
class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.geometry("800x600")

        ### Main Window Widgets ###

        # Configure grid layout
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)

        # Form Buttons
        self.buttons = []
        for i in range(15):
            button = customtkinter.CTkButton(self, text="")
            button.grid(row=i//4, column=i%4, padx=10, pady=10, sticky="nsew")
            self.buttons.append(button)

        # Project Manager Button - Using CTkImage
        self.pm_image_path = "pm.png"
        self.pm_image = CTkImage(Image.open(self.pm_image_path).resize((200, 200), Image.LANCZOS))

        self.project_manager_button = customtkinter.CTkButton(self, image=self.pm_image, text="", command=self.open_project_manager)
        self.project_manager_button.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")

        # Bind the resize event
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        # Calculate the size of each button to maintain a square aspect ratio
        size = min(event.width // 4, event.height // 4)
        if size > 0:  # Ensure size is greater than 0
            for button in self.buttons:
                button.configure(width=size, height=size)
            self.project_manager_button.configure(width=size, height=size)

            # Resize the image to fit the button
            pm_image_pil = Image.open(self.pm_image_path).resize((size, size), Image.LANCZOS)
            self.pm_image = CTkImage(pm_image_pil)
            self.project_manager_button.configure(image=self.pm_image)

    def open_project_manager(self):
        self.destroy()
        self.project_manager = ProjectManager()
        self.project_manager.mainloop()



# Project Manager Class
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


root = LoginWindow()
root.mainloop()