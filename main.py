from tkinter import *
import settings


'''-----------------EJECUCION----------------------'''
root = Tk()

# Create Window
root.configure(bg='black')
root.title(f"{settings.WIDTH}x{settings.HEIGHT}")
root.geometry('1440x720')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='grey',
    width=1440,
    height=180
)
top_frame.place(x=0,y=0)

left_frame = Frame(
    root,
    bg='grey',
    width=360,
    height=720
)
left_frame.place(x=0,y=180)

# Run window
root.mainloop()