# De La Salle University–Dasmariñas
# S-ITCS214LA — Data Structures & Algorithms (Laboratory)

# Luis Anton P. Imperial
# BCS22

# Tuesday, November 28, 2023
# parkingLot

# Using the stack or queue, create a parking system using the principle of stack or queue (LIFO or FIFO). The parking lot has a maximum capacity and the cars added to the stack/list when parked. When a car leaves, it is remove from the stack/list

# Create your own method and avoid using python library or method

# Ex
#    In this simulation, cars will enter the parking lot and leae in a last-in-first-out order (stack)

import os
from tabulate import tabulate
from time import sleep

class Node:
    def __init__(self, initial):
        self.data = initial
        self.next = None

class Stack:
    def __init__(self, capacity_input):
        self.top = None
        self.capacity: int = capacity_input
    
    def isFull(self):
        elements_count = 0

        temp = self.top
        while temp:
            elements_count += 1
            temp = temp.next
        
        return elements_count >= self.capacity

    def push(self, input_received: chr):
        node_for_insertion = Node(input_received)

        if self.isFull() is True:
            print("Error! — Stack full. Overflow.")
        elif self.top is None:
            self.top = node_for_insertion
            self.top.next = None
        else:
            node_for_insertion.next = self.top
            self.top = node_for_insertion
    
    def pop(self):
        if self.top is None:
            print("Error! — No vehicles left.")
        elif self.top.next is None:
            print("Success! — “" + self.top.data + "” element removed from stack.")
            self.top = None
        else:
            node_for_removal = self.top

            print("Success! — “" + self.top.data + "” element removed from stack.")
            self.top = node_for_removal.next
            node_for_removal = None

    def display(self):
        if self.top is None:
            print("Error! — Stack is empty.")
        else:
            print("Elements of the stack are: ")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
            print("Top of the stack is: ", self.top.data)
    
    def showCapacity(self):
        return self.capacity
    
