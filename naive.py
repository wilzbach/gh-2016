from orders import load, unload, deliver, wait

def schedule(state):
    commands = []
    state["drone_busy_times"] = [-1 for _ in nr_drones]
    current_order = 0
    state["current_order"] = 0
    for turn in range(nr_turns)
        for drone, busy_till in enumerate(drone_busy_time for drone_busy_time in state["drone_busy_times"] if drone_busy_time < turn):
            # select product to deliver
            offer = choose_product_naive(state)

            # create command
            command = deliver(drone, offer[0], offer[1], offer[2])
            commands.append(command)

            # search closest warehouse with chosen product
            # compute fly time
            # update state
            state["drone_busy_times"] += flight_time
            state["orders"][offer[0]]["distances"][warehouseid] 
            





def choose_product_naive(state):
    current_order = state["current_order"]
    state["current_order"] += 1

    product_to_deliver = state["orders"][current_order]["type"][0]
    state["orders"][current_order]["type"] = state["orders"][current_order]["type"][1:]   
    return (current_order, product_to_deliver, 1)
