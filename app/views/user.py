# coding=utf-8
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import random
import json
import hashlib
import database


def get_md5_value(src):
    myMd5 = hashlib.md5()
    myMd5.update(src)
    yMd5_Digest = myMd5.hexdigest()
    return yMd5_Digest

@csrf_exempt
def login(request):
    print "xxxx"
    username = request.GET.get("username", None)
    password = request.GET.get("password", None)
    print "received Data:"
    print username
    print password
    print "received end"
    ret_data = {}
    ret_data["result"] = "error"
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
        user_id = user_db[0]
        ret_data = {}
        ret_data["user_id"] = user_id
        print ret_data
        return HttpResponse(json.dumps(ret_data))


def getAreaList(request):
    user_id = request.GET.get("user_id", None)
    ret_data = {}
    ret_data["result"] = "error"
    if user_id is None:
        return HttpResponse(json.dumps(ret_data))
    DB = database.SqlServer()
    conn = DB.connnect()
    cur = conn.cursor()
    cur.execute('select AreaID from UserRange where UserID=?', user_id)
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
    ret_data = {}
    ret_data["result"] = "success"
    ret_data["areaData"] = AreaList
    return HttpResponse(json.dumps(ret_data))


def getLineList(request):
    area_id = request.GET.get("area_id", None)
    ret_data = {}
    ret_data["result"] = "error"
    if area_id is None:
        return HttpResponse(json.dumps(ret_data))
    DB = database.SqlServer()
    conn = DB.connnect()
    cur = conn.cursor()
    cur.execute('select * from Line where AreaID=? and isRemove = 0', area_id)
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
    ret_data = {}
    ret_data["result"] = "success"
    ret_data["lineData"] = LineList
    return HttpResponse(json.dumps(ret_data))