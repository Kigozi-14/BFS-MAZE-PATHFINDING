import collections
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MazeGrid(GridLayout):           
    maze = [[1, 1, 1, 1, 0, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 1], 
           [0, 1, 0, 1, 0, 0, 1, 0, 0], 
           [0, 0, 0, 1, 1, 0, 0, 1, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 2, 1, 1, 1, 1]]

    def find_path(self, start, end):
        rows, cols = len(self.maze), len(self.maze[0])
        q = collections.deque()
        visited = set() 
        q.append([start])  
        visited.add(start)
        found_path = []
        blocks = set()

        while q and end not in visited:
            a = q.popleft()
            sa, sb = a[-1]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for i in range(0, len(directions)):
                dr, dc = directions[i]
                sdr, sdc = (sa+dr), (sb+dc)
                if sdr in range(rows) and sdc in range(cols) and (sdr, sdc) not in visited:
                    if self.maze[sdr][sdc] == 1:
                        blocks.add((sdr, sdc))
                    if self.maze[sdr][sdc] == 0:
                        newlist = a.copy()
                        newlist.append((sdr, sdc))
                        q.append(newlist)
                        visited.add((sdr, sdc))
                    elif self.maze[sdr][sdc] == 2:
                        final_path = a.copy()
                        final_path.append((sdr, sdc))
                        found_path.append(final_path)
        return found_path[0]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze[i])):
                if self.maze[i][j] == 1:
                    b = Button(background_color="blue")
                    self.add_widget(b)
                else:
                    b = Button(background_color="white")
                    self.add_widget(b)
                
                for cr, cc in self.find_path((0, 4), (7, 4)):
                    if (cr, cc) == (i, j):
                        b.background_color="green"
class MazeApp(App):
    def build(self):
        Builder.load_file("./visual.kv")
        return MazeGrid()

if __name__ := "__main__":
    MazeApp().run()

    