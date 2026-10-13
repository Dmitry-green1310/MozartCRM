

class Validator:

	ALLOWED = set(
		'abcdefghijklmnopqrstuvwxyz'
		'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		'0123456789'
		'-_.'
	)

	def name_validator(self, validate_data: str):
		
		if len(validate_data) <= 16: 
			if len(validate_data) >= 2: 
				if all(ch in self.ALLOWED for ch in validate_data):
					return True, None
				else: return False, 'Недопустимые символы'
			else: return False, 'Не менее двух символов'
		else: return False, 'Не более 16 символов'


	def username_validator(self, validate_data: str):
		if len(validate_data) <= 16: 
			if len(validate_data) >= 2: 
				if not any('\u0400' <= ch <= '\u04FF' for ch in validate_data):
					if not any(ch.isdigit() for ch in validate_data):
						if all(ch in self.ALLOWED for ch in validate_data):
							return True, None
						else: return False, 'Недопустимые символы'
					else: return False, 'Только символы'
				else: return False, 'Только латиница'
			else: return False, 'Не менее двух символов'
		else: return False, 'Не более 16 символов'


	def mail_validator(self, validate_data: str):
		if '@' in validate_data and '.' in validate_data: 
			if all(ch in self.ALLOWED or ch == '@' for ch in validate_data):
					return True, None
			else: return False, 'Недопустимые символы'
		else: return False, 'Неккоректный адрес'



	def password_validator(self, validate_data: str, repeat = None):
		if len(validate_data) >= 8:
			if len(validate_data) <= 16:
				if validate_data == repeat: 
					if all(ch in self.ALLOWED or ch == '@' or ch == '.' or ch == '-' for ch in validate_data):
						return True, None
					else: return False, 'Недопустимые символы'
				else: return False, 'Пароли отличаются'
			else: return False, 'Слишком длинный пароль'
		else: return False, 'Слишком короткий пароль'


