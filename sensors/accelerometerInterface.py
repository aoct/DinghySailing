from plyer import accelerometer

class Accelerometer:
    def __init__(self):
        if self.is_implemented():
            self.working = True
        else:
            self.working = False

    def start(self):
        if self.working:
            accelerometer.enable()

    def stop(self):
        if self.working:
            accelerometer.disable()

    def get_value(self):
        if self.working:
            val = accelerometer.acceleration[:3]
            return val
        else:
            return [0, 0, 0]

    def is_implemented(self):
        try:
            accelerometer.enable()
            print(accelerometer.acceleration[:3])

            accelerometer.disable()
            return True
        except:
            # import traceback
            # traceback.print_exc()
            print('Accelerometer is not implemented for your platform')
            return False
