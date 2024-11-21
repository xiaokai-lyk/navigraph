# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:37:55 2024

@author: xk
"""

import io
import base64
from gevent import pywsgi



import networkx as nx

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import flask
from flask import redirect, render_template,url_for
backGroundImg=plt.imread("campus.png")

def backToIndex():
    return flask.redirect(url_for("index"),code=301)


app = flask.Flask("DemoOfNavi-graphAPP")


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/api/<op>',methods=["GET","POST"])
def api(op):
    request=flask.request
    import json
    if request.method == "POST":
        match op:
            case "navi":
                try:
                    sourcePoint=int(request.get_json()['source'])
                    targetPoint=int(request.get_json()['target'])
                except:
                    return render_template('err.html',code=416,error="OH!Parameters not available!不是哥们,你的参数呢?")
                try:
                    img = io.BytesIO()
                    Gmain=nx.Graph()
                    _,ax=plt.subplots()
                    ax.imshow(backGroundImg,extent=[0,640,0,480])
                    data_list=json.load(open("node_list.json",encoding='utf-8'))['edges']

                    Gmain.add_weighted_edges_from(data_list)
                    data_list=json.load(open("node_list.json",encoding='utf-8'))['pos']
                    pos={}
                    for i in data_list:
                        pos[int(i)]=data_list[i]                        
                    nx.draw(Gmain, pos, with_labels=True, alpha=0.5)
                    labels = nx.get_edge_attributes(Gmain, 'weight')
                    #nx.draw_networkx_edge_labels(Gmain, pos, edge_labels=labels)

                    try:
                        minWPath= nx.dijkstra_path(Gmain, source=sourcePoint, target=targetPoint)
                    except:
                        return render_template('err.html',code=416,error="OH!No available path!你要上天啊(bushi)")

                    edgeList = []
                    for i in range(len(minWPath)-1):
                        edgeList.append((minWPath[i], minWPath[i+1]))
                    nx.draw_networkx_edges(Gmain, pos, edgelist=edgeList, width=4,label=labels,ax=ax)
                    

                    plt.savefig(img, format='png')
                    plt.close()

                    if img.readable():
                        image = base64.b64encode(img.getvalue()).decode()
                    else:
                        return render_template('err.html',code=500,error="buffer is not readable!Strange:-(")
                    return flask.jsonify({"image_base64":image})
                except BaseException as e:
                    return render_template('err.html',code=500,error=str(e))
            case "nodes":
                import json
                return flask.jsonify(json.load(open("node_list.json",encoding='utf-8'))['nodes'])
            case _:
                return str(op)
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template("404.html")

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0',80), app)
    server.serve_forever()