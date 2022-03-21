from tkinter import Tk


class Window:
    def __init__(self, title: str = "PyScript GUI", geometry: tuple = (500, 500), resizable=(True, True)):
        self.win = Tk()
        self.title_ = title
        self.geometry_ = geometry
        self.resizable_ = resizable
        self.win.title(self.title_)
        self.win.resizable(self.resizable_[1], self.resizable_[0])
        self.geo_str = self._geo_tuple_to_str()
        self.win.geometry(self.geo_str)

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
