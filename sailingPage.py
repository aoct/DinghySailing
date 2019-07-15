from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from gravityInterface import Gravity

class sailingPage(Screen):
	def __init__(self, **kwargs):
		super(sailingPage, self).__init__(**kwargs)
		self.gravity = Gravity()

		self.measGrid = GridLayout(cols=1, size_hint=(1.,.8))
		self.measGrid.add_widget(Label(text='Speed: 0 knts', font_size='20sp'))
		self.measGrid.add_widget(Label(text='X: 0', font_size='20sp'))
		self.measGrid.add_widget(Label(text='Y: 0', font_size='20sp'))
		self.measGrid.add_widget(Label(text='Z: 0', font_size='20sp'))

		self.add_widget(self.measGrid)

	def on_enter(self):
		self.gravity.start()
		Clock.schedule_interval(self.update_angles, 1 / 1.)

	def on_leave(self):
		self.gravity.stop()
		Clock.unschedule(self.update_angles)

	def update_angles(self, dt):
		val = self.gravity.get_value()

		self.measGrid.children[2].text = 'X: {:.2f}'.format(val[0])
		self.measGrid.children[1].text = 'Y: {:.2f}'.format(val[1])
		self.measGrid.children[0].text = 'Z: {:.2f}'.format(val[2])


Builder.load_string("""
<SailingPage>:
	FloatLayout:
		Button:
			size_hint: (.1, .1)
			pos_hint: {'x':0.01, 'y':.89}
			on_release: app.sm.current = 'MainPage'
			background_color: 0, 0, 0, .0
			Image:
				source: "images/icons/home.png"
				y: self.parent.y
				x: self.parent.x
				size: self.parent.size
				allow_stretch: True
""")



"""
Calculate the velocity of a movement:
1. https://kivy.org/doc/stable/api-kivy.effects.kinetic.html
2. https://github.com/tito/android-demo/blob/master/main.py (how to access gps with kivy)
3. https://github.com/kivy/plyer (most updated version for kivy)
"""
