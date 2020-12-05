#!/usr/bin/env python3

import numpy as np
from bokeh.plotting import figure
from bokeh.models import HoverTool
import panel as pn
import panel.widgets as pnw


pn.extension()


# ## Simulation


def regular_shade_drop(size, trails=1):
    """
    Generates random drops for regular shade
    
    Parameters
    ----------
    size: int
        Number of regular shade kills in the trail
    trails: int
        Number of trails to simulate
    """
    return np.random.choice(["None", "Medicinal Herb", "Old Schoolbook", "Dented Metal Bat"], size=[trails, size], p=[0.74, 0.15, 0.1, 0.01])


def regular_shade_2_drop(size, trails=1):
    return np.random.choice(["None", "Medicinal Herb", "Used Coloring Book", "Rusty Kitchen Knife", "Broken Saw"], size=[trails, size], p=[0.72, 0.15, 0.1, 0.02, 0.01])


def large_shade_drop(size, trails=1):
    return np.random.choice(["None", "Defense Drop", "Thick Dictionary", "Stopped Clock", "Leather Boots"], size=[trails, size], p=[0.745, 0.15, 0.08, 0.02, 0.005])


def large_shade_2_drop(size, trails=1):
    return np.random.choice(["None", "Strength Drop", "Closed Book", "Broken Wristwatch", "Leather Boots"], size=[trails, size], p=[0.745, 0.15, 0.08, 0.02, 0.005])


def boar_drop(size, trails=1):
    return np.random.choice(["Boar Meat", "Boar Hide", "Boar Liver"], size=[trails, size], p=[0.5, 0.3, 0.2])


def sg01_drop(size, trails=1):
    return np.random.choice(['Dented Metal Board', "Broken Arm", "Broken Antenna"], size=[trails, size], p=[0.5, 0.3, 0.2])


def sg10_drop(size, trails=1):
    return np.random.choice(["Stripped Bolt", "Broken Antenna", "Broken Motor", "Titanium Alloy"], size=[trails, size], p=[0.4, 0.3, 0.2, 0.1])




conversion_dict = {"None": 0,
                   'Medicinal Herb': 10,
                   'Lure': 20,
                   'Defense Drop': 100,
                   'Used Coloring Book': 100,
                   'Broken Arm': 120,
                   'Dented Metal Board': 150,
                   'Broken Antenna': 150,
                   'Thick Dictionary': 160,
                   'Old Schoolbook': 160,
                   'Stripped Bolt': 180,
                   'Closed Book': 250,
                   'Broken Wristwatch': 280,
                   'Boar Meat': 300,
                   'Rusty Kitchen Knife': 300,
                   'Broken Motor': 400,
                   'Leather Boots': 620,
                   'Boar Hide': 700,
                   'Stopped Clock': 700,
                   'Broken Saw': 800,
                   'Titanium Alloy': 800,
                   'Dented Metal Bat': 900,
                   'Pyrite': 1500,
                   'Boar Liver': 2500}



# simulate ten runs with four regular shade kills
res = regular_shade_drop(4, 10)
res


def get_returns(drops):
    """
    Calculates the values for drops, by converting the names to the values of the conversion dict and then summing over all drops in a trail.
    
    Parameters
    ----------
    drops: np.ndarray
        2D array with the first axis beeing the trails and the second one beeing the drops in the trail 
    """
    total_money = np.vectorize(conversion_dict.get)(drops).sum(axis=1)
    return total_money


# return of the the 10 runs done simulated above 
get_returns(res)


# ## Visualization


def money_hist(x,y):
    p = figure()
    p.xaxis.axis_label="Money"
    p.yaxis.axis_label="No. Occurances"
    p.vbar(x, 1, y)
    return p

def money_cdf(x, cdf):
    hover_tool = HoverTool(
        tooltips = [("", "P(money < $x{(0.)}) = @y")],
        mode="vline"
    )

    p = figure()
    p.add_tools(hover_tool)
    p.xaxis.axis_label="Money"
    p.yaxis.axis_label="Probability"
    p.line(x, cdf)
    return p

def dashboard(results):
    hist_x,hist_y = np.unique(results, return_counts=True)
    cdf = np.cumsum(hist_y)
    cdf = cdf/cdf.max()
    return pn.Row(money_hist(hist_x, hist_y), money_cdf(hist_x, cdf))


# ### Simulate drops before the shop


def drops_before_shop(trails):
    regular_shade_drops = regular_shade_drop(size=12, trails=trails)
    regular_shade_2_drops = regular_shade_2_drop(size=4, trails=trails)
    large_shade_drops = large_shade_drop(size=10, trails=trails)
    large_shade_2_drops = large_shade_drop(size=2, trails=trails)
    boar_drops = boar_drop(size=1, trails=trails)
    
    money = get_returns(regular_shade_drops)
    money += get_returns(regular_shade_2_drops)
    money += get_returns(large_shade_drops)
    money += get_returns(large_shade_2_drops)
    money += get_returns(boar_drops)
    money += 20 # for the LURE
    return money

results_before_shop = drops_before_shop(10*3)


dashboard(results_before_shop)


# #### Notes
# - Bimodal distribution due to the large value of 'Boar Liver'.

# ### After Shop


def drops_after_shop(trails):
    sg01_drops = sg01_drop(size=56, trails=trails)
    sg10_drops = sg10_drop(size=17, trails=trails)
    regular_shade_drops = regular_shade_drop(size=4, trails=trails)

    money = get_returns(sg01_drops)
    money += get_returns(sg10_drops)
    money += get_returns(regular_shade_drops)
    return money



results_after_shop = drops_after_shop(10*3)



dashboard(results_after_shop)


# ### Full simulation with before/after shop + funds


results_all = results_before_shop + results_after_shop - 400
print(results_all)
for result in results_all:
	print(result)



dashboard(results_all)




