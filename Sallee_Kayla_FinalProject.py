"""Author: Kayla Sallee
Purpose: This Python program helps users find and save therapists based on their gender and specialty preferences, 
providing an intuitive interface and therapist details for easy access.
<a href="https://www.flaticon.com/free-icons/therapist" title="therapist icons">Therapist icons created by Good Ware - Flaticon</a>
"""

import tkinter as tk
from tkinter import ttk
from breezypythongui import EasyFrame
from tkinter import PhotoImage, Menu, StringVar, Radiobutton, Canvas, Scrollbar

# Therapist data
therapists = [
    {"name": "Dr. John Smith", "specialty": "Anxiety", "gender": "Male", "address": "123 Main St", "phone": "555-123-4567"},
    {"name": "Dr. Sarah Lee", "specialty": "Anxiety", "gender": "Female", "address": "456 Elm St", "phone": "555-987-6543"},
    {"name": "Dr. Mark Green", "specialty": "Depression", "gender": "Male", "address": "789 Oak St", "phone": "555-456-7890"},
    {"name": "Dr. Emily White", "specialty": "Depression", "gender": "Female", "address": "101 Pine St", "phone": "555-654-3210"},
    {"name": "Dr. James Miller", "specialty": "PTSD", "gender": "Male", "address": "202 Birch St", "phone": "555-111-2222"},
    {"name": "Dr. Amanda Brown", "specialty": "Substance Abuse", "gender": "Female", "address": "303 Cedar St", "phone": "555-333-4444"},
    {"name": "Dr. Robert Brown", "specialty": "Stress", "gender": "Male", "address": "404 Maple St", "phone": "555-555-6666"},
    {"name": "Dr. Linda Black", "specialty": "Anxiety", "gender": "Female", "address": "789 Maple St", "phone": "555-888-9999"},
    {"name": "Dr. George White", "specialty": "Anxiety", "gender": "Male", "address": "321 Cherry St", "phone": "555-444-8888"},
    {"name": "Dr. Patricia Young", "specialty": "Anxiety", "gender": "Non-binary", "address": "654 Cypress St", "phone": "555-222-7777"},
]

# Global variable to save selected therapists
saved_therapists = []

class MindMatchApp(EasyFrame):
    def __init__(self):
        super().__init__(title="MindMatch", width=800, height=600, background="#e6e6fa")
        self.gender_var = StringVar(value="Any")
        self.specialty_var = None

        # Load the logo image
        try:
            self.logo_image = PhotoImage(file="mindmatch_logo.gif")
        except Exception as e:
            print(f"Error loading logo: {e}")
            self.logo_image = None

        self.create_main_screen()

    def create_main_screen(self):
        """Main screen with Find a Therapist button."""
        self.clear_screen()

        # Add "Welcome to" text and logo side by side
        tk.Label(self, text="Welcome to", font=("Arial", 20), background="#e6e6fa").grid(row=0, column=0, sticky="E", padx=10, pady=20)

        if self.logo_image:
            tk.Label(self, image=self.logo_image, background="#e6e6fa").grid(row=0, column=1, sticky="W", padx=10, pady=20)

        find_button = tk.Button(self, text="Find a Therapist", command=self.show_gender_specialty_screen, font=("Arial", 14))
        find_button.grid(row=1, column=0, columnspan=2, pady=20)

        self.create_hamburger_menu(back_command=None)

    def clear_screen(self):
        """Clears all widgets from the current frame."""
        for widget in self.winfo_children():
            widget.destroy()

    def create_hamburger_menu(self, back_command=None):
        """Creates a hamburger menu visible on all screens."""
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        main_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="☰", menu=main_menu)

        main_menu.add_command(label="Home", command=self.create_main_screen)

        if back_command:
            main_menu.add_command(label="Back", command=back_command)

        main_menu.add_command(label="View Saved Therapists", command=self.show_saved_therapists_screen)

    def show_gender_specialty_screen(self):
        """Placeholder for navigating to the next screen."""
        print("Gender and Specialty selection screen.")

    def show_saved_therapists_screen(self):
        """Placeholder for displaying saved therapists."""
        print("Saved therapists screen.")

if __name__ == "__main__":
    MindMatchApp().mainloop()
