###########################################################################################
# MASTAN3 - Python-based Cross-platforms Frame Analysis Software
#
# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
###########################################################################################
# Description:
# =========================================================================================
# Import standard libraries
import logging

def setLogger():

  #logging.basicConfig(level=logging.DEBUG)

  logger    = logging.getLogger()
  handler   = logging.StreamHandler()
  formatter = logging.Formatter(
        '[%(asctime)s]:\t%(message)s')
  handler.setFormatter(formatter)
  logger .addHandler(handler)
  logger .setLevel(logging.INFO)

  return logger

def getLogger():

  return logging.getLogger()
