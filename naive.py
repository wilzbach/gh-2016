from orders import load, unload, deliver, wait

def schedule(state):
    commands = []
    for turn in range(nr_turns):
        for drone in (drone for drone in state.drones if not drone.busy(turn)):
            # select product to deliver
            offer = state.next_offer()
            closest_warehouse = state.closest_warehouse(drone, offer)

            # get to warehouse if not there

            # load items

            # create command
            command = deliver(state, drone, offer)
            commands.append(command)

def choose_product_naive(state):
    if "current_order" not in state:
        state["current_order"] = 0
    current_order = state["current_order"]
    state["current_order"] += 1

    product_to_deliver = state["orders"][current_order]["type"][0]
    state["orders"][current_order]["type"] = state["orders"][current_order]["type"][1:]
    return ("order": current_order, "product": product_to_deliver, "count": 1)
