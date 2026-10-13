import flet
import asyncio
from packages.utils.validator import Validator
from packages.pixelkit.button import Button
from packages.pixelkit.input import Input
from services.mail_sender import MailSender



@flet.component
def email_sender_screen():

	validator = Validator()

	mail_field_value, set_mail_field_value = flet.use_state('')
	mail_field_border_color, set_mail_field_border_color = flet.use_state(flet.Colors.GREY)
	mail_field_hint, set_mail_field_hint = flet.use_state('Электронная почта')
	mail_field_is_valid, set_mail_field_is_valid = flet.use_state(False)

	async def next_step(e):

		await flet.context.page.push_route('/account-recovery/mail-code')

		prefs = flet.SharedPreferences()
		mail_sender = MailSender(user_mail = mail_field_value)

		await prefs.set('user_email', mail_field_value)
		await prefs.set('verification_code', mail_sender.verification_code)
		await mail_sender.send_verification_code()


	def mail_validation(e):
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


	mail_send_screen = flet.Container(
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
						flet.Text(
							value = 'Укажите в поле ниже почту которую вы указывали при регистрации аккаунта. Мы отправим туда письмо с кодом', 
							text_align = flet.TextAlign.CENTER,
							size = 12
						),
						Input(
							value = mail_field_value,
							width = 300, 
							height = 40, 
							label = mail_field_hint, 
							border_color = mail_field_border_color,
							on_change = mail_validation
						),
						Button(content = 'Далее', on_click = next_step, disabled = not mail_field_is_valid),

					]
				)
			)
		)

	return mail_send_screen