import flet
from packages.pixelkit.button import Button
from packages.utils.validator import Validator
from services.mail_sender import MailSender



@flet.component
def registration_screen():

	validator = Validator()

	name_field_value, set_name_field_value = flet.use_state('')
	name_field_border_color, set_name_field_border_color = flet.use_state(flet.Colors.GREY)
	name_field_hint, set_name_field_hint = flet.use_state('Имя')
	name_field_is_valid, set_name_field_is_valid = flet.use_state(False)

	surname_field_value, set_surname_field_value = flet.use_state('')
	surname_field_border_color, set_surname_field_border_color = flet.use_state(flet.Colors.GREY)
	surname_field_hint, set_surname_field_hint = flet.use_state('Фамилия')
	surname_field_is_valid, set_surname_field_is_valid = flet.use_state(False)

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

	repeat_password_value = flet.use_ref('')
	repeat_password_border_color, set_repeat_password_border_color = flet.use_state(flet.Colors.GREY)
	repeat_password_hint, set_repeat_password_hint = flet.use_state('Повторите пароль')
	repeat_password_is_valid, set_repeat_password_is_valid = flet.use_state(False)

	i_accept, set_i_accept = flet.use_state(True)
	is_disabled, set_is_disabled = flet.use_state(True)


	def name_field_validation(e):

		set_name_field_value(e.control.value)

		is_valid, error_text = validator.name_validator(validate_data = e.control.value)

		if is_valid and error_text == None:
			set_name_field_border_color(flet.Colors.GREEN)
			set_name_field_hint('Имя')
			set_name_field_is_valid(True)
		else:
			set_name_field_border_color(flet.Colors.RED)
			set_name_field_hint(error_text)
			set_name_field_is_valid(False)


	def surname_field_validation(e):
		set_surname_field_value(e.control.value)

		is_valid, error_text = validator.name_validator(validate_data = e.control.value)

		if is_valid and error_text == None:
			set_surname_field_border_color(flet.Colors.GREEN)
			set_surname_field_hint('Фамилия')
			set_surname_field_is_valid(True)
		else:
			set_surname_field_border_color(flet.Colors.RED)
			set_surname_field_hint(error_text)
			set_surname_field_is_valid(False)


	def username_field_validation(e):
		set_username_field_value(e.control.value)

		is_valid, error_text = validator.username_validator(validate_data = e.control.value)

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
				repeat = repeat_password_value.current
			)
		if is_valid and error_text == None:
			set_password_hint('Пароль')
			set_password_border_color(flet.Colors.GREEN)
			set_password_is_valid(True)
			if password_value.current == repeat_password_value.current:
				set_repeat_password_hint('Повторите пароль')
				set_repeat_password_border_color(flet.Colors.GREEN)
				set_repeat_password_is_valid(True)
				return True
			return True
		else:
			set_password_hint(error_text)
			set_password_border_color(flet.Colors.RED)
			set_password_is_valid(False)
			return False


	def repeat_password_validation(e):
		repeat_password_value.current = e.control.value

		is_valid, error_text = validator.password_validator(
				validate_data = repeat_password_value.current,
				repeat = password_value.current
			)
		if is_valid and error_text == None:
			set_repeat_password_hint('Повторите пароль')
			set_repeat_password_border_color(flet.Colors.GREEN)
			set_repeat_password_is_valid(True)
			if repeat_password_value.current == password_value.current:
				set_password_hint('Пароль')
				set_password_border_color(flet.Colors.GREEN)
				set_password_is_valid(True)
				return True
			return True
		else:
			set_repeat_password_hint(error_text)
			set_repeat_password_border_color(flet.Colors.RED)
			set_repeat_password_is_valid(False)
			return False


	def is_all_valid():
		params = [
			name_field_is_valid, 
			surname_field_is_valid, 
			username_field_is_valid,
			mail_field_is_valid,
			password_is_valid,
			repeat_password_is_valid
		]
		set_is_disabled(not all(params))


	async def final_validation(e):
		await flet.context.page.push_route('/account-recovery/mail-code')
		
		prefs = flet.SharedPreferences()
		mail_sender = MailSender(user_mail = mail_field_value)

		await prefs.set('verification_code', mail_sender.verification_code)
		await mail_sender.send_verification_code()


	flet.use_effect(is_all_valid, dependencies = [
		name_field_is_valid, surname_field_is_valid, username_field_is_valid,
		mail_field_is_valid, password_is_valid, repeat_password_is_valid
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
							value = name_field_value,
							label = name_field_hint,
							border_color = name_field_border_color,
							width = 300,
							height = 40,
							cursor_height = 20,
							text_vertical_align = flet.VerticalAlignment.CENTER,
							on_change = lambda e: name_field_validation(e)
						),
						flet.TextField(
							value = surname_field_value,
							label = surname_field_hint,
							border_color = surname_field_border_color,
							width = 300,
							height = 40,
							cursor_height = 20,
							text_vertical_align = flet.VerticalAlignment.CENTER,
							on_change = lambda e: surname_field_validation(e)
						),
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
							label = mail_field_hint,
							border_color = mail_field_border_color,
							width = 300,
							height = 40,
							cursor_height = 20,
							text_vertical_align = flet.VerticalAlignment.CENTER,
							on_change = lambda e: mail_field_validation(e)
						),
						flet.TextField(
							value = password_value.current,
							label = password_hint,
							border_color = password_border_color,
							width = 300,
							height = 40,
							cursor_height = 20,
							text_vertical_align = flet.VerticalAlignment.CENTER,
							on_change = lambda e: password_field_validation(e)
						),
						flet.TextField(
							value = repeat_password_value.current,
							width = 300,
							height = 40,
							label = repeat_password_hint,
							border_color = repeat_password_border_color,
							cursor_height = 20,
							text_vertical_align = flet.VerticalAlignment.CENTER,
							on_change = lambda e: repeat_password_validation(e)
						),
						flet.Checkbox(
							value = i_accept,
							on_change = lambda e: set_i_accept(not i_accept),
							label = 'Я принимаю условия пользования'
						),
						Button(content = 'Зарегистрироваться', width = 280, height = 49, on_click = final_validation, disabled = is_disabled),
						flet.Row(
							width = 300,
							height = 40,
							alignment = flet.MainAxisAlignment.CENTER,
							controls = [
								flet.TextButton(
									content = 'Войти',
									on_click = lambda e: flet.context.page.run_task(flet.context.page.push_route, '/login')
								)
							]
						)
					]
				)
			)
		)

	return registration_screen_content