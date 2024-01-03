import os


AUTHOR = 'realz'
SITENAME = 'Random ComfyUI Notes'
SITEURL = "https://realazthat.github.io/ComfyUIResources"

PATH = "content"

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


# THEME = str(Path(pelican.__path__[0]) / 'themes/notmyidea')

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
THEME = os.path.join(CURRENT_DIR, 'monospace-andrewboring')
