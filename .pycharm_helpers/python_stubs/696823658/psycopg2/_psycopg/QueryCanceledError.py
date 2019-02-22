# encoding: utf-8
# module psycopg2._psycopg
# from /home/ubuntu/py36/lib/python3.5/site-packages/psycopg2/_psycopg.cpython-35m-x86_64-linux-gnu.so
# by generator 1.146
""" psycopg PostgreSQL driver """

# imports
import psycopg2 as __psycopg2
import psycopg2.extensions as __psycopg2_extensions


class QueryCanceledError(__psycopg2.OperationalError):
    """ Error related to SQL query cancellation. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


