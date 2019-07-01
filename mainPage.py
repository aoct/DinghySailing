from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivmob import KivMob, TestIds

class mainPage(Screen):

	def __init__(self, **kwargs):
		super(mainPage, self).__init__(**kwargs)


Builder.load_string("""
<mainPage>:

	Button:
		on_release: app.sm.current = 'SailingPage'
		text: 'Start Sailing'
		size_hint: (.2, .2)
		pos_hint: {'x':.4, 'y':.4}
		# background_color: 0,0,0,.0
		
	""")


"""
The main page will be the opening of the app. It will have a big central button 
that will lead us to the sailing page. Then we are going to have a small settings
button, a small button to access old sailing data, etc...



"""