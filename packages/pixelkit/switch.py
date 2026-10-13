import flet


@flet.control
class Switch(flet.Switch):
	def __init__(self, **kwargs):
		super().__init__(
			width = 30,
			height = 20,
			**kwargs
			)