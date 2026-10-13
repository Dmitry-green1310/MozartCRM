import flet
from router import router
from settings.app_settings import set_app_settings
from components.theme_switcher import theme_switcher


def main(page):
	page.run_task(set_app_settings, page)
	page.render(router)
	page.update()


if __name__ == '__main__':
	flet.run(main)