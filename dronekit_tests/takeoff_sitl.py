from dronekit import connect, VehicleMode
import dronekit_sitl
from dronekit_sitl import SITL
import time

TARGET_ALTITUDE = 20 # Meters

# Start simulated drone
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

# Connect to the Vehicle (in this case a simulator running the same computer)
vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)


def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print "Basic pre-arm checks"
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print " Waiting for vehicle to initialise..."
        time.sleep(1)

    print "Arming motors"
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print " Waiting for arming..."
        time.sleep(1)

    print "Taking off!"
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt

        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print "Reached target altitude"
            break
        time.sleep(1)


def land():
    print "Landing..."
    vehicle.mode = VehicleMode("LAND")


def main():
    arm_and_takeoff(5)
    land()


if __name__ == "__main__":
    main()