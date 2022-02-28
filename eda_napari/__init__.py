try:
    from ._version import version as __version__
except ImportError:
    __version__ = "1.2"

from ._widget import widgetFunctions