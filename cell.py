from tkinter import Button, Label, messagebox
import random
import settings
#import utilities
#import ctypes
#import sys

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    def __init__(self,x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_flag_marked = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        
        # Append the object to the Cell.all List
        Cell.all.append(self)


    def create_btn_object(self, location):
        btn = Button(
            location,
            width=settings.CELL_WIDTH,
            height=settings.CELL_HEIGHT
        )
        btn.bind('<Button-1>', self.left_click_actions) # Left Click
        btn.bind('<Button-3>', self.right_click_actions) # Right Click
        self.cell_btn_object = btn
    
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells left: {Cell.cell_count}",
            font=("",25)
        )
        Cell.cell_count_label_object = lbl
    
    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # If mines count == cells left count, player won
            if Cell.cell_count == settings.MINES_COUNT:
                messagebox.showinfo("You won :D", "You won the game, congrats.")
                for cell in Cell.all:
                    cell.cell_btn_object.unbind('<Button-1>')
                    cell.cell_btn_object.unbind('<Button-3>')
                #ctypes.windll.user32.MessageBoxW(0, 'You won the game! :D Congrats', 'Game Over', 0)
        
        # Cancel left and right click events if cell is opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')
    
    def get_cell_by_axis(self, x, y):
        # return a cell object based on the value of x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property # We can now use this as an attribute
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        # We must insert all the surrounded cells again, but without None objects
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter
    
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # Update the text of cell count label
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells left: {Cell.cell_count}"
                )
            # If this was marked as a marked_flag, must update to the default color
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
        # Mark the cell as opened
        self.is_opened = True

        if self.surrounded_cells_mines_length == 0:
            for cell in self.surrounded_cells:
                if not cell.is_opened:
                 cell.show_cell()

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        messagebox.showinfo("You lost", "You lose, try again!")
        #ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        
        for cell in Cell.all:
            cell.cell_btn_object.unbind('<Button-1>')
            cell.cell_btn_object.unbind('<Button-3>')
        

    def right_click_actions(self, event):
        if not self.is_flag_marked:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_flag_marked = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace' #Set the default color if it was marked already
            )
            self.is_flag_marked = False
    
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT # 9 Cells will be converted into mines
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    @staticmethod
    def delete_all_cell_objects():
        del Cell.all[:]
    
    @staticmethod
    def reset_cell_count():
        Cell.cell_count = settings.CELL_COUNT
        if Cell.cell_count_label_object:
            Cell.cell_count_label_object.configure(
                text=f"Cells left: {Cell.cell_count}"
            )

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"

    