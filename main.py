from tkinter import *
import settings
import utilities
from cell import Cell

root = Tk()


def setDifficulty(difficulty):
    if(difficulty == "easy"):
        settings.GRID_SIZE = 6
        settings.CELL_COUNT = settings.GRID_SIZE ** 2
        settings.MINES_COUNT = (settings.CELL_COUNT) // 10
        settings.CELL_HEIGHT = 4
        settings.CELL_WIDTH = 12
        restart_game()
    elif(difficulty == "medium"):
        settings.GRID_SIZE = 8
        settings.CELL_COUNT = settings.GRID_SIZE ** 2
        settings.MINES_COUNT = (settings.CELL_COUNT) // 6
        settings.CELL_HEIGHT = 3
        settings.CELL_WIDTH = 9
        restart_game()
    elif(difficulty == "hard"):
        settings.GRID_SIZE = 10
        settings.CELL_COUNT = settings.GRID_SIZE ** 2
        settings.MINES_COUNT = (settings.CELL_COUNT) // 4
        settings.CELL_HEIGHT = 2
        settings.CELL_WIDTH = 6
        restart_game()

def create_grid():
    for x in range(settings.GRID_SIZE):
        for y in range(settings.GRID_SIZE):
            c = Cell(x, y)
            c.create_btn_object(center_frame)
            c.cell_btn_object.grid( # Will take the center frame as the parent
            column=x,row=y
            )

def delete_grid():
    # Get all the widgets in center_frame
    widgets = center_frame.grid_slaves()

    # Remove all the widgets from center_frame
    for widget in widgets:
        widget.destroy()

def create_count_label():
    # Call the label from Cell class
    Cell.cell_count_label_object = settings.CELL_COUNT
    Cell.create_cell_count_label(left_frame)
    Cell.cell_count_label_object.place(x=0,y=0)

def delete_count_label():
    Cell.cell_count_label_object.destroy()

def restart_game():
    delete_grid()
    Cell.delete_all_cell_objects()
    create_grid()
    if Cell.cell_count_label_object:
        Cell.reset_cell_count()
    Cell.randomize_mines()

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

# Difficulty buttons
btn_easy = Button(
    left_frame,
    width=15,
    height=5,
    text=f"Easy",
    command=lambda: setDifficulty("easy")
)
btn_easy.place(
    x=utilities.width_percentage(8.5), 
    y=utilities.height_percentage(12.5)
)

btn_medium = Button(
    left_frame,
    width=15,
    height=5,
    text=f"Medium",
    command=lambda: setDifficulty("medium")
)
btn_medium.place(
    x=utilities.width_percentage(8.5), 
    y=utilities.height_percentage(25)
)

btn_hard = Button(
    left_frame,
    width=15,
    height=5,
    text=f"Hard",
    command=lambda: setDifficulty("hard")
)
btn_hard.place(
    x=utilities.width_percentage(8.5), 
    y=utilities.height_percentage(37.5)
)

create_grid()

create_count_label()

Cell.randomize_mines()

# Run window
root.mainloop()
