from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivmob import KivMob, TestIds

class sailingPage(Screen):

	def __init__(self, **kwargs):
		super(sailingPage, self).__init__(**kwargs)


Builder.load_string("""
<SailingPage>:

	Label:
		text: 'This is the sailing Page'
		
	""")