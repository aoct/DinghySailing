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
		text: 'Will contain the speed in kts and 2 angles'

	""")



"""
Calculate the velocity of a movement:
1. https://kivy.org/doc/stable/api-kivy.effects.kinetic.html
2. https://github.com/tito/android-demo/blob/master/main.py (how to access gps with kivy)
3. https://github.com/kivy/plyer (most updated version for kivy)
"""
