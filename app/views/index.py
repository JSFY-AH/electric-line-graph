# coding=utf-8
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import random
from app.models import Node
import json
import database


def painting(request):
    line_id = request.GET.get("line_id", None)
    edit_right = request.GET.get("edit_right", None)
    if line_id is None:
        line_id = 1
    if edit_right is None:
        edit_right = 0

    try:
        DB = database.SqlServer()
        conn = DB.connnect()
        cur = conn.cursor()
        cur.execute('select * from MathinInstance WHERE LineID=? and IsRemove = 0 and ChildPointNo != 0', int(line_id))
        results = cur.fetchall()
        cur.execute('select * from Line where LineID=?', int(line_id))
        line_result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
    except:
        print "db error"
    Painted = True
    line = {}
    line["id"] = line_result[0]
    line["areaID"] = line_result[2]
    line["name"] = line_result[3]
    line["instanceId"] = line_result[7]
    print line
    areaID = int(line["areaID"])
    try:
        DB = database.SqlServer()
        conn = DB.connnect()
        cur = conn.cursor()
        cur.execute('select * from Area where AreaID=?', areaID)
        area_result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
    except:
        print "db error"
    area = {}
    area["id"] = area_result[0]
    area["name"] = area_result[1]
	
    node_list = []
    for row in results:
        node = {}
        node["id"] = row[0]
        node["name"] = row[14]
        node["father_id"] = row[19]
        node["X"] = row[20]
        node["Y"] = row[21]
        node["description"] = "description"
        node["online"] = row[9]
        node["status"] = row[9]
        if node["X"] is None or node["Y"] is None:
            Painted = False
        node_list.append(node)
    # print node_list
    node_id = []
    node_id.append(0)
    step = 0
    ret_data = []
    ret_data.append(Painted)
    node_ret_data = []
    print "node_list_len ======="
    print len(node_list)
    while len(node_list) >= len(node_id):
        node_list_len = len(node_list)
        for i in range(node_list_len):
            node = node_list[i]
            if node["father_id"] == node_id[step]:
                node_id.append(node["id"])
                node_ret_data.append(node)
        step += 1
    # print node_ret_data
    ret_data.append(node_ret_data)
    # print len(ret_data)
    return render(request, "app/index2.html", {
        "data": json.dumps(ret_data),
        "line": json.dumps(line),
        "edit_right": edit_right,
		"area": json.dumps(area),
    })


@csrf_exempt
def update_position(request):
    node_id = request.POST.get("node_id", None)
    node_x = request.POST.get("node_x", None)
    node_y = request.POST.get("node_y", None)
    if node_id is None or node_x is None or node_y is None:
        return HttpResponse("error")
    try:
        DB = database.SqlServer()
        conn = DB.connnect()
        cur = conn.cursor()
        cur.execute('update MathinInstance set X = ?, Y = ? where id=?', float(node_x), float(node_y), int(node_id))
        conn.commit()
        cur.close()
        conn.close()
    except:
        return HttpResponse("error")
    return HttpResponse("success")


@csrf_exempt
def update_root_position(request):
    line_id = request.POST.get("line_id", None)
    root_x = request.POST.get("root_x", None)
    root_y = request.POST.get("root_y", None)
    if line_id is None or root_x is None or root_y is None:
        return HttpResponse("error")
    try:
        DB = database.SqlServer()
        conn = DB.connnect()
        cur = conn.cursor()
        cur.execute('update Line set x = ?, y = ? where LineID=?', float(root_x), float(root_y), int(line_id))
        conn.commit()
        cur.close()
        conn.close()
    except:
        return HttpResponse("error")
    return HttpResponse("success")

# Create your views here.
