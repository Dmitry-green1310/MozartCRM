import flet
import asyncio
from packages.pixelkit.button import Button
from packages.pixelkit.input import Input

x = "jcdeuhvlwfxovxpf"

@flet.component
def mail_code_screen():

	code_length = 6
	inputed_code, set_inputed_code = flet.use_state('')
	code_saver, set_code_saver = flet.use_state(['', '', '', '', '', ''])

	async def next_step():
		await flet.context.page.push_route('/account-recovery/password-recovery')



	async def code_input_autofocus_switcher(e, field_index):
		controls = e.control.parent.controls
		field_value = e.control.value
		max_field_index = len(controls) - 1

		x.join(field_value)

		# Все сслыки на поля должны идти в порядке возрастания

		# Если текущий индкес поля не равен максимальному индексу и  поле не пустое - сфокусироваться на следующей ячейке
		if field_index != max_field_index and field_value != '':
			await controls[field_index + 1].focus()

		if (field_value == '' or field_value == None) and field_index != 0:
			await controls[field_index - 1].focus()
		if field_index == max_field_index:
			save_coder(controls)


	def save_coder(controls):
		#full_code = "".join([field.value for field in controls if field.value])
		set_inputed_code(x)
		print(inputed_code)


	def save_code(d): pass


	mail_code_content = flet.Container(
			expand = True,
			alignment = flet.Alignment.CENTER,
			content = flet.Container(
				width = 600,
				height = 600,
				alignment = flet.Alignment.CENTER,
				content = flet.Column(
					expand = True,
					alignment = flet.MainAxisAlignment.CENTER,
					horizontal_alignment = flet.CrossAxisAlignment.CENTER,
					controls = [
						flet.Text('Восстановление пароля', size = 27, text_align = flet.TextAlign.CENTER),
						flet.Text('Введите код который мы отправили вам на электронную почту', size = 12),
						flet.Row(
							alignment = flet.MainAxisAlignment.CENTER,
							vertical_alignment = flet.CrossAxisAlignment.CENTER,
							controls = [
								Input(
									width = 50, 
									height = 50, 
									autofocus = True, 
									max_length = 1,
									on_blur = lambda e: save_code(e.control.parent.controls),
									on_change = lambda e: flet.context.page.run_task(code_input_autofocus_switcher, e, field_index = 0)
								),
								Input(
									width = 50, 
									height = 50, 
									max_length = 1,
									on_blur = lambda e: save_code(e.control.parent.controls),
									on_change = lambda e: flet.context.page.run_task(code_input_autofocus_switcher, e, field_index = 1)
								),
								Input(
									width = 50, 
									height = 50, 
									max_length = 1,
									on_blur = lambda e: save_code(e.control.parent.controls),
									on_change = lambda e: flet.context.page.run_task(code_input_autofocus_switcher, e, field_index = 2)
								),
								Input(
									width = 50, 
									height = 50, 
									max_length = 1,
									on_blur = lambda e: save_code(e.control.parent.controls),
									on_change = lambda e: flet.context.page.run_task(code_input_autofocus_switcher, e, field_index = 3)
								),
								Input(
									width = 50, 
									height = 50,
									max_length = 1,
									on_blur = lambda e: save_code(e.control.parent.controls),
									on_change = lambda e: flet.context.page.run_task(code_input_autofocus_switcher, e, field_index = 4)
								),
								Input(
									width = 50, 
									height = 50, 
									max_length = 1,
									on_blur = lambda e: save_code(e.control.parent.controls),
									on_change = lambda e: flet.context.page.run_task(code_input_autofocus_switcher, e, field_index = 5)
								),
								
							]
						),
						Button(content = 'Далее', on_click = next_step)
					]
				)
			)
		)

	return mail_code_content