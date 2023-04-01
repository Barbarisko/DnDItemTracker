from collections import defaultdict
from contextlib import contextmanager
from psycopg2 import InterfaceError, DatabaseError

from Loging import *
from DomainExeption import DatabaseGatewayError

from flask import abort


def abort_on_failure():
    def decorate(f):
        def applicator(*args, **kwargs):
            try:
                return f(*args,**kwargs)
            except InterfaceError as ie:
                data_log("Interface error occured: " + str(ie), logging.ERROR)
                abort(500)
            except DatabaseError as dbe:
                data_log("Database error occured: " + str(dbe), logging.ERROR)
                abort(500)
            except DatabaseGatewayError as my_db_error:
                data_log("Database error occured: " + str(my_db_error), logging.ERROR)
                abort(500)
            except KeyError as ke:
                api_log("API Error: request does not have required params" + str(ke), logging.ERROR)
                abort(400)
        return applicator
    return decorate
