# Pentest probe (teaflask engagement): measures whether the verification runner
# imports repository-root conftest.py when it collects a generated suite.
# The only effect is a delay, so a run that imports this file takes ~40s longer.
import time

time.sleep(40)
