from tkinter import *
import settings
import utilities
from cell import Cell

root = Tk()

# Create Window 
root.configure(bg='black')
root.title(f"{settings.WIDTH}x{settings.HEIGHT}")
root.geometry('1440x720')
root.resizable(False, False)

# Creation of Frames
top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utilities.height_percentage(25)
)
top_frame.place(x=0,y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)
game_title.place(
    x=utilities.width_percentage(25), y=0
)

left_frame = Frame(
    root,
    bg='black',
    width=utilities.width_percentage(25),
    height=utilities.height_percentage(75)
)
left_frame.place(x=0, y=utilities.height_percentage(25))

center_frame = Frame(
    root,
    bg='black',
    width=utilities.width_percentage(75),
    height=utilities.height_percentage(75)
)
center_frame.place(
    x=utilities.width_percentage(25), 
    y=utilities.height_percentage(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid( # Will take the center frame as the parent
            column=x,row=y
        )

# Call the label from Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0,y=0)

Cell.randomize_mines()

# Run window
root.mainloop()
