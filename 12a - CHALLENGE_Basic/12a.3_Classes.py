### 1-Setting Up Our Robot
# Define the DriveBot class here!
class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0
  
robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

### 2- Adding Robot Logic
class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0
    
    # Add the methods here!
    def control_bot(self, new_speed, new_direction):
      self.motor_speed = new_speed
      self.direction = new_direction
 
    def adjust_sensor(self, new_sensor_range):
      self.sensor_range = new_sensor_range

robot_1 = DriveBot()
# Use the methods here!
robot_1.motor_speed = 10
robot_1.direction = 180
robot_1.sensor_range = 20
print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

### 3- Enhanced Constructor

class DriveBot:
    # Update this constructor!
    def __init__(self,motor_speed =0,direction = 180,sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

# Create robot_2 here!
robot_2 = DriveBot(35, 75,25)

print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

### 4- Controlling Them All
class DriveBot:
  # Create the class variables!
    all_disabled = False
    latitude = -999999
    longitude = -999999

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

# Change the latitude, longitude, and all_disabled values for all three robots using only three lines of code!

DriveBot.longitude = 50.0
DriveBot.latitude = -50.0
DriveBot.all_disabled = True

print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)
#We placed the class variables at the top of the class outside of the constructor. These variables can be accessed within the scope of the entire class. 
#This means that the class variables contained within every object from the DriveBot class will change if we modify the class variable directly.


### 5- Identifying Robots
class DriveBot:
  # Create a counter to keep track of how many robots were created
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        # Assign an `id` to the robot when it is constructed by incrementing the counter and assigning the value to `id`
        DriveBot.robot_count +=1
        self.id = DriveBot.robot_count
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)
print(robot_1.id)
print(robot_2.id)
print(robot_3.id)

#The final modifications to this class can be seen at the top of the class and in the constructor. We use a class variable to keep track of the total number of robots. 
#This information is shared across all robot objects we create from the class. Every time a robot object is created, the constructor is called and the count is incremented. 


