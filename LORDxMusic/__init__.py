from LORDxMusic.core.bot import LORDy
from LORDxMusic.core.dir import dirr
from LORDxMusic.core.git import git
from LORDxMusic.core.userbot import Userbot
from LORDxMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = LORDy()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
