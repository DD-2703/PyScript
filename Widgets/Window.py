from tkinter import Tk


class Window:
    def __init__(self, title: str = "PyScript GUI", geometry: tuple = (500, 500), resizable: tuple = (True, True),
                 place: tuple = (400, 400)):

        self.win = Tk()
        self.title_ = title
        self.geometry_ = geometry
        self.resizable_ = resizable
        self.place1 = str(place[0])
        self.place2 = str(place[1])
        self.place_ = "+" + self.place1 + "+" + self.place2

        self.win.title(self.title_)
        self.win.resizable(self.resizable_[1], self.resizable_[0])
        self.geo_str = self._geo_tuple_to_str()
        self.win.geometry(self.geo_str + self.place_)

    def run(self):
        self.win.mainloop()

    def _geo_tuple_to_str(self):
        result = ""
        if len(self.geometry_) >= 3:
            from Exceptions.UnexpectedValueError import UnexpectedValueError
            raise UnexpectedValueError("More than 2 Values Found in Geometry Parameter.")
        else:
            result += str(self.geometry_[0])
            result += "x"
            result += str(self.geometry_[1])
        return result

    def geometry(self, param: tuple):
        self.geometry_ = param
        self.geo_str = self._geo_tuple_to_str()
        self.win.geometry(self.geo_str)

    def geo(self, param: tuple):
        self.geometry(param)

    def resizable(self, height: bool, width: bool):
        self.win.resizable(width, height)
        self.resizable_ = (width, height)

    def place(self, x: int, y: int):
        self.win.geometry(self.win.geometry.join("+", x, "+", y))

    def center_window(self):
        screen_width = self.win.winfo_screenwidth()
        screen_height = self.win.winfo_screenheight()
        coordinate_x = int(screen_width/2 - self.geometry_[0]/2)
        coordinate_y = int(screen_height/2 - self.geometry_[1]/2)
        self.win.geometry(f"{self.geometry_[0]}x{self.geometry_[1]}+{coordinate_x}+{coordinate_y}")
