from threading import Thread
import os
import re
import logging
import time

from robotbackgroundlogger import BackgroundLogger

logger = BackgroundLogger()
threads = {}


def log_on_thread(message, level='INFO', html=False, name=None):
    thread = Thread(name=name, target=logger.write, args=[message, level, html])
    thread.start()
    threads[thread.getName()] = thread


def log_on_threads(message, name_prefix, count):
    for i in range(int(count)):
        name = '%s %d' % (name_prefix, i+1)
        thread = Thread(name=name, target=logger.info,
                        args=['%s says <i>%s</i>.' % (name, message)],
                        kwargs={'html': True})
        thread.start()
        threads[thread.getName()] = thread


def finish_all():
    while threads:
        threads.popitem()[1].join()
    logger.log_background_messages()


def finish_one(name):
    threads.pop(name).join()
    logger.log_background_messages(name)




def output_file(self, file_type, path):
    """Finished output, report, log, debug, or xunit file"""
    for logger in self._loggers.all_loggers():
        logger.output_file(file_type, path)



def test():
    cmd = ' net state" '
    output = os.popen(cmd).read()
    match1 = re.findall('.* (START).*',output)
    mat1 = ['START']
    if match1 == mat1:
        print("output: " + output)


def my_logger(arg):
    # logger.console('Got console %s.' % arg)
    # logger.info('<i>This</i> is a test case %s.'% arg, html=True)
    # logger.info(arg)
    # print('---TEST------------')
    logger.write(arg,level='INFO', html=False)



def my_logging(arg):
        logging.basicConfig(format='%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s',
                            datefmt="%Y-%m-%d-%H-%M-%S",
                            filename=time.strftime("myLogging-%Y-%m-%d.log"))
        logging.info(arg)
        logging.debug("debug")
        logging.info("info")
        logging.warning("warning")
        logging.error("error")
        logging.critical("critical")
        print(time.strftime("myLogging-%Y-%m-%d.log"))
        logging.info(logging.__status__)


# my_logger('---------HADSAI-TESTING-LOGGER--------')
# my_logging('---------HADSAI-TESTING-LOGGING--------')