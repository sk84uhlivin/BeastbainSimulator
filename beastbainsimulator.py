#!/usr/bin/env python3

import numpy as np

# ## Simulation


def regular_shade_drop(size, trails=1, preshop=False):
    """
    Generates random drops for regular shade

    Parameters
    ----------
    size: int
        Number of regular shade kills in the trail
    trails: int
        Number of trails to simulate
    preshop: bool
        If shade is one of the first 4.
    """

    return np.random.choice(
        ["None", "Medicinal Herb2" if preshop else "Medicinal Herb", "Old Schoolbook", "Dented Metal Bat"],
        size=[trails, size],
        p=[0.74, 0.15, 0.1, 0.01])


def regular_shade_2_drop(size, trails=1):
    return np.random.choice(["None", "Medicinal Herb", "Used Coloring Book", "Rusty Kitchen Knife", "Broken Saw"],
                            size=[trails, size], p=[0.72, 0.15, 0.1, 0.02, 0.01])


def large_shade_drop(size, trails=1):
    return np.random.choice(["None", "Defense Drop", "Thick Dictionary", "Stopped Clock", "Leather Boots"],
                            size=[trails, size], p=[0.745, 0.15, 0.08, 0.02, 0.005])


def large_shade_2_drop(size, trails=1):
    return np.random.choice(["None", "Strength Drop", "Closed Book", "Broken Wristwatch", "Leather Boots"],
                            size=[trails, size], p=[0.745, 0.15, 0.08, 0.02, 0.005])


def boar_drop(size, trails=1):
    return np.random.choice(["Boar Meat", "Boar Hide", "Boar Liver"], size=[trails, size], p=[0.5, 0.3, 0.2])


def sg01_drop(size, trails=1):
    return np.random.choice(['Dented Metal Board', "Broken Arm", "Broken Antenna"], size=[trails, size],
                            p=[0.5, 0.3, 0.2])


def sg10_drop(size, trails=1):
    return np.random.choice(["Stripped Bolt", "Broken Antenna", "Broken Motor", "Titanium Alloy"], size=[trails, size],
                            p=[0.4, 0.3, 0.2, 0.1])


def box_drop(size, trails=1):
    return np.random.choice(['None', "Pyrite", "Amber"], size=[trails, size],
                            p=[0.94, 0.05, 0.01])


conversion_dict = {"None": 0,
                   'Medicinal Herb': 10,
                   'Medicinal Herb2': 100,
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
                   'Boar Liver': 2500,
                   'Amber': 3000
                   }


def get_returns(drops):
    """
    Calculates the values for drops, by converting the names to the values of the conversion dict and then summing over all drops in a trail.

    Parameters
    ----------
    drops: np.ndarray
        2D array with the first axis being the trails and the second one being the drops in the trail
    """
    total_money = np.vectorize(conversion_dict.get)(drops).sum(axis=1)
    return total_money


# ### Simulate drops before the shop


def drops_before_shop(trails):
    regular_shade_drops_pre = regular_shade_drop(size=4, trails=trails, preshop=True)
    regular_shade_drops = regular_shade_drop(size=8, trails=trails)
    regular_shade_2_drops = regular_shade_2_drop(size=4, trails=trails)
    large_shade_drops = large_shade_drop(size=10, trails=trails)
    large_shade_2_drops = large_shade_drop(size=2, trails=trails)
    boar_drops = boar_drop(size=1, trails=trails)

    money = get_returns(regular_shade_drops_pre)
    money += get_returns(regular_shade_drops)
    money += get_returns(regular_shade_2_drops)
    money += get_returns(large_shade_drops)
    money += get_returns(large_shade_2_drops)
    money += get_returns(boar_drops)
    money += 20  # for the LURE
    return money


# ### After Shop


def drops_after_shop(trails):
    sg01_drops = sg01_drop(size=56, trails=trails)
    sg10_drops = sg10_drop(size=17, trails=trails)
    regular_shade_drops = regular_shade_drop(size=4, trails=trails)
    box_drops = box_drop(size=6, trails=trails)

    money = get_returns(sg01_drops)
    money += get_returns(sg10_drops)
    money += get_returns(regular_shade_drops)
    money += get_returns(box_drops)
    # Dented Metal Board from boxes
    money += 1600
    return money


sims = int(input("How many simulations? "))
print(f"Processing {sims} simulations...")
print()
results_before_shop = drops_before_shop(sims)
results_after_shop = drops_after_shop(sims)

# ### Full simulation with before/after shop + funds

results_all = results_before_shop + results_after_shop - 400

good_runs = [result for result in results_all if result >= 16800]
print(f"{len(good_runs)} out of {sims}, or {round((len(good_runs) / sims * 100), 3)}% successful Beastbain attempts.")
