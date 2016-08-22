# coding=utf-8
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import random
import json
import MySQLdb
import pyodbc
import hashlib
import database


def get_md5_value(src):
    myMd5 = hashlib.md5()
    myMd5.update(src)
    yMd5_Digest = myMd5.hexdigest()
    return yMd5_Digest


def login(request):
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)
    ret_data = {}
    ret_data["code"] = 401
    ret_data["data"] = "error"
    if username is None or password is None:
        return HttpResponse(json.dumps(ret_data))
    DB = database.SqlServer()
    conn = DB.connnect()
    cur = conn.cursor()
    cur.execute('select * from UserInfo where Name=? and password=?', username, get_md5_value(password))
    user_db = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    print user_db
    if user_db is None:
        return HttpResponse(json.dumps(ret_data))
    else:
        user = {}
        user["id"] = user_db[0]
        user["name"] = user_db[1]
        ret_data = {}
        ret_data["code"] = 200
        ret_data["data"] = user

        return HttpResponse(json.dumps(ret_data))


def getAreaList(request):
    username = request.GET.get("username", None)
    ret_data = {}
    ret_data["code"] = 401
    ret_data["data"] = "error"
    if username is None:
        return HttpResponse(json.dumps(ret_data))
    DB = database.SqlServer()
    conn = DB.connnect()
    cur = conn.cursor()
    cur.execute('select AreaID from UserRange where UserID=?', username)
    area_query = cur.fetchall()
    AreaList = []
    for row in area_query:
        area_id = row[0]
        cur.execute('select * from Area where AreaID=? and IsRemove = 0', area_id)
        Area_query = cur.fetchone()
        area_dic = {}
        area_dic["AreaID"] = Area_query[0]
        area_dic["Name"] = Area_query[1]
        area_dic["GroupID"] = Area_query[2]
        area_dic["Phone"] = Area_query[3]
        area_dic["Ver"] = str(Area_query[4])
        AreaList.append(area_dic)
    print AreaList
    conn.commit()
    cur.close()
    conn.close()
    return HttpResponse(json.dumps(AreaList))


def getLineList(request):
    areaID = request.GET.get("areaID", None)
    ret_data = {}
    ret_data["code"] = 401
    ret_data["data"] = "error"
    if areaID is None:
        return HttpResponse(json.dumps(ret_data))
    DB = database.SqlServer()
    conn = DB.connnect()
    cur = conn.cursor()
    cur.execute('select * from Line where AreaID=? and isRemove = 0', areaID)
    line_query = cur.fetchall()
    LineList = []
    for row in line_query:
        line_dic = {}
        line_dic["LineID"] = row[0]
        line_dic["GroupID"] = row[1]
        line_dic["AreaID"] = row[2]
        line_dic["LineName"] = row[3]
        line_dic["Phone"] = row[4]
        line_dic["Ver"] = str(row[5])
        line_dic["RootInstanceID"] = row[7]
        LineList.append(line_dic)
    print "LineList", LineList
    return HttpResponse(json.dumps(LineList))