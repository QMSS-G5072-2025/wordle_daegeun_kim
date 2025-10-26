# read version from installed package
from importlib.metadata import version
__version__ = version("wordle_dk3481")

from .wordle_dk3481 import *