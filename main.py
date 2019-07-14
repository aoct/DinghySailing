import os
import kivy
kivy.require("1.10.0")

if os.name == 'posix':
	print('Showing a smartphone-like screen')
	from kivy.config import Config
	Config.set('graphics', 'width', '540')
	Config.set('graphics', 'height', '960')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from mainPage import mainPage
from sailingPage import sailingPage

class DinghySailingApp(App):
	def build(self):
		self.sm = ScreenManager()

		self.mainPage = mainPage(name = 'MainPage')
		self.sm.add_widget(self.mainPage)

		self.sailingPage = sailingPage(name = 'SailingPage')
		self.sm.add_widget(self.sailingPage)

		return self.sm

if __name__=="__main__":
	app = DinghySailingApp()
	app.run()
