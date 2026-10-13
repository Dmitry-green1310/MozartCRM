import flet



class Input(flet.TextField):
	def __init__(self, only_num = False, *args, **kwargs):

		self.field_regex = r'^[0-9]*$' if only_num else None

		super().__init__(
			cursor_height = 20, 
			text_vertical_align = flet.VerticalAlignment.CENTER,
			counter_style = flet.TextStyle(size = 0),
			input_filter = flet.InputFilter(allow = True, regex_string = self.field_regex),
			**kwargs
			)