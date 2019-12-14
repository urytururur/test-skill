from mycroft import MycroftSkill, intent_file_handler
import requests

class Test(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('on.intent')
    def handle_on(self, message):
        requests.put('http://192.168.0.106/1', data="{\"on\":true}")
        self.speak_dialog('on')

    @intent_file_handler('off.intent')
    def handle_off(self, message):
        requests.put('http://192.168.0.106/0', data="{\"on\":false}")
        self.speak_dialog('off')


def create_skill():
    return Test()

