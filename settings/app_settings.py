import flet


async def set_app_settings(page):
	page.window.width = 1300
	page.window.height = 700
	page.window.min_width = 900
	page.window.min_height = 500
	page.resizable = True
	page.title = 'Mozart'
	page.padding = 0
	page.margin = 0

	prefs = flet.SharedPreferences()
	if await prefs.contains_key('app_theme'):
		saved_theme = await prefs.get('app_theme')
		page.theme_mode = flet.ThemeMode.LIGHT if saved_theme == 'light' else flet.ThemeMode.DARK
	else:
		page.theme_mode = flet.ThemeMode.LIGHT