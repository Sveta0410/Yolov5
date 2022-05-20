#from track import detect
#import psycopg2

#def test_smt():
#    assert


#def test_db_connection():
#    assert psycopg2.connect(database="yolo_db", user="postgres", password="123", host="localhost", port="5432")

def test_a():
    assert 0 * 10 == 0


# def test_b():
#     try:
#         conn = psycopg2.connect(database="yolo_db", user="postgres", password="123", host="localhost", port="5432")
#         conn.close()
#         return True
#     except:
#         return False

import pytest

from add_to_db import add_to_db


def test_name():
    inf = {'name1': 'fight', 'accuracy1': 13.397889999999999, 'time1': 16, 'time_ent_1': '10:57:08',
           'time_out_1': '10:57:19', 'name2': 'fight', 'accuracy2': 74.86325999999995, 'time2': 91,
           'time_ent_2': '10:57:08', 'time_out_2': '10:58:02', 'name3': 'fight', 'accuracy3': 1.45782, 'time3': 2,
           'time_ent_3': '10:57:21', 'time_out_3': '10:57:21', 'name4': 'fight', 'accuracy4': 6.755979999999999,
           'time4': 9, 'time_ent_4': '10:57:24', 'time_out_4': '10:57:29', 'name7': 'fight',
           'accuracy7': 15.783180000000003, 'time7': 21, 'time_ent_7': '10:57:41', 'time_out_7': '10:57:54',
           'name9': 'fight', 'accuracy9': 19.90835, 'time9': 26, 'time_ent_9': '10:58:00', 'time_out_9': '10:58:16',
           'name11': 'fight', 'accuracy11': 53.42228000000002, 'time11': 70, 'time_ent_11': '10:58:07',
           'time_out_11': '10:58:45', 'name12': 'fight', 'accuracy12': 1.3086600000000002, 'time12': 2,
           'time_ent_12': '10:58:27', 'time_out_12': '10:58:28', 'name13': 'fight', 'accuracy13': 7.4717899999999995,
           'time13': 10, 'time_ent_13': '10:58:33', 'time_out_13': '10:58:39', 'name15': 'fight', 'accuracy15': 2.15566,
           'time15': 3, 'time_ent_15': '10:58:44', 'time_out_15': '10:58:45'}
    all_id = [1, 2, 3, 4, 7, 9, 11, 12, 13]
    add_to_db(inf, all_id)

    i = 1
    name1 = str(inf['name%s' % i])
    assert name1 == 'fight'
    assert add_to_db(inf, all_id)[0] == ['1', 'fight', '10:57:08', '10:57:19', '0.84']
    assert add_to_db(inf, all_id)[1] == ['2', 'fight', '10:57:08', '10:58:02', '0.82']

