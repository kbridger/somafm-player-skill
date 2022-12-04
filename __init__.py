from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel
from mycroft.util.parse import match_one
from mycroft.util import LOG

track_dict = {
    'groovesalad': 'https://ice4.somafm.com/groovesalad-128-mp3',
    'groove salad': 'https://ice4.somafm.com/groovesalad-128-mp3',
    'suburbs of goa': 'https://ice4.somafm.com/suburbsofgoa-128-mp3',
    'test': 'https://cbc.mc.tritondigital.com/CBC_HOURLYNEWS_P/media/hourlynews/hourlynews-ttA7xpoG-20221201.mp3'
}

def new_func():
    LOG.info("this is outside the class")


class SomafmPlayer(CommonPlaySkill):

    def initialize(self):
        self.log.info("the skill is loaded!")
#        new_func()

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
        #self.log.info(f"Playing from: {url}")
        #self.log.exception("This is an error.")
        # Let's output this data to see what came in
        self.log.info("Let's dump some data to see what's what.")
        self.log.info(f"self: {self}")
        self.log.info(f"phrase: {phrase}")
        self.log.info(f"data: {data}")
        self.log.info(f"url: {url}")
        #self.speak_dialog("Playing Soma FM")
        # Send url to audioservice to start playback
        #self.audioservice.play(url) 
        self.CPS_play(url)
#        try:
#            print(new_var)
#        except NameError:
#            self.log.exception("This is an exception")
        self.log.info(f"That should have worked to play: {url}")
#        self.log.debug("This is debug level log")
#        self.log.info("Let's just play this URL directly")
#        self.CPS_play("https://ice4.somafm.com/groovesalad-128-mp3")
#        self.log.info("That should have played")

def create_skill():
    return SomafmPlayer()

