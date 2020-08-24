# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2020/8/23 17:12
# Description: sql
import pymysql
from configs import *
from loguru import logger


class MysqlDb(object):
    """mysql client"""

    def __init__(self):
        self.db = pymysql.connect(host=HOST, user=USERNAME, password=PASSWORD, database=DATABASE, port=PORT)
        self.cursor = self.db.cursor()

    def close(self):
        self.db.close()

    def create_table(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            logger.error(e)
        finally:
            self.db.close()

    def drop_table(self, tab_name):
        try:
            drop_sql = "DROP TABLE IF EXISTS %s" % tab_name
            self.cursor.execute(drop_sql)
        except Exception as e:
            logger.error(e)
        finally:
            self.cursor.close()
            self.db.close()

    def insert_update_del(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            logger.info("insert_update_del success")
        except Exception as e:
            logger.error(e)
            self.db.rollback()
        finally:
            self.cursor.close()
            self.db.close()

    def query(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()  # all records
            return results
        except Exception as e:
            logger.error("Error: unable to fetch data")
            logger.error(e)
        finally:
            self.cursor.close()
            self.db.close()


# db = MysqlDb()

# create table
# create_sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
# db.create_table(create_sql)

# insert data
# insert_sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# db.insert_update_del(insert_sql)

# query
# query_sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %s" % 1000
# results = db.query(query_sql)
# for e in results:
#     logger.info(e)
#     logger.info("fname=%s, lname=%s, age=%s, sex=%s, income=%s" % (e[0], e[1], e[2], e[3], e[4]))

# update
# 注意%c加单引号
# update_sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % "M"
# db.insert_update_del(update_sql)

# del
# del_sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % 20
# # db.insert_update_del(del_sql)
