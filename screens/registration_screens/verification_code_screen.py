import flet
import asyncio
from packages.pixelkit.button import Button
from packages.pixelkit.input import Input
from services.mail_sender import MailSender



@flet.component
def verification_code_screen():

	counter, set_counter = flet.use_state(5)

	verification_code_hint, set_verification_code_hint = flet.use_state('Код')
	verification_code_border_color, set_verification_code_border_color = flet.use_state(flet.Colors.GREY)

	code_is_valid, set_code_is_valid = flet.use_state(False)
	inputed_code_is_correct, set_inputed_code_is_correct = flet.use_state(None)
	code_is_arrived, set_code_is_arrived = flet.use_state(True)

	is_active, set_is_active = flet.use_state(False)
	code = flet.use_ref('')

	async def next_step(e):
		prefs = flet.SharedPreferences()
		if await prefs.contains_key('verification_code'):
			verification_code = await prefs.get('verification_code')
			if int(code.current) == int(verification_code):
				set_verification_code_hint('Код')
				set_verification_code_border_color(flet.Colors.GREEN)
				set_inputed_code_is_correct(True)
				await flet.context.page.push_route('/account-recovery/password-recovery')
			else:
				set_verification_code_hint('Неверный код')
				set_verification_code_border_color(flet.Colors.RED)
				set_inputed_code_is_correct(False)



	async def resend_code(e):
		set_code_is_arrived(False)
		set_is_active(False)
		second_counter()
		set_counter(5)

		prefs = flet.SharedPreferences()
		mail_sender = MailSender(user_mail = await prefs.get('user_email'))

		await prefs.set('verification_code', mail_sender.verification_code)
		await mail_sender.send_verification_code()




	def code_validation(e):
		code.current = e.control.value
		if len(e.control.value) == 6:
			if all([val.isdigit() for val in e.control.value]):
				set_code_is_valid(True)
		else: set_code_is_valid(False)


	def button_unlock():
		async def _task():
			await asyncio.sleep(counter)
			set_is_active(True)
		flet.context.page.run_task(_task)


	def second_counter():
		async def _counter():
			for i in range(counter):
				await asyncio.sleep(1)
				set_counter(lambda s: s - 1)

		flet.context.page.run_task(_counter)



	flet.use_effect(button_unlock, dependencies=[])
	flet.use_effect(second_counter, dependencies=[])
	flet.use_effect(second_counter, dependencies=[code_is_arrived])

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
						flet.Text(
							value = 'Восстановление пароля', 
							size = 27, 
							text_align = flet.TextAlign.CENTER
						),
						flet.Text(
							value = 'Введите код который мы отправили вам на электронную почту', 
							size = 12
						),
						flet.Row(
							alignment = flet.MainAxisAlignment.CENTER,
							vertical_alignment = flet.CrossAxisAlignment.CENTER,
							controls = [
								Input(
									value = code.current,
									label = verification_code_hint,
									border_color = verification_code_border_color,
									width = 100, 
									height = 50, 
									autofocus = True, 
									max_length = 6,
									on_change = code_validation
								)
							]
						),
						Button(
							content = 'Далее', 
							on_click = next_step, 
							disabled = not code_is_valid
						),
						flet.TextButton(
							content = f'Код не пришёл ({counter})', 
							disabled = not is_active, 
							on_click = resend_code
						)
					]
				)
			)
		)

	return mail_code_content