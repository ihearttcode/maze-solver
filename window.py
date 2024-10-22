import tkinter as tk

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        # Create the main Tkinter window
        self.root = tk.Tk()
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
        # Set the size of the window
        self.root.geometry(f"{self.width}x{self.height}")
        
        # Boolean to determine state of redrawing the window
        self.running = False
        
        # Create the widgets (like canvas, buttons, etc.)
        self.create_widgets()
    
    def create_widgets(self):
        """Create the main widgets of the application"""
        # Create a canvas to draw the maze
        self.canvas = tk.Canvas(self.root, width=self.width - 100, height=self.height - 100, bg="white")
        self.canvas.pack(pady=20)
        
        # Create a button to start sovling the maze
        self.solve_button = tk.Button(self.root, text="Solve Maze", command=self.solve_maze)
        self.solve_button.pack()
        
    def redraw(self):
        """Clear and redraw the canvas"""
        self.root.update_idletasks()
        self.root.update()
        
    def wait_for_close(self):
        """Dynamically update the window"""
        self.running = True
        while self.running:
            self.redraw()
            
    def close(self):
        """Stop running processes"""
        print("Closing Maze Solver Window...")
        self.running = False
        self.root.destroy()
        print("Done")  
        
    def solve_maze(self):
        """Placeholder method to start solving the maze"""
        # Here we will eventually call the maze solving logic
        print("Solve button clicked - maze solving will be implemented here")
        
    def run(self):
        """Run the Tkinter main event loop."""
        self.root.mainloop()
        
# Create an instance of the window and run it
if __name__ == "__main__":
    app = Window(800, 600)
    app.run()