import flet
from screens.home_screen import home_screen
from screens.settings_screen import settings_screen
from screens.registration_screens.registration_screen import registration_screen
from screens.registration_screens.login_screen import login_screen
from screens.registration_screens.verification_code_screen import verification_code_screen
from screens.registration_screens.email_sender_screen import email_sender_screen
from screens.registration_screens.password_recovery_screen import password_recovery_screen



@flet.component
def router():
	return flet.Router(
		manage_views = True,
		routes = [
			flet.Route(index = True, component = home_screen),
			flet.Route(path = '/settings', component = settings_screen),
         
			flet.Route(path = '/registration', component = registration_screen),
			flet.Route(path = '/login', component = login_screen),
			flet.Route(path = '/account-recovery', component = email_sender_screen),
			flet.Route(path = '/account-recovery/mail-code', component = verification_code_screen),
			flet.Route(path = '/account-recovery/password-recovery', component = password_recovery_screen)
		]
	)