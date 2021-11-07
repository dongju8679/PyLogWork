import logging
import logging.handlers
import datetime
import os



current_dir = os.path.dirname(os.path.realpath(__file__))
current_file = os.path.basename(__file__)
current_file_name = current_file[:-3]  # xxxx.py
#LOG_FILENAME = 'log-{}'.format(current_file_name)
LOG_FILENAME = '{}'.format(current_file_name)

log_dir = '{}/logs'.format(current_dir)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
#formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
formatter = logging.Formatter('%(asctime)s %(message)s', "%Y%m%d_%H%M%S")

streamhandler = logging.StreamHandler()
streamhandler.setFormatter(formatter)
# logger.addHandler(streamhandler)
# filehandler = logging.FileHandler(
#     './logs/{}_{:%Y%m%d_%H%M%S}.log'.format(LOG_FILENAME, datetime.datetime.now()), encoding='utf-8')
# filehandler = logging.FileHandler('./logs/abc.log'.format(LOG_FILENAME, datetime.datetime.now()), encoding='utf-8')
# file max size를 10MB로 설정
# file_max_bytes = 10 * 1024 * 1024
file_max_bytes = 1024*1024*1024
filehandler = logging.handlers.RotatingFileHandler('./logs/abc.log'.format(), maxBytes=file_max_bytes, backupCount=10000, encoding='utf-8')
# filehandler = logging.FileHandler(
#     './logs/abc1_{:%Y%m%d%H%M}.log'.format(datetime.datetime.now()), encoding='utf-8')
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)

# logger.debug("debug mode")
# logger.info("info mode")
# logger.warning("warn mode")
# #logger.info("current_dir = {current_dir}", current_dir)
# logger.info(f"testttt = {current_dir}")
# logger.warning('abc %s', current_dir)
