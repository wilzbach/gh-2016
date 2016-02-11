def load(drone_id, warehouse_id, product_id, item_count):
    return (drone_id, 'L', warehouse_id, product_id, item_count)

def unload(drone_id, warehouse_id, product_id, item_count):
    return (drone_id, 'U', warehouse_id, product_id, item_count)

def deliver(drone_id, order_id, product_id, item_count):
    return (drone_id, 'D', order_id, product_id, item_count)

def wait(drone_id, turn_count):
    return (drone_id, 'W', turn_count)
