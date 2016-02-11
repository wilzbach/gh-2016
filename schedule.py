from orders import load, unload, deliver, wait

def schedule(state):
    commands = []
    for turn in range(state.nr_turns):
        for drone in state.drones:
            command = drone.new_instructions(turn)
            if command is not None:
                commands.append(command)
            elif not drone.busy(turn):
                # select product to deliver
                offer = state.next_offer()
                offer["warehouse"] = state.closest_warehouse(drone, offer)
                command = drone.process_offer(turn, offer)
                commands.append(command)
    return commands
