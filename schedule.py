from orders import load, unload, deliver, wait


def schedule(state):
    commands = []
    print(state.nr_turns)
    for turn in range(state.nr_turns):
        for drone in state.drones:
            if drone.has_new_instructions(turn):
                commands.append(drone.new_instructions(turn))
            elif not drone.busy(turn):
                # select product to deliver
                offer = state.next_offer()
                offer["warehouse"] = state.closest_warehouse(drone, offer)
                command = drone.process(turn, offer)
                commands.append(command)
        if turn % 1000 == 0:
            print(turn)
    return commands
