import flet
from packages.pixelkit.button import Button



@flet.component
def asidebar():
	asidebar_content = flet.Container(
			width = 200,
			height = 700,
			content = flet.Column(
				expand = True,
				spacing = 0,
				controls = [
					Button(
						content = 'Главная',
						on_click = lambda e: flet.context.page.run_task(flet.context.page.push_route, '/'),
					),
					Button(
						content = 'Настройки', 
						on_click = lambda e: flet.context.page.run_task(flet.context.page.push_route, '/settings')
					),
					Button(
						content = 'Регистрация',
						on_click = lambda e: flet.context.page.run_task(flet.context.page.push_route, '/registration')
					)
				]
			)
		)

	return asidebar_content