# coding=utf-8
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import random
from app.models import Node
import json
import MySQLdb


def painting(request):
    line_id = request.GET.get("line_id", None)
    edit_right = request.GET.get("edit_right", None)
    if line_id is None:
        line_id = 1
    if edit_right is None:
        edit_right = 0

    print "line_id: " ,line_id
    print "edit_right: " ,edit_right
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306, charset="utf8")
        cur = conn.cursor()
        conn.select_db('electricity')
        cur.execute('select * from app_node WHERE line_id=%s limit 10', str(line_id))
        results = cur.fetchall()
        cur.execute('select * from app_line where id=%s', str(line_id))
        line_result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    # print line_result
    Painted = True
    line = {}
    line["id"] = line_result[0]
    line["name"] = line_result[1]
    line["X"] = line_result[2]
    line["Y"] = line_result[3]
    if line["X"] is None or line["Y"] is None:
        Painted = False
    # print line

    node_list = []
    for row in results:
        node = {}
        node["id"] = row[0]
        node["name"] = row[1]
        node["father_id"] = row[2]
        node["node_type"] = row[3]
        node["X"] = row[4]
        node["Y"] = row[5]
        node["description"] = row[6]
        node["online"] = row[7]
        node["status"] = row[8]
        if node["X"] is None or node["Y"] is None:
            Painted = False
        node_list.append(node)
    node_id = []
    node_id.append(0)
    step = 0
    ret_data = []
    ret_data.append(Painted)
    node_ret_data = []

    while len(node_list) >= len(node_id):
        node_list_len = len(node_list)
        for i in range(node_list_len):
            node = node_list[i]
            if node["father_id"] == node_id[step]:
                node_id.append(node["id"])
                node_ret_data.append(node)
        step += 1
    ret_data.append(node_ret_data)
    return render(request, "app/index.html", {
        "data": json.dumps(ret_data),
        "line": json.dumps(line),
        "edit_right": edit_right,
    })


@csrf_exempt
def update_position(request):
    node_id = request.POST.get("node_id", None)
    node_x = request.POST.get("node_x", None)
    node_y = request.POST.get("node_y", None)
    print "node_save"
    print node_id
    print node_x
    print node_y
    print "node_save_data_finished"
    if node_id is None or node_x is None or node_y is None:
        return HttpResponse("error")
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306, charset="utf8")
        cur = conn.cursor()
        conn.select_db('electricity')
        cur.execute('update app_node set X = %s, Y = %s where id=%d' % (node_x, node_y, int(node_id)))
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        return HttpResponse("error")
    return HttpResponse("success")


@csrf_exempt
def update_root_position(request):
    line_id = request.POST.get("line_id", None)
    root_x = request.POST.get("root_x", None)
    root_y = request.POST.get("root_y", None)
    # print "root_save"
    # print line_id
    # print root_x
    # print root_y
    # print "root_save_end"
    if line_id is None or root_x is None or root_y is None:
        print "NONE"
        return HttpResponse("error")
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306, charset="utf8")
        cur = conn.cursor()
        conn.select_db('electricity')
        # print "xx"
        cur.execute('update app_line set root_x = %s, root_y = %s where id=%d' % (root_x, root_y, int(line_id)))
        # print "yy"
        conn.commit()
        cur.close()
        conn.close()
        # print "success"
    except MySQLdb.Error, e:
        print str(e)
        # print "error"
        return HttpResponse("error")
    return HttpResponse("success")

# Create your views here.
