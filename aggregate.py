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

            #print(name)
            #print(profile[:,1])

            if not name in ad:
                ad[name] = []
                fa[name] = []
                md[name] = []
                rd[name] = []
            ad[name].append(profile[:,1])
            fa[name].append(profile[:,3])
            md[name].append(profile[:,5])
            rd[name].append(profile[:,7])

            #sys.exit(1)


layout = {
#    "yaxis": {
#        "autorange": "reversed"
#    }
}

for name in ad:
    profiles = ad[name]
    data = [] 

    #add all profiles
    idx=0
    for profile in profiles:
        #replace NaN with 0
        where_are_NaNs = numpy.isnan(profile)
        profile[where_are_NaNs] = 0
        data.append({
            "x": len(profile),
            "y": profile.tolist(),
            "name": "output"+str(idx),
            "type": "scatter"
        })
        idx+=1

    #generate heatmap from density std/mean
    plot = {}
    plot["type"] = "plotly"
    plot["name"] = name
    plot["data"] = data
    plot["layout"] = layout
    plots.append(plot)

#save product.json
product = {}
product["brainlife"] = plots
with open("product.json", "w") as fp:
    json.dump(product, fp)
