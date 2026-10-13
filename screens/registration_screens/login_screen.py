import flet
from packages.pixelkit.button import Button
from packages.utils.validator import Validator


@flet.component
def login_screen():

	validator = Validator()

	username_field_value, set_username_field_value = flet.use_state('')
	username_field_border_color, set_username_field_border_color = flet.use_state(flet.Colors.GREY)
	username_field_hint, set_username_field_hint = flet.use_state('Имя пользователя')
	username_field_is_valid, set_username_field_is_valid = flet.use_state(False)

	mail_field_value, set_mail_field_value = flet.use_state('')
	mail_field_border_color, set_mail_field_border_color = flet.use_state(flet.Colors.GREY)
	mail_field_hint, set_mail_field_hint = flet.use_state('Электронная почта')
	mail_field_is_valid, set_mail_field_is_valid = flet.use_state(False)

	password_value = flet.use_ref('')
	password_border_color, set_password_border_color = flet.use_state(flet.Colors.GREY)
	password_hint, set_password_hint = flet.use_state('Пароль')
	password_is_valid, set_password_is_valid = flet.use_state(False)

	is_disabled, set_is_disabled = flet.use_state(True)



	def username_field_validation(e):
		set_username_field_value(e.control.value)

		is_valid, error_text = validator.name_validator(validate_data = e.control.value)

		if is_valid and error_text == None:
			set_username_field_border_color(flet.Colors.GREEN)
			set_username_field_hint('Имя пользователя')
			set_username_field_is_valid(True)

		else:
			set_username_field_border_color(flet.Colors.RED)
			set_username_field_hint(error_text)
			set_username_field_is_valid(False)


	def mail_field_validation(e):
		set_mail_field_value(e.control.value)

		is_valid, error_text = validator.mail_validator(validate_data = e.control.value)
		if is_valid and error_text == None:
			set_mail_field_border_color(flet.Colors.GREEN)
			set_mail_field_hint('Электронная почта')
			set_mail_field_is_valid(True)
		else:
			set_mail_field_border_color(flet.Colors.RED)
			set_mail_field_hint(error_text)
			set_mail_field_is_valid(False)


	def password_field_validation(e):
		password_value.current = e.control.value

		is_valid, error_text = validator.password_validator(
				validate_data = password_value.current,
				repeat = password_value.current
			)
		if is_valid and error_text == None:
			set_password_hint('Пароль')
			set_password_border_color(flet.Colors.GREEN)
			set_password_is_valid(True)
			return True
		else:
			set_password_hint(error_text)
			set_password_border_color(flet.Colors.RED)
			set_password_is_valid(False)
			return False


	def is_all_valid():
		print('')
		params = [ 
			username_field_is_valid,
			mail_field_is_valid,
			password_is_valid
		]
		print('validity:',)
		set_is_disabled(not all(params))


	async def final_validation(e):
		await flet.context.page.push_route('/')


	flet.use_effect(is_all_valid, dependencies = [
		username_field_is_valid, mail_field_is_valid, password_is_valid
	])

	
	registration_screen_content = flet.Container(
			expand = True,
			alignment = flet.Alignment.CENTER,
			content = flet.Container(
				width = 300,
				height = 600,
				alignment = flet.Alignment.CENTER,
				content = flet.Column(
					expand = True,
					alignment = flet.MainAxisAlignment.CENTER,
					horizontal_alignment = flet.CrossAxisAlignment.CENTER,
					controls = [
						flet.Text('Mozart', size = 27, text_align = flet.TextAlign.CENTER),
						flet.TextField(
							value = username_field_value,
							label = username_field_hint,
							border_color = username_field_border_color,
							width = 300, 
							height = 40,
							cursor_height = 20, 
							text_vertical_align = flet.VerticalAlignment.CENTER,
							on_change = lambda e: username_field_validation(e)
						),
						flet.TextField(
							value = mail_field_value,
							width = 300, 
							height = 40,
							label = mail_field_hint,
							border_color = mail_field_border_color,
							cursor_height = 20, 
							text_vertical_align = flet.VerticalAlignment.CENTER,
							on_change = lambda e: mail_field_validation(e)
						),
						flet.TextField(
							value = password_value.current,
							border_color = password_border_color,
							width = 300, 
							height = 40,
							label = password_hint,
							cursor_height = 20, 
							text_vertical_align = flet.VerticalAlignment.CENTER,
							on_change = lambda e: password_field_validation(e)
						),
						Button(content = 'Войти', width = 300, height = 40, disabled = is_disabled, on_click = final_validation),
						flet.Row(
							width = 300,
							height = 40,
							controls = [
								flet.TextButton(
									content = 'Зарегистрироваться', 
									on_click = lambda e: flet.context.page.run_task(flet.context.page.push_route, '/registration')
								),
								flet.TextButton(
									content = 'Забыл пароль',
									on_click = lambda e: flet.context.page.run_task(flet.context.page.push_route, '/account-recovery')
								)
							]
						)
					]
				)
			)
		)

	return registration_screen_content