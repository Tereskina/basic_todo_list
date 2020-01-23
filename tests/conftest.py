import pytest

import service

TASK_ID = 1
TASK_TEXT = "text text"
TASKS = {TASK_ID: TASK_TEXT}

@pytest.fixture()
def tasks():
    service.TASKS = TASKS

@pytest.fixture()
def tasks_empty():
    service.TASKS = TASKS

@pytest.fixture()
def db(config):
    db = open_connection(config[db])
def db_disconnect():
	db.close_connection()
	request.addfinalizer(db_disconnect)
	return db