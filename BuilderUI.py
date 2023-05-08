import tkinter
import tkinter.messagebox
import customtkinter
import os
import time
from tkinter import *
from tkinter import messagebox
from PIL import Image



customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Nexus Rat | veal#0001 | Monkeys DONT SKID ")
        self.geometry(f"{1100}x{500}")
        self.iconbitmap(r"./assets/nexus.ico")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets/")
        self.basefilepath = os.path.dirname(str(os.path.realpath(__file__)))
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "nexus.ico")), size=(60, 60))      
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "nexus.ico")), size=(20, 20))
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.sidebar_frame, text=" Nexus RAT", image=self.logo_image, compound="left")
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, 
                                                        text="Compile",
                                                        border_color="white", 
                                                        fg_color="#f300ff", 
                                                        command=self.sidebar_button_event)
        
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        #self.progress_bar_1 = customtkinter.CTkProgressBar(self.sidebar_frame, 
        #                                                   orientation="horizontal", 
        #                                                   fg_color="#f300ff")
        #self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10)

        

        #self.checkbox1 = customtkinter.CTkCheckBox(self.sidebar_frame, 
        #                                           text="Backgorund Pth", 
        #                                           fg_color="#f300ff")
        #
        #self.checkbox1.grid(row=2, column=0, padx=15, pady=10)

        self.checkbox2 = customtkinter.CTkCheckBox(self.sidebar_frame, 
                                                   text="Bind Stealer", 
                                                   fg_color="#f300ff",)
        
        self.checkbox2.grid(row=3, column=0, padx=15, pady=10)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Dev veal#1337", font=customtkinter.CTkFont(size=13, weight="bold"))
        self.logo_label.grid(row=4, column=0, padx=20, pady=(20, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, 
                                                            text="Appearance Mode:", 
                                                            anchor="w", )
        
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, 
                                                                       values=["Light", "Dark", "System"], 
                                                                       fg_color="#f300ff", 
                                                                       command=self.change_appearance_mode_event)
        
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, 
                                                    text="UI Scaling:", 
                                                    anchor="w")
        
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, 
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               fg_color="#f300ff", 
                                                               command=self.change_scaling_event)
        
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

       
        self.entry1 = customtkinter.CTkEntry(self, 
                                             height=10, 
                                             placeholder_text="Bot Token here",
                                             text_color="#f300ff")
        self.entry1.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.entry2 = customtkinter.CTkEntry(self, 
                                             height=10, 
                                             placeholder_text="Server ID here", 
                                             text_color="#f300ff")
        
        self.entry2.grid(row=2, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.entry3 = customtkinter.CTkEntry(self, 
                                             height=10, 
                                             placeholder_text="Custom Background Path here",
                                             text_color="#f300ff")
        
        self.entry3.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.entry4 = customtkinter.CTkEntry(self, 
                                             placeholder_text="File Name",
                                             text_color="#f300ff")
        
        self.entry4.grid(row=4, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        
        self.textbox = customtkinter.CTkTextbox(self, width=50, font=customtkinter.CTkFont(size=12, weight="bold"))
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0", "FUNCTIONS OF Nexus RAT\n\n\nAnti-VM // will not execute in a Virtual environment Set to True as Default\n\n!startup // Adds its self to Startup\n\nAnti Dnspy\n\nHIDE-CONSOLE // Hides CMD Pannel\n\n!killall // Blue screen\n\n")


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def error_log(self, error):
        with open("error.txt", "w") as f:
            f.write(str(error))
            f.close()

    def sidebar_button_event(self):
            window = Tk()
            window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
            window.withdraw()
            messagebox.showinfo('Success', f'{self.entry4.get()} Is Being built Please be paitent As this might take some time')
            window.deiconify()
            window.destroy()
            window.quit()
            with open("./src/Nexus.py", "r", encoding="utf-8") as f:
                raw = f.read()
            with open(f"{self.entry4.get()}.py", "w", encoding="utf-8") as f:
                f.write(raw.replace("TOKENHERE", self.entry1.get()))
            with open(f"{self.entry4.get()}.py", "r", encoding="utf-8") as f:
                raw = f.read()
            with open(f"{self.entry4.get()}.py", "w", encoding="utf-8") as f:
                f.write(raw.replace("SERVER_ID_HERE", self.entry2.get()))
            with open(f"{self.entry4.get()}.py", "r", encoding="utf-8") as f:
                raw = f.read()
            with open(f"{self.entry4.get()}.py", "w", encoding="utf-8") as f:
                f.write(raw.replace("IMAGE_PATH_HERE", self.entry3.get()))
            time.sleep(2)
            
            os.system(f"pyinstaller --onefile --noconsole  --icon assets/nexus.ico --distpath ./ .\{self.entry4.get()}.py")
            os.remove(f".\{self.entry4.get()}.py")
            os.remove(f".\{self.entry4.get()}.spec")

if __name__ == "__main__":
    app = App()
    app.mainloop()