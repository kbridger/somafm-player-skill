from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel
from mycroft.util.parse import match_one

track_dict = {
    'groovesalad': 'https://ice4.somafm.com/groovesalad-128-mp3',
    'suburbs of goa': 'https://ice4.somafm.com/suburbsofgoa-128-mp3'
}

class SomafmPlayer(CommonPlaySkill):
    def CPS_match_query_phrase(self, phrase):
        """ This method responds whether the skill can play the input phrase.

            The method is invoked by the PlayBackControlSkill.

            Returns: tuple (matched phrase(str),
                            match level(CPSMatchLevel),
                            optional data(dict))
                     or None if no match was found.
        """
        # Get match and confidence
        match, confidence = match_one(phrase, track_dict)
        # If confidence is high enough return a match
        if confidence > 0.5:
            return (match, CPSMatchLevel.TITLE, {"track": match})
        # Otherwise return None
        else:
            return None

    def CPS_start(self, phrase, data):
        """ Starts playback.

            Called by the playback control skill to start playback if the
            skill is selected (has the best match level)
        """
        # Retrieve the track url from the data
        url = data['track']
        self.log.info(f"Playing from: {url}")
        self.speak_dialog("Playing Soma FM")
        # Send url to audioservice to start playback
        self.audioservice.play(url) 
        #self.CPS_play(["url"])


def create_skill():
    return SomafmPlayer()

