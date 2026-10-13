import flet
from components.asidebar import asidebar
from components.theme_switcher import theme_switcher



@flet.component
def home_screen():
	return flet.Container(
		content = flet.Row(
			controls = [
				asidebar(),
				flet.Text('Home'),
				theme_switcher()
			]
		)
	)