class terminalCarParkAesthetics:
    def convertToSidewaysEmoji(self, char: chr):
        if char == 'p':
            # 'p' means police car
            return '🚓'
        elif char == 'f':
            # 'f' means fire engine
            return '🚒'
        elif char == 'b':
            # 'b' means bus
            return '🚌'
        elif char == 'r':
            # 'r' means railway car
            return '🚃'
        elif char == 'x':
            # 'x' means taxi
            return '🚕'
        elif char == 'a':
            # 'a' means default automobile
            return '🚗'
        else:
            return '🚗'
        
    def convertToOncomingEmoji(self, char: chr):
        if char == 'p':
            # 'p' means police car
            return '🚔'
        elif char == 'f':
            # 'f' means fire engine
            # opted for 'person firefighter' emoji as 'oncoming' version for vehicle missing
            return '🧑‍🚒'
        elif char == 'b':
            # 'b' means bus
            return '🚍'
        elif char == 'r':
            # 'r' means railway car
            # no direct equivalent?
            return '🚆'
        elif char == 'x':
            # 'x' means taxi
            return '🚖'
        elif char == 'a':
            # 'a' means default automobile
            return '🚘'
        else:
            return '🚘'
    
    def showParkingLane(self, vehicle_parked, isFirst: bool):
        # Use these Unicode characters, for aesthetics:
        # ┏┓┗┛▓┫━┆┃┐┯┷

        vehicle_parked_emoji = self.convertToSidewaysEmoji(vehicle_parked)

        if isFirst == True:
            print("┏========"+ "="+                 "====┛")
            print("|| ▓  "+ vehicle_parked_emoji + "      ")
            print("┗========"+ "="+                 "====━")
        else:
            print("┏========"+ "="+                 "====┛")
            print("|| ▓  "+ vehicle_parked_emoji + "      ")
            print("┗========"+ "="+                 "====┓")

    def showParkingTollGate(self):
        toll_gate_empty = """
┏=============━
       ▓     
    🫷 🧑    
       ▓     
┗=============┓
        """

        print(toll_gate_empty)

    def showCarListAnimation(self, stack_input):
        vehicles_to_add = stack_input.top
        vehicles_added = 0

        if vehicles_to_add is None:
            print("No vehicles in the parking lot.")
            return vehicles_added

        self.showParkingTollGate()
        while vehicles_to_add:
            is_first_vehicle = True if vehicles_to_add.next == None else False
            self.showParkingLane(vehicles_to_add.data, is_first_vehicle)
            vehicles_added += 1
            vehicles_to_add = vehicles_to_add.next
        
        empty_parking_spots = stack_input.capacity - vehicles_added
        print("There are", empty_parking_spots, "empty parking spots.")

        return vehicles_added
    
    def showServiceRoadAnimation(self, vehicle_passing, passThru_stage: int, isAtBottom: bool, isGateExit: bool):
        vehicle_passing_oncomingEmoji = self.convertToOncomingEmoji(vehicle_passing)
        vehicle_passing_sidewaysEmoji = self.convertToSidewaysEmoji(vehicle_passing)

        serviceRoad_startStrip                = "━━━━━━━━┯┓"
        serviceRoad_empty_midStrip            = "        ┆┃"
        serviceRoad_empty_endStrip            = "┆       ┆┃"
        serviceRoad_atBottom_endStrip         = "━━━━━━━━┷┛"
        serviceRoad_oncoming_midStrip  = f"   {vehicle_passing_oncomingEmoji}   ┆┃"
        serviceRoad_oncoming_endStrip  = f"┆  {vehicle_passing_oncomingEmoji}   ┆┃"
        serviceRoad_sideways1_midStrip = f"   {vehicle_passing_sidewaysEmoji}   ┆┃"
        serviceRoad_sideways2_midStrip = f" {vehicle_passing_sidewaysEmoji}     ┆┃"
        serviceRoad_sideways3_midStrip = f"{vehicle_passing_sidewaysEmoji}      ┆┃"
        
        if isGateExit is True:
            if vehicle_passing is None:
                return (serviceRoad_startStrip,
                        serviceRoad_empty_midStrip,
                        serviceRoad_empty_midStrip,
                        serviceRoad_empty_midStrip,
                        serviceRoad_empty_endStrip)
            else:
                if passThru_stage == 1:
                    return(serviceRoad_startStrip,
                           serviceRoad_empty_midStrip,
                           serviceRoad_empty_midStrip,
                           serviceRoad_empty_midStrip,
                           serviceRoad_oncoming_endStrip)
                elif passThru_stage == 2:
                    return(serviceRoad_startStrip,
                           serviceRoad_empty_midStrip,
                           serviceRoad_empty_midStrip,
                           serviceRoad_oncoming_midStrip,
                           serviceRoad_empty_endStrip)
                elif passThru_stage == 3:
                    return(serviceRoad_startStrip,
                           serviceRoad_empty_midStrip,
                           serviceRoad_oncoming_midStrip, serviceRoad_empty_midStrip,
                           serviceRoad_empty_endStrip)
                elif passThru_stage == 4:
                    return(serviceRoad_startStrip,
                           serviceRoad_sideways1_midStrip,
                           serviceRoad_empty_midStrip,
                           serviceRoad_empty_midStrip,
                           serviceRoad_empty_endStrip)
                elif passThru_stage == 5:
                    return(serviceRoad_startStrip,
                           serviceRoad_sideways2_midStrip,
                           serviceRoad_empty_midStrip,
                           serviceRoad_empty_midStrip,
                           serviceRoad_empty_endStrip)
        elif isAtBottom is True:
            if vehicle_passing is None:
                return(serviceRoad_empty_endStrip,
                       serviceRoad_empty_midStrip,
                       serviceRoad_atBottom_endStrip)
            else:
                if passThru_stage == 1:
                    return(serviceRoad_oncoming_endStrip,
                           serviceRoad_empty_midStrip,
                           serviceRoad_atBottom_endStrip)
                elif passThru_stage == 2:
                    return(serviceRoad_empty_endStrip,
                           serviceRoad_oncoming_midStrip,
                           serviceRoad_atBottom_endStrip)
                elif passThru_stage == 3:
                    return(serviceRoad_empty_endStrip,
                           serviceRoad_sideways1_midStrip,
                           serviceRoad_atBottom_endStrip)
                elif passThru_stage == 4:
                    return(serviceRoad_empty_endStrip,
                           serviceRoad_sideways2_midStrip,
                           serviceRoad_atBottom_endStrip)
                elif passThru_stage == 5:
                    return(serviceRoad_empty_endStrip,
                           serviceRoad_sideways3_midStrip,
                           serviceRoad_atBottom_endStrip)
        else:
            if vehicle_passing is None:
                return(serviceRoad_empty_endStrip,
                       serviceRoad_empty_midStrip,
                       serviceRoad_empty_endStrip)
            else:
                if passThru_stage == 1:
                    return(serviceRoad_oncoming_endStrip,
                           serviceRoad_empty_midStrip,
                           serviceRoad_empty_endStrip)
                elif 2 <= passThru_stage <= 4:
                    return(serviceRoad_empty_endStrip,
                           serviceRoad_oncoming_midStrip,
                           serviceRoad_empty_endStrip)
                elif passThru_stage == 5:
                    return(serviceRoad_empty_endStrip,
                           serviceRoad_empty_midStrip,
                           serviceRoad_oncoming_endStrip)
    
    def printCarparkRows(self, parking_lot: []):
        column_names = ["Parking", "Svc Rd"]
        print(tabulate(parking_lot, headers=column_names))

    def showEntranceAnimation(self, stack_input, vehicles_added: int, new_vehicle: str):
        toll_gates: int = 1
        stages: int = 5

        stages_complete: int = 0

        while stages_complete < stages:
            stages_complete += 1
            lanes_printed: int = 0
            toll_gates_printed: int = 0

            while toll_gates_printed < toll_gates:
                for lane in self.showServiceRoadAnimation(new_vehicle, stages_complete, False, True):
                    print(lane, end=os.linesep)
                toll_gates_printed += 1

            while lanes_printed < (vehicles_added - 1):
                for lane in self.showServiceRoadAnimation(new_vehicle, stages_complete, False, False):
                    print(lane, end=os.linesep)
                lanes_printed += 1
            
            # For the bottom lane
            for lane in self.showServiceRoadAnimation(new_vehicle, stages_complete, False, True):
                print(lane, end=os.linesep)
            lanes_printed += 1

            print("")
            print("Entering bus into system... — stage", stages_complete, "done.")
            print("")
            sleep(3)


    @staticmethod
    def showEntranceInfo():
        print("Which vehicle do you wish to enter into the parking lot?")
        print("")

        print("• [p] 🚓 Police Car")
        print("• [f] 🚒 Fire Engine")
        print("• [b] 🚌 Bus")
        print("• [r] 🚃 Railway Car")
        print("• [x] 🚕 Taxi")
        print("• [a] 🚗 Automobile")
        print("")

        vehicle_for_insertion = input("Enter letter code here: ")[0]
        return vehicle_for_insertion

    @staticmethod
    def showMenu():
        print("")
        print("Welcome to Filten Terminal Parking Lot!")
        print("")

        print("©️ 2023 Luis Anton P• Imperial.")
        print("")

        print("What do you want to do today?")
        print("1 — Enter new vehicle into parking lot")
        print("2 — Remove last vehicle from parking lot")
        print("3 — Show contents of parking lot")
        print("4 — Exit program")
        print("")

        numerical_input = int(input("Type your option here: "))
        return numerical_input
   

def main():
    program_stack_capacity = 5
    program_stack = Stack(program_stack_capacity)

    while True:
        user_input = terminalCarParkAesthetics().showMenu()
        if user_input == 1:
            new_vehicle = terminalCarParkAesthetics().showEntranceInfo()
            terminalCarParkAesthetics().showEntranceAnimation(program_stack, program_stack.capacity, new_vehicle)
            
            program_stack.push(new_vehicle)
        elif user_input == 2:
            # terminalCarParkAesthetics().showExitInfo(program_stack)
            # terminalCarParkAesthetics().showExitAnimation(program_stack)
            program_stack.pop()
        elif user_input == 3:
            parking_lot_now = [terminalCarParkAesthetics().showCarListAnimation(program_stack),
             terminalCarParkAesthetics().showServiceRoadAnimation(None, 0, False, False)]
            
            terminalCarParkAesthetics().printCarparkRows(parking_lot_now)
        elif user_input == 4:
            print("")
            print("Thank you for using the Filten Terminal Parking Lot!")
            print("Have a great day!")
            break
        else:
            print("")
            print("Error! — Kindly select only among the available options.")


if __name__ == "__main__":
    main()