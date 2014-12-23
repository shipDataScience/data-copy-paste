import json
import os
import logging

logging.info("Copy-Paste data plugin starting!")

try:
  logging.info("loading config from environment!")
  cfg_json = os.environ['SDS_PLUGIN_CONFIG_JSON']
except KeyError:
  logging.error("Failed to load config.")
  raise

try: 
  logging.info("parsing config.")
  cfg = json.loads(cfg_json)
except StandardError:
  logging.error("failed to parse config as json---try running it through a validator.")
  raise

try:
  logging.info("setting option values from config!")
  path       = cfg['outPath']
except KeyError:
  logging.error("Required options not specified.")
  raise

try:
  logging.info("Moving file!")
  os.rename("text.txt", path )
except StandardError:
  logging.error("Attempt to move file failed!.")
  raise
logging.info("success!")

