import flet
import asyncio
from packages.pixelkit.button import Button
from packages.pixelkit.input import Input
from packages.utils.validator import Validator



@flet.component
def password_recovery_screen():

	password_value = flet.use_ref('')
	password_is_valid, set_password_is_valid = flet.use_state(False)
	password_hint, set_password_hint = flet.use_state('Пароль')
	password_border_color, set_password_border_color = flet.use_state(flet.Colors.GREY)

	repeat_password_value = flet.use_ref('')
	repeat_password_is_valid, set_repeat_password_is_valid = flet.use_state(False)
	repeat_password_hint, set_repeat_password_hint = flet.use_state('Повторите пароль')
	repeat_password_border_color, set_repeat_password_border_color = flet.use_state(flet.Colors.GREY)

	passwords_is_identy, set_passwords_is_identy = flet.use_state(True)
	is_disabled, set_is_disabled = flet.use_state(True)


	def password_field_validation(e):
		validator = Validator()
		password_value.current = e.control.value

		is_valid, error_text = validator.password_validator(
			validate_data = password_value.current,
			repeat = repeat_password_value.current
		)

		if is_valid and error_text == None:
			set_password_is_valid(True)
			set_password_hint('Пароль')
			set_password_border_color(flet.Colors.GREEN)
			if password_value.current == repeat_password_value.current:
				set_repeat_password_hint('Повторите пароль')
				set_repeat_password_border_color(flet.Colors.GREEN)
				set_is_disabled(False)
				return True
			return True
		else:
			set_password_is_valid(False)
			set_password_hint(error_text)
			set_password_border_color(flet.Colors.RED)
			set_is_disabled(True)
			return False


	def repeat_password_validation(e):
		validator = Validator()
		repeat_password_value.current = e.control.value

		is_valid, error_text = validator.password_validator(
			validate_data = repeat_password_value.current,
			repeat = password_value.current
		)

		if is_valid and error_text == None:
			set_repeat_password_is_valid(True)
			set_repeat_password_hint('Повторите пароль')
			set_repeat_password_border_color(flet.Colors.GREEN)
			if repeat_password_value.current == password_value.current:
				set_password_hint('Повторите пароль')
				set_password_border_color(flet.Colors.GREEN)
				set_is_disabled(False)
				return True
			return True
		else:
			set_repeat_password_is_valid(False)
			set_repeat_password_hint(error_text)
			set_repeat_password_border_color(flet.Colors.RED)
			set_is_disabled(True)
			return False


	async def go_to_home(e):
		await flet.context.page.push_route('/')



	password_recovery_content = flet.Container(
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
					flet.Text('Придумайте новый пароль', text_align = flet.TextAlign.CENTER, size = 12),
					Input(
						width = 300, 
						height = 40, 
						label = password_hint,
						value = password_value.current, 
						border_color = password_border_color,
						on_change = lambda e: password_field_validation(e)
					),
					Input( 
						width = 300, 
						height = 40,
						label = repeat_password_hint,
						value = repeat_password_value.current,
						border_color = repeat_password_border_color,
						on_change = lambda e: repeat_password_validation(e)
					),
					Button(content = 'Далее', disabled = is_disabled, on_click = go_to_home)
				]
			)
		)
	)

	return password_recovery_content