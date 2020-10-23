#!usr/bin/env/python3

# Using context manager to backup database offline

import contextlib


def stop_db():
    print('systemct1 stop postgresql.service')


def run_db():
    print('systemct1 start postgresql.service')


class Handler(object):
    def __enter__(self):
        stop_db()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        run_db()


def db_backup():
    print('pg_dump database')


# def main():
#     with Handler():
#         db_backup()


# using contextlib to perform the same function

@contextlib.contextmanager
def handler():
    stop_db()
    yield
    run_db()


def main():
    with handler():
        db_backup()
