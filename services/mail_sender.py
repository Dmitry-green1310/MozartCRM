import asyncio
import random
import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MailSender:

	SMTP_SERVER = 'smtp.gmail.com'
	SENDER_EMAIL = 'mozartcrm@gmail.com'
	SMTP_PORT = 587
	APP_PASSWORD = "jcdeuhvlwfxovxpf"

	def __init__(self, user_mail):
		self.user_mail = user_mail

		self.verification_code = random.randint(100000, 999999)
		self.__email_settings()



	async def send_verification_code(self):
		await self.__smtp_server_connect()



	def __email_settings(self):
		self.msg = MIMEMultipart()
		self.msg['From'] = self.SENDER_EMAIL
		self.msg['To'] = self.user_mail
		self.msg['Subject'] = 'Код подтверждения'
		self.msg.attach(MIMEText(f'Ваш код подтверждения: {self.verification_code}', 'plain', 'utf-8'))



	async def __smtp_server_connect(self):
		async with aiosmtplib.SMTP(hostname = self.SMTP_SERVER, port = self.SMTP_PORT) as server:
			await server.login(self.SENDER_EMAIL, self.APP_PASSWORD)
			await server.send_message(self.msg)