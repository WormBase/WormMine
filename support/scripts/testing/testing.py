# Paulo Nuin June 2020

import logging
import click
import testing_development
import settings
from intermine.webservice import Service
import coloredlogs

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')
logging.getLogger("intermine").setLevel(logging.INFO)

def development():

    service = Service("http://im-dev1.wormbase.org/tools/wormmine/service")
    settings.init()
    for x in dir(testing_development):
        item = getattr(testing_development, x)
        if callable(item):
            if not item.__name__ in ['assert_result', 'Service', 'assert_greater', 'save_txt_file']:
                item(service)

    # test = [('query_01', 'Gene'), ('query_02', 'Gene')]
    logger.info(str(len(settings.to_check)) + ' query(ies) failed')
    for query in settings.to_check:
    # for query in test:
        logger.warning(query[0] + ' ' + query[1])
        item = getattr(testing_development, query[0])
        item(service, True)

if __name__ == '__main__':


    development()