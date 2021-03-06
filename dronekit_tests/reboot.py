import time
import argparse
from utils import dronekit_utils

### Test script for auto reboot and reconnection ### 

#Set up option parsing to get connection string
parser = argparse.ArgumentParser(description='Test reboot')
parser.add_argument('--sitl',
                   help="Vehicle connection target string. If specified, SITL will be used.")
args = vars(parser.parse_args())

def main():

    # Connect to vehicle
    vehicle = dronekit_utils.connect_vehicle_args(args)

    # Reboot
    dronekit_utils.reboot(vehicle)
    vehicle.close() 

if __name__ == "__main__":
    main()
