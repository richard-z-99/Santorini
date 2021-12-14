def run(self):
    worker_name = input("Select a worker to move\n>")
    if(worker_name == 'A'): 
        worker = self.worker1

    elif(worker_name == 'B'):
        worker = self.worker2

    else:
        print("Invalid worker name input")
        return

    #TODO: Error checking on move_direction, actually moving worker
    move_dir = input("Select a direction to move {}\n".format(directions.keys()))

    if(not directions.has_key(move_dir)):
        print("Invalid move input")
        return

    else:
        pass


    #TODO: Error checking on build_direction, actually building
    build_dir = input("Select a direction to build {}}\n".format(directions.keys()))