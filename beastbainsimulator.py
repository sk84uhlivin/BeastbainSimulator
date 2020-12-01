import numpy as np

# import json
# from tqdm import tqdm_notebook
# from matplotlib import pyplot as plt


def regular_shade_drop(size):
    return np.random.choice(["None", "Medicinal Herb", "Old Schoolbook", "Dented Metal Bat"], size=size,
                            p=[0.74, 0.15, 0.1, 0.01])


def regular_shade_2_drop(size):
    return np.random.choice(["None", "Medicinal Herb", "Used Coloring Book", "Rusty Kitchen Knife", "Broken Saw"],
                            size=size, p=[0.72, 0.15, 0.1, 0.02, 0.01])


def large_shade_drop(size):
    return np.random.choice(["None", "Defense Drop", "Thick Dictionary", "Stopped Clock", "Leather Boots"], size=size,
                            p=[0.745, 0.15, 0.08, 0.02, 0.005])


def large_shade_2_drop(size):
    return np.random.choice(["None", "Strength Drop", "Closed Book", "Broken Wristwatch", "Leather Boots"], size=size,
                            p=[0.745, 0.15, 0.08, 0.02, 0.005])


def boar_drop(size):
    return np.random.choice(["Boar Meat", "Boar Hide", "Boar Liver"], size=size, p=[0.5, 0.3, 0.2])


def sg01_drop(size):
    return np.random.choice(["Dented Metal Plate", "Broken Arm", "Broken Antenna"], size=size, p=[0.5, 0.3, 0.2])


def sg10_drop(size):
    return np.random.choice(["Stripped Bolt", "Broken Antenna", "Broken Motor", "Titanium Alloy"], size=size,
                            p=[0.4, 0.3, 0.2, 0.1])


def get_returns(drop_names, drop_counts):
    total_money = 0
    for drop_name, drop_count in zip(drop_names, drop_counts):
        total_money = conversion_dict[drop_name] * drop_count
    return total_money


def drops_before_shop():
    regular_shade_drops = regular_shade_drop(size=12)
    regular_shade_2_drops = regular_shade_2_drop(size=4)
    large_shade_drops = large_shade_drop(size=10)
    large_shade_2_drops = large_shade_drop(size=2)
    boar_drops = boar_drop(size=1)

    # Why does each one refer to "regular_shade_drop_item_counts"?
    regular_shade_drop_items, regular_shade_drop_item_counts = np.unique(regular_shade_drops, return_counts=True)
    regular_shade_2_drop_items, regular_shade_drop_item_counts = np.unique(regular_shade_2_drops, return_counts=True)
    large_shade_drop_items, regular_shade_drop_item_counts = np.unique(large_shade_drops, return_counts=True)
    large_shade_2_drop_items, regular_shade_drop_item_counts = np.unique(large_shade_2_drops, return_counts=True)
    boar_drop_items, regular_shade_drop_item_counts = np.unique(boar_drops, return_counts=True)

    # Why does each one refer to "regular_shade_drop_item_counts"?
    money = 20 # for the LURE
    money += get_returns(regular_shade_drop_items, regular_shade_drop_item_counts)
    money += get_returns(regular_shade_2_drop_items, regular_shade_drop_item_counts)
    money += get_returns(large_shade_drop_items, regular_shade_drop_item_counts)
    money += get_returns(large_shade_2_drop_items, regular_shade_drop_item_counts)
    money += get_returns(boar_drop_items, regular_shade_drop_item_counts)
    return money


def drops_after_shop():
    sg01_drops = sg01_drop(size=56)
    sg10_drops = sg10_drop(size=17)
    regular_shade_drops = regular_shade_drop(size=4)

    # Why does each one refer to "regular_shade_drop_item_counts"?
    sg01_drop_items, regular_shade_drop_item_counts = np.unique(sg01_drops, return_counts=True)
    sg10_drop_items, regular_shade_drop_item_counts = np.unique(sg10_drops, return_counts=True)
    regular_shade_drop_items, regular_shade_drop_item_counts = np.unique(regular_shade_drops, return_counts=True)

    # Why does each one refer to "regular_shade_drop_item_counts"?
    money = 0
    money += get_returns(sg01_drop_items, regular_shade_drop_item_counts)
    money += get_returns(sg10_drop_items, regular_shade_drop_item_counts)
    money += get_returns(regular_shade_drop_items, regular_shade_drop_item_counts)
    return money


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

# Final calculation of funds. I'm only going to worry about plotting this number in the end for now, preferably
# in a scatter plot.
print(2600 + drops_before_shop() - 3000 + drops_after_shop())
