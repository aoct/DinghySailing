from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock, mainthread

from plyer import gps

from kivmob import KivMob, TestIds

class sailingPage(Screen):

	def __init__(self, **kwargs):
		super(sailingPage, self).__init__(**kwargs)

		self.gpsLocation = StringProperty()
		self.gpsStatus = StringProperty()

	def on_enter(self):
		try:
			self.GPS = gps.configure(on_location=self.on_location,
							on_status=self.on_status)

			"""
			When testing on the computer, we raise the exception here and this causes the rest of the system to crash. 
			Might require testing on the phone
			"""
		except NotImplementedError:
			import traceback
			traceback.print_exc()
			self.gpsStatus = 'GPS not working'

	def start(self, minTime, minDistance):
		self.GPS.start(minTime, minDistance)

	def stop(self):
		self.GPS.stop()

	def on_location(self, **kwargs):
		self.gpsLocation = '\n'.join([
			'{}={}'.format(k, v) for k, v in kwargs.items()])

	def on_status(self, stype, status):
		self.gpsStatus = 'type={}\n{}'.format(stype, status)

	def on_pause(self):
		self.GPS.stop()
		return True

	def on_resume(self):
		self.GPS.start(1000, 0)
		pass


Builder.load_string("""
<sailingPage>:

	Label:
		text: 'Sailing Page contains: speed (kts), the direction angle, and the inclination angle'
	# Label: 
	# 	text: root.gpsLocation
	# Label: 
	# 	text: root.gpsStatus
	BoxLayout:
		size_hint_y: None
		height: '48dp'
		padding: '4dp'
		ToggleButton:
			text: 'Start' if self.state == 'normal' else 'Stop'
			on_state:
				root.start(1000, 0) if self.state == 'down' else \
				root.stop()

""")



"""
Calculate the velocity of a movement:
1. https://kivy.org/doc/stable/api-kivy.effects.kinetic.html
2. https://github.com/tito/android-demo/blob/master/main.py (how to access gps with kivy)
3. https://github.com/kivy/plyer (most updated version for kivy)
"""

"""
Example code for gps implementation

from kivy.lang import Builder
from plyer import gps
from kivy.app import App
from kivy.properties import StringProperty
from kivy.clock import Clock, mainthread

kv = '''
BoxLayout:
    orientation: 'vertical'
    Label:
        text: app.gps_location
    Label:
        text: app.gps_status
    BoxLayout:
        size_hint_y: None
        height: '48dp'
        padding: '4dp'
        ToggleButton:
            text: 'Start' if self.state == 'normal' else 'Stop'
            on_state:
                app.start(1000, 0) if self.state == 'down' else \
                app.stop()
'''

class GpsTest(App):

    gps_location = StringProperty()
    gps_status = StringProperty('Click Start to get GPS location updates')

    def build(self):
        try:
            gps.configure(on_location=self.on_location,
                          on_status=self.on_status)
        except NotImplementedError:
            import traceback
            traceback.print_exc()
            self.gps_status = 'GPS is not implemented for your platform'

        return Builder.load_string(kv)

    def start(self, minTime, minDistance):
        gps.start(minTime, minDistance)

    def stop(self):
        gps.stop()

    @mainthread ####This is the first thing that starts running when you run the application -- How can we deal with this since we are not making this the app but a screen? 
    def on_location(self, **kwargs):
        self.gps_location = '\n'.join([
            '{}={}'.format(k, v) for k, v in kwargs.items()])

    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)

    def on_pause(self):
        gps.stop()
        return True

    def on_resume(self):
        gps.start(1000, 0)
        pass

if __name__ == '__main__':
    GpsTest().run()

"""