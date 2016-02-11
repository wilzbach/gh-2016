#!/usr/bin/env python
# encoding: utf-8


def parse(inFileName):

    with open(inFileName, "r") as inFile:

        header = inFile.readline()
        rows, columns, nr_drones, nr_turns, max_paylod = list(map(int, header.strip().split(" ")))

        # read product types
        nr_products = int(inFile.readline())
        products = list(map(int, inFile.readline().strip().split(" ")))
        assert len(products) == nr_products

        # read warehouses
        nr_warehouses = int(inFile.readline())
        warehouses = []
        for i in range(nr_warehouses):
            pos = list(map(int, inFile.readline().strip().split(" ")))
            product_types = list(map(int, inFile.readline().strip().split(" ")))
            assert len(product_types) == nr_products
            warehouses.append({"pos": pos, "type": product_types})

        assert len(warehouses) == nr_warehouses

        # read orders
        nr_orders = int(inFile.readline())
        orders = []
        lines = inFile.readlines()
        for pos, nr_items, items in zip(lines[::3], lines[1::3], lines[2::3]):
            items = list(map(int, items.strip().split(" ")))
            assert int(nr_items) == len(items)
            orders.append({"pos": pos, "items": items})

        assert len(orders) == nr_orders

        return {
            "rows": rows,
            "columns": columns,
            "nr_drones": nr_drones,
            "nr_turns": nr_turns,
            "max_paylod": max_paylod,
            "products": products,
            "warehouses": warehouses,
            "orders": orders
        }
