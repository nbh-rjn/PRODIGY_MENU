import tkinter as tk
from tkinter import messagebox
import subprocess
from pygame import mixer

def run_file(file_name):
    try:
        subprocess.run(["python", file_name], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error running {file_name}: {e}")


def menu_selection(choice):
    if choice == "t1":
        run_file("PRODIGY_SD_01.py")
    elif choice == "t2":
        run_file("PRODIGY_SD_02.py")
    elif choice == "t3":
        run_file("PRODIGY_SD_03.py")
    elif choice == "t4":
        run_file("PRODIGY_SD_03.py")
    elif choice == "Exit":
        root.destroy()


def main():
    mixer.init()
    mixer.music.load("lullaby.mp3")
    mixer.music.play(loops=-1)

    global root

    root = tk.Tk()
    root.title("Prodigy InfoTech SD Internship Tasks")
    root.geometry("600x450")

    # Set background color
    root.configure(bg="#001F3F")

    background_image = tk.PhotoImage(file="bg_image.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    menu = tk.Menu(root)
    root.config(menu=menu)

    script_menu = tk.Menu(menu, tearoff=0, font=("Helvetica", 14))
    menu.add_cascade(label="Tasks", menu=script_menu)

    # Set menu background and foreground color
    script_menu.configure(bg="#001F3F", fg="cyan")

    script_menu.add_command(label="Temperature Converter", command=lambda: menu_selection("t1"),
                            font="Consolas", background="#54434D", foreground="white")
    script_menu.add_command(label="Number Guessing Game", command=lambda: menu_selection("t2"),
                            font="Consolas", background="#54434D", foreground="white")
    script_menu.add_command(label="Sudoku Solver", command=lambda: menu_selection("t3"),
                            font="Consolas", background="#54434D", foreground="white")
    script_menu.add_command(label="Web Scraper", command=lambda: menu_selection("t4"),
                            font="Consolas", background="#54434D", foreground="white")
    script_menu.add_separator()
    script_menu.add_command(label="Exit", command=lambda: menu_selection("Exit"),
                            font="Consolas", background="#54434D", foreground="white")

    title = tk.Label(root, text=" Nabiha Rajani "
                                " \n Software Development Internship Tasks "
                                " \n Prodigy InfoTech",
                                font=("Consolas", 16, 'bold'), bg="#54434D", fg='white')
    title.place(relx=0.5, rely=0.25, anchor = tk.CENTER)

    root.mainloop()


if __name__ == "__main__":
    main()
