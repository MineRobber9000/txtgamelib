from curses import wrapper
class Menu:
	def __init__(self):
		pass
	def draw_menu(self,stdscr):
		stdscr.clear()
		stdscr.refresh()
	def start(self):
		return wrapper(self.draw_menu)
