class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_position_speed_map = list(zip(position, speed))
        car_position_speed_map = sorted(car_position_speed_map, reverse=True)
        carFleetStack = []

        for car_position, car_speed in car_position_speed_map:
            distance = (target - car_position)
            speed = car_speed
            # Time it takes to get to the destination
            time = distance / speed
            if len(carFleetStack) == 0 or time > carFleetStack[-1]:
                carFleetStack.append(time)

        print(len(carFleetStack))
        totalCarFleetOutput = len(carFleetStack)
        return totalCarFleetOutput