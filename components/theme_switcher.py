import flet
from packages.pixelkit.switch import Switch


@flet.component
def theme_switcher():

	theme, set_theme = flet.use_state('light')
	

	async def theme_handler(e):
		prefs = flet.SharedPreferences()
		if e.control.value: flet.context.page.theme_mode = flet.ThemeMode.DARK
		else: flet.context.page.theme_mode = flet.ThemeMode.LIGHT

		await prefs.set('app_theme', 'dark' if e.control.value else 'light')
		set_theme(flet.ThemeMode.DARK if e.control.value else flet.ThemeMode.LIGHT)
		flet.context.page.update()


	
	async def load_saved_theme():
		prefs = flet.SharedPreferences()
		if await prefs.contains_key('app_theme'):
			saved_theme = await prefs.get('app_theme')
			flet.context.page.theme_mode = flet.ThemeMode.DARK if saved_theme == 'dark' else flet.ThemeMode.LIGHT
			set_theme('dark' if saved_theme == 'dark' else 'light')
		else:
			prefs.set('app_theme', 'dark' if flet.context.page.theme_mode == flet.ThemeMode.DARK else 'light')
			set_theme('light')

		flet.context.page.update()

		



	flet.use_effect(lambda: flet.context.page.run_task(load_saved_theme), dependencies = [])
	theme_switcher_content = Switch(
		value = (flet.context.page.theme_mode == flet.ThemeMode.DARK),
		on_change = lambda e: flet.context.page.run_task(theme_handler, e)
		)

	return theme_switcher_content