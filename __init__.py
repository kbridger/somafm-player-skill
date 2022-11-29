from mycroft import MycroftSkill, intent_file_handler


class SomafmPlayer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('player.somafm.intent')
    def handle_player_somafm(self, message):
        streamname = message.data.get('streamname')

        self.speak_dialog('player.somafm', data={
            'streamname': streamname
        })


def create_skill():
    return SomafmPlayer()

