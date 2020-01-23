import datetime

import pytest

import service
import sys

TASK_ID = 1
TASK_TEXT = "text text"
TASKS = {TASK_ID: TASK_TEXT}

service.TASKS = TASKS

def test_get_task_id_exists(tasks):
    result_task = service.get_task(TASK_ID)
    assert result_task == TASK_TEXT

def test_get_task_doesnt_exist(tasks):
    result_task = service.get_task(2)
    assert result_task is None

def test_get_all_tasks_empty(tasks_empty):
    service.TASKS = {}
    all_tasks = service.get_all_tasks()
    assert all_tasks == {}
    service.TASKS = TASKS

def test_get_all_tasks_not_empty(tasks):
    all_tasks = service.get_all_tasks()
    assert all_tasks == TASKS

def test_create_task_success():
    date = (
            datetime.datetime.now() + 
            datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
    task = service.create_task(date, TASK_TEXT)
    assert task 

def test_create_task_in_the_past():
    date = (
            datetime.datetime.now() - 
            datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
    
    task = service.create_task(date, TASK_TEXT)
    assert task is None

def func(x, y):
    return x + y
#Допустим, вот функция, которую мы тестируем, Можно параметризовать сам тест-кейс:

# @pytest.mark.parametrize("x", [-1, 0, 1, 2])
# @pytest.mark.parametrize("y", [-1,0, 1, 2])
# def test_sum_parametrized(x,y):
#     assert func(x, y) == x + y

@pytest.fixture(params=[-1, 0, 1, 2])
def x(request):
    return request.param

@pytest.fixture(params=[-1, 0, 1, 2])
def y(request):
    return request.param


def test_sum_parametrized(x,y):
    assert func(x, y) == x + y

# def setup():
#     print ("Setup test")
 
# def teardown():
#     print ("Teardown test")

# def setup_module(module):
#     print ("Setup module")
 
# def teardown_module(module):
#     print ("Teardown module")
 
# def setup_function(function):
#     print ("Setup function")
 
# def teardown_function(function):
#     print ("Teardown function")
 
# def test_something_one():
#     print("Test 1")
 
# def test_something_two():
#     print("Test 2")

# @pytest.mark.xfail()
# def test_xfail():
#     assert False
    
# @pytest.mark.xfail(
#     sys.version.startswith("3"),
#     reason="supported only in older Python versions")
# def test_xfail_condition():
#     assert False

# @pytest.mark.skipif(
#     sys.version.startswith("3"),
#     reason="supported only in older Python versions")
# def test_skipif():
#     assert False

# @pytest.mark.xfail()
# def test_xfail_fail():
#     assert True