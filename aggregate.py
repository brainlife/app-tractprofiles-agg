#!/usr/bin/env python

import csv
import json
import numpy
import glob
import sys
import os

plots = []

#ad_1,ad_2,fa_1,fa_2,md_1,md_2,rd_1,rd_2

#load densities and compute std/mean
with open('config.json') as config_f:
    config = json.load(config_f)
    ad = {}
    fa = {}
    md = {}
    rd = {}
    for output_dir in config["outputs"]:
        print("finding csv in ", output_dir)
        for path in glob.glob(output_dir+"/*.csv"):
            fullname = os.path.basename(path)
            name = os.path.splitext(fullname)[0]
            profile = numpy.genfromtxt(path, skip_header=1, delimiter=',')

            if not name in ad:
                ad[name] = []
                fa[name] = []
                md[name] = []
                rd[name] = []
            ad[name].append(profile[:,0])
            fa[name].append(profile[:,2])
            md[name].append(profile[:,4])
            rd[name].append(profile[:,6])

###################################################################################################
for name in ad:
    data = [] 
    idx=0
    all = []
    for profile in fa[name]:
        all.append(profile)
        #replace NaN with 0
        where_are_NaNs = numpy.isnan(profile)
        profile[where_are_NaNs] = 0
        #data.append({
        #    "y": numpy.round(profile, 4).tolist(),
        #    "name": config["_inputs"][idx]["meta"]["subject"],
        #    "type": "scatter",
        #    "opacity": 0.3
        #})
        #idx+=1

    data.append({
        "y": numpy.round(numpy.mean(all, axis=0), 4).tolist(),
        "error_y": {
            "type": "data",
            "array": numpy.round(numpy.std(all, axis=0), 6).tolist(),
            "visible": True,
        },
        "name": "mean",
        "type": "scatter",
        "line": {
            "color": "black",
        },
    })
    plot = {}
    plot["type"] = "plotly"
    plot["name"] = name+" FA"
    plot["data"] = data
    plot["layout"] = {
        "yaxis": {
            "title": "FA",
            "range": [0, 1],
        },
    }
    plots.append(plot)

###################################################################################################
for name in md:
    data = [] 
    idx=0
    all = []
    for profile in md[name]:
        all.append(profile)
        #replace NaN with 0
        where_are_NaNs = numpy.isnan(profile)
        profile[where_are_NaNs] = 0
        #data.append({
        #    "y": numpy.round(profile, 4).tolist(),
        #    "name": config["_inputs"][idx]["meta"]["subject"],
        #    "type": "scatter",
        #    "opacity": 0.3
        #})
        #idx+=1

    data.append({
        "y": numpy.round(numpy.mean(all, axis=0), 4).tolist(),
        "error_y": {
            "type": "data",
            "array": numpy.round(numpy.std(all, axis=0), 6).tolist(),
            "visible": True,
        },
        "name": "mean",
        "type": "scatter",
        "line": {
            "color": "black",
        },
    })
    plot = {}
    plot["type"] = "plotly"
    plot["name"] = name+" MD"
    plot["data"] = data
    plot["layout"] = {
        "yaxis": {
            #"domain": [0, 0.45],
            "title": "MD",
            #"anchor": "y_fa",
            "range": [0, 1],
        },
    }
    plots.append(plot)

#save product.json
product = {}
product["brainlife"] = plots
with open("product.json", "w") as fp:
    json.dump(product, fp)


