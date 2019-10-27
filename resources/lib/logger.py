import xbmc

from . import PLUGIN_ID


def _log(message, level):
    fmt_message = "[{}]: {}".format(PLUGIN_ID, str(message))
    xbmc.log(fmt_message, level=level)


def debug(message):
    _log(message, xbmc.LOGDEBUG)


def info(message):
    _log(message, xbmc.LOGINFO)


def notice(message):
    _log(message, xbmc.LOGNOTICE)


def warning(message):
    _log(message, xbmc.LOGWARNING)


def error(message):
    _log(message, xbmc.LOGERROR)


def fatal(message):
    _log(message, xbmc.LOGFATAL)
