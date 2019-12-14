from mycroft import MycroftSkill, intent_file_handler
import requests

class Test(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('on.intent')
    def handle_on(self, message):
        requests.put('http://192.168.0.101/api/AmE3DbmI-V6GpnsBHqdG-g5NG7Xiz1AvUh8iMVt7/lights/12/state', data="{\"on\":true}")
        self.speak_dialog('on')

    @intent_file_handler('test.intent')
    def handle_off(self, message):
        requests.put('http://192.168.0.101/api/AmE3DbmI-V6GpnsBHqdG-g5NG7Xiz1AvUh8iMVt7/lights/12/state', data="{\"on\":false}")
        self.speak_dialog('test')


def create_skill():
    return Test()

