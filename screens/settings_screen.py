import flet
from components.asidebar import asidebar
from components.theme_switcher import theme_switcher




@flet.component
def settings_screen():
	return flet.Container(
				content = flet.Row(
					controls = [
						asidebar(),
						flet.Text('Settings'),
						theme_switcher()
					]
				)
			)
