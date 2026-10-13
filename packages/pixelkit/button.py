import flet



@flet.control
class Button(flet.Button):
	def __init__(self, **kwargs):
		kwargs.setdefault('width', 200)
		kwargs.setdefault('height', 40)
		super().__init__(
			style = flet.ButtonStyle(shape = flet.RoundedRectangleBorder(radius = 0)),
			**kwargs
			)