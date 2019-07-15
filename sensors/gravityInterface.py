from plyer import gravity

class Gravity:
    def __init__(self):
        if self.is_implemented():
            self.working = True
        else:
            self.working = False

    def start(self):
        if self.working:
            gravity.enable()

    def stop(self):
        if self.working:
            gravity.disable()

    def get_value(self):
        if self.working:
            val = gravity.gravity[:3]
            return val
        else:
            return [0, 0, 0]

    def is_implemented(self):
        try:
            gravity.enable()
            print(gravity.gravity[:3])

            gravity.disable()
            return True
        except:
            # import traceback
            # traceback.print_exc()
            print('Gravity is not implemented for your platform')
            return False
