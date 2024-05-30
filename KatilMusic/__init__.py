from KatilMusic.core.bot import Anony
from KatilMusic.core.dir import dirr
from KatilMusic.core.git import git
from KatilMusic.core.userbot import Userbot
from KatilMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
