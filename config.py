from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)


class Database:
    def __init__(self):
        host = "104.199.117.142"
        user = "abby"
        password = "cpsc408"
        db = "cpsc408"

        self.con = pymysql.connect(host=host, user=user, password=password, db=db,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def __getitem__(self):
        self.cur = self.con.cursor()
        return self.cur

    def __getstate__(self):
        return self.con