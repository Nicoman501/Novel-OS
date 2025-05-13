#!/usr/bin/python3

import rospy
import atexit
import matplotlib.pyplot as plt
from std_msgs.msg import Float64
from geometry_msgs.msg import Pose, Twist, Point
from gazebo_msgs.msg import ModelStates, ModelState
import numpy as np
import math
import time

time.sleep(5) 
Actual_pose_x = []
Actual_pose_y = []
Actual_pose_z = []
Actual_orientation_x = []
Actual_orientation_y = []
Actual_orientation_z = []
Actual_Speed_x = []
Actual_Speed_y = []
Actual_Speed_z = []
Actual_ang_speed_x = []
Actual_ang_speed_y = []
Actual_ang_speed_z = []
Noisy_pose_x = []
Noisy_pose_y = []
Noisy_pose_z = []
Noisy_orientation_x = []
Noisy_orientation_y = []
Noisy_orientation_z = []
Noisy_Speed_x = []
Noisy_Speed_y = []
Noisy_Speed_z = []
Noisy_ang_speed_x = []
Noisy_ang_speed_y = []
Noisy_ang_speed_z = []


predicted_pose_x = []
predicted_pose_y = []
predicted_pose_z = []
predicted_orientation_x = []
predicted_orientation_y = []
predicted_orientation_z = []
predicted_Speed_x = []
predicted_Speed_y = []
predicted_Speed_z = []
predicted_ang_speed_x = []
predicted_ang_speed_y = []
predicted_ang_speed_z = []
filtered_pose_x = []
filtered_pose_y = []
filtered_pose_z = []
filtered_orientation_x = []
filtered_orientation_y = []
filtered_orientation_z = []
filtered_Speed_x = []
filtered_Speed_y = []
filtered_Speed_z = []
filtered_ang_speed_x = []
filtered_ang_speed_y = []
filtered_ang_speed_z = []

std_dev = 0.1  # for mpu 6050

# Kalman filter variables
state = np.zeros((6, 1))  # Current state [x, y, z, roll, pitch, yaw]
covariance = np.eye(6)  # Error covariance

# Model parameters
dt = 0.01  # Time step

# Process and measurement noise
Q = np.eye(6) * 0.01  # Process noise covariance
R = np.eye(6) * 0.1  # Measurement noise covariance

# Initial state estimate and error covariance
state_estimate = np.zeros((6, 1))
covariance_estimate = np.eye(6)
# Initialize ROS Node
rospy.init_node('Localization_Module_Team_3')  # Identify ROS Node
pub = rospy.Publisher('/Localization', ModelState, queue_size=1)
rospy.Rate(30)  # rate of publishing msg 10hz
def Gasussian_noise(mu, sigma):
    return np.random.normal(mu, sigma)
# Kalman filter algorithm

def plot_graphs():
    # Plot the ground truth
    # fig1 = plt.figure()
    # plt.plot(Noisy_pose_x,label='Noisy X')
    # plt.plot(predicted_pose_x,label='Predicted X')
    # plt.plot(filtered_pose_x,label='Filtered X')
    # plt.plot(Actual_pose_x,label='Actual X')
    # plt.title('x_Position Results')


    # plt.plot(Noisy_pose_y,label='Noisy Y')
    # plt.plot(predicted_pose_y,label='Predicted Y')
    # plt.plot(filtered_pose_y,label='Filtered Y')
    # plt.plot(Actual_pose_y,label='Actual Y')
    # plt.title('y_Position Results')
    # plt.savefig('y_Position Results.png')

    # fig3 = plt.figure()
    # plt.plot(Noisy_orientation_x,label='Noisy Orientation X')
    # plt.plot(predicted_orientation_x,label='Predicted Orientation X')
    # plt.plot(filtered_orientation_x,label='Filtered Orientation X')
    # plt.plot(Actual_orientation_x,label='Actual Orientation X')
    # plt.title('Orientation X Results')
    # plt.savefig('Orientation X Results.png')
    fig5 = plt.figure()
    plt.plot(Noisy_Speed_y,label='Noisy Speed Y')
    plt.plot(predicted_Speed_y,label='Predicted Speed Y')
    plt.plot(filtered_Speed_y,label='Filtered Speed Y')
    plt.plot(Actual_Speed_y,label='Actual Speed Y')
    plt.title('Speed Y Results')
    plt.legend()
    plt.show()
    # fig4 = plt.figure()
    # plt.plot(Noisy_orientation_y,label='Noisy Orientation Y')
    # plt.plot(predicted_orientation_y,label='Predicted Orientation Y')
    # plt.plot(filtered_orientation_y,label='Filtered Orientation Y')
    # plt.plot(Actual_orientation_y,label='Actual Orientation Y')
    # plt.title('Orientation Y Results')
    # plt.savefig('Orientation Y Results.png')
    # plt.savefig('/home/figure.png')
    # plt.savefig('/figure.png')
    # plt.xlabel('sample')
    # plt.ylabel('states')
    
    # fig2 = plt.figure()



    # plt.show()
    # hold till i press any key
    plt.waitforbuttonpress()

    plt.plot(Actual_pose_y,label='Actual Y')
    plt.plot(Noisy_pose_y,label='Noisy Y')



    # plt.plot(Actual_pose_z,label='Actual Z')
    plt.plot(Actual_orientation_x,label='Actual Orientation X')
    plt.plot(Actual_orientation_y,label='Actual Orientation Y')
    # plt.plot(Actual_orientation_z,label='Actual Orientation Z')
    plt.plot(Actual_Speed_x,label='Actual Speed X')
    plt.plot(Actual_Speed_y,label='Actual Speed Y')
    # plt.plot(Actual_Speed_z,label='Actual Speed Z')
    plt.plot(Actual_ang_speed_x,label='Actual Angular Speed X')
    plt.plot(Actual_ang_speed_y,label='Actual Angular Speed Y')
    # plt.plot(Actual_ang_speed_z,label='Actual Angular Speed Z')


    
    # plt.plot(Noisy_pose_z,label='Noisy Z')
    plt.plot(Noisy_orientation_x,label='Noisy Orientation X')
    plt.plot(Noisy_orientation_y,label='Noisy Orientation Y')
    # plt.plot(Noisy_orientation_z,label='Noisy Orientation Z')
    plt.plot(Noisy_Speed_x,label='Noisy Speed X')
    plt.plot(Noisy_Speed_y,label='Noisy Speed Y')
    # plt.plot(Noisy_Speed_z,label='Noisy Speed Z')
    plt.plot(Noisy_ang_speed_x,label='Noisy Angular Speed X')
    plt.plot(Noisy_ang_speed_y,label='Noisy Angular Speed Y')
    # plt.plot(Noisy_ang_speed_z,label='Noisy Angular Speed Z')

    plt.plot(predicted_pose_y,label='Predicted Y')
    # plt.plot(predicted_pose_z,label='Predicted Z')
    plt.plot(predicted_orientation_x,label='Predicted Orientation X')
    plt.plot(predicted_orientation_y,label='Predicted Orientation Y')
    # plt.plot(predicted_orientation_z,label='Predicted Orientation Z')
    plt.plot(predicted_Speed_x,label='Predicted Speed X')
    plt.plot(predicted_Speed_y,label='Predicted Speed Y')
    # plt.plot(predicted_Speed_z,label='Predicted Speed Z')
    plt.plot(predicted_ang_speed_x,label='Predicted Angular Speed X')
    plt.plot(predicted_ang_speed_y,label='Predicted Angular Speed Y')
    # plt.plot(predicted_ang_speed_z,label='Predicted Angular Speed Z')
    
    plt.plot(filtered_pose_y,label='Filtered Y')
    plt.plot(filtered_pose_z,label='Filtered Z')
    plt.plot(filtered_orientation_x,label='Filtered Orientation X')
    plt.plot(filtered_orientation_y,label='Filtered Orientation Y')
    plt.plot(filtered_orientation_z,label='Filtered Orientation Z')
    plt.plot(filtered_Speed_x,label='Filtered Speed X')
    plt.plot(filtered_Speed_y,label='Filtered Speed Y')
    # plt.plot(filtered_Speed_z,label='Filtered Speed Z')
    plt.plot(filtered_ang_speed_x,label='Filtered Angular Speed X')
    plt.plot(filtered_ang_speed_y,label='Filtered Angular Speed Y')
    # plt.plot(filtered_ang_speed_z,label='Filtered Angular Speed Z')


    
    


def model_states_callback(msg):
    # Callback function for the model states
    global Actual_position, Actual_Speed, Noisy_position, Noisy_orientation, Noisy_Speed, Filtered_position, Filtered_Speed
    global vehicle_index, Actual_pose_x, Actual_pose_y, Actual_pose_z, Actual_orientation_x, Actual_orientation_y, Actual_orientation_z, Actual_Speed_x, Actual_Speed_y, Actual_Speed_z, Actual_ang_speed_x, Actual_ang_speed_y, Actual_ang_speed_z
    global Noisy_pose_x, Noisy_pose_y, Noisy_pose_z, Noisy_orientation_x, Noisy_orientation_y, Noisy_orientation_z, Noisy_Speed_x, Noisy_Speed_y, Noisy_Speed_z, Noisy_ang_speed_x, Noisy_ang_speed_y, Noisy_ang_speed_z
    global predicted_pose_x, predicted_pose_y, predicted_pose_z, predicted_orientation_x, predicted_orientation_y, predicted_orientation_z, predicted_Speed_x, predicted_Speed_y, predicted_Speed_z, predicted_ang_speed_x, predicted_ang_speed_y, predicted_ang_speed_z
    global filtered_pose_x, filtered_pose_y, filtered_pose_z, filtered_orientation_x, filtered_orientation_y, filtered_orientation_z, filtered_Speed_x, filtered_Speed_y, filtered_Speed_z, filtered_ang_speed_x, filtered_ang_speed_y, filtered_ang_speed_z
    

    print('Call Back Function')
    vehicle_index=2 
    # try:
    #   vehicle_index = state.name.index('ackermann_vehicle')
    # except:
    #   pass
    
    Actual_position = msg.pose[vehicle_index].position
    Actual_orientation = msg.pose[vehicle_index].orientation
    Actual_Speed = msg.twist[vehicle_index].linear
    Actual_ang_speed = msg.twist[vehicle_index].angular

    Actual_pose_x.append(Actual_position.x)
    Actual_pose_y.append(Actual_position.y)
    Actual_pose_z.append(Actual_position.z)
    Actual_orientation_x.append(Actual_orientation.x)
    Actual_orientation_y.append(Actual_orientation.y)
    Actual_orientation_z.append(Actual_orientation.z)
    Actual_Speed_x.append(Actual_Speed.x)
    Actual_Speed_y.append(Actual_Speed.y)
    Actual_Speed_z.append(Actual_Speed.z)
    Actual_ang_speed_x.append(Actual_ang_speed.x)
    Actual_ang_speed_y.append(Actual_ang_speed.y)
    Actual_ang_speed_z.append(Actual_ang_speed.z)


    Noise=Gasussian_noise(0.1, std_dev)
    

    # Add noise to the position and orientation
    
    Noisy_pose = Pose()
    Noisy_Speed = Twist()
    Noisy_pose.position.x = Actual_position.x + Noise
    Noisy_pose.position.y = Actual_position.y + Noise
    Noisy_pose.position.z = Actual_position.z + Noise
    Noisy_pose.orientation.x = Actual_orientation.x + Noise
    Noisy_pose.orientation.y = Actual_orientation.y + Noise
    Noisy_pose.orientation.z = Actual_orientation.z + Noise
    Noisy_Speed.linear.x = Actual_Speed.x + Noise
    Noisy_Speed.linear.y = Actual_Speed.y + Noise
    Noisy_Speed.linear.z = Actual_Speed.z + Noise
    Noisy_Speed.angular.x = Actual_ang_speed.x + Noise
    Noisy_Speed.angular.y = Actual_ang_speed.y + Noise
    Noisy_Speed.angular.z = Actual_ang_speed.z + Noise

    Noisy_pose_x.append(Noisy_pose.position.x)
    Noisy_pose_y.append(Noisy_pose.position.y)
    Noisy_pose_z.append(Noisy_pose.position.z)
    Noisy_orientation_x.append(Noisy_pose.orientation.x)
    Noisy_orientation_y.append(Noisy_pose.orientation.y)
    Noisy_orientation_z.append(Noisy_pose.orientation.z)
    Noisy_Speed_x.append(Noisy_Speed.linear.x)
    Noisy_Speed_y.append(Noisy_Speed.linear.y)
    Noisy_Speed_z.append(Noisy_Speed.linear.z)
    Noisy_ang_speed_x.append(Noisy_Speed.angular.x)
    Noisy_ang_speed_y.append(Noisy_Speed.angular.y)
    Noisy_ang_speed_z.append(Noisy_Speed.angular.z)



    # Noisy_position = Actual_position + Noise
    # Noisy_orientation = Actual_orientation + Noise
    # Noisy_Speed = Actual_Speed + Noise
    # Noisy_angular = Actual_ang_speed + Noise 
    # Get the position and orientation from the first model in the message

    # Convert position and orientation to the measurement vector
    measurement_pose = np.array([[Noisy_pose.position.x], [Noisy_pose.position.y], [Noisy_pose.position.z],
                                 [Noisy_pose.orientation.x], [Noisy_pose.orientation.y], [Noisy_pose.orientation.z]])
    measurement_twist = np.array([[Noisy_Speed.linear.x], [Noisy_Speed.linear.y], [Noisy_Speed.linear.z],
                                  [Noisy_Speed.angular.x], [Noisy_Speed.angular.y], [Noisy_Speed.angular.z]])
    # Perform Kalman filter update
    # print('Measured Values: \n',measurement_pose)
    filtered_Pose,predicted_pose = kalman_filter(measurement_pose)
    # print('Filtered Values: \n',filtered_Pose)
    filtered_Twist,predicted_twist = kalman_filter(measurement_twist)

    predicted_pose_x.append(predicted_pose[0])
    predicted_pose_y.append(predicted_pose[1])
    predicted_pose_z.append(predicted_pose[2])
    predicted_orientation_x.append(predicted_pose[3])
    predicted_orientation_y.append(predicted_pose[4])
    predicted_orientation_z.append(predicted_pose[5])
    predicted_Speed_x.append(predicted_twist[0])
    predicted_Speed_y.append(predicted_twist[1])
    predicted_Speed_z.append(predicted_twist[2])
    predicted_ang_speed_x.append(predicted_twist[3])
    predicted_ang_speed_y.append(predicted_twist[4])
    predicted_ang_speed_z.append(predicted_twist[5])


    # Print filtered state
    # rospy.loginfo('Actual position: ', Actual_position, 'Noisy position: ',
    #       Noisy_position, 'Filtered position: ', filtered_Pose)
    # rospy.loginfo('Actual orientation: ', Actual_orientation, 'Noisy orientation: ',
    #       Noisy_orientation, 'Filtered orientation: ', filtered_Pose)
    # rospy.loginfo('Actual Speed: ', Actual_Speed, 'Noisy Speed: ',
    #       Noisy_Speed, 'Filtered Speed: ', filtered_Twist)
    # rospy.loginfo('Actual angular: ', Actual_ang_speed, 'Noisy angular: ',
    #       Noisy_angular, 'Filtered angular: ', filtered_Twist)
    # rospy.loginfo('Actual position: ' + str(Actual_position) + ' Noisy position: ' + str(Noisy_position) + ' Filtered position: ' + str(filtered_Pose))
    # rospy.loginfo('Actual orientation: ' + str(Actual_orientation) + ' Noisy orientation: ' + str(Noisy_orientation) + ' Filtered orientation: ' + str(filtered_Pose))
    # rospy.loginfo('Actual Speed: ' + str(Actual_Speed) + ' Noisy Speed: ' + str(Noisy_Speed) + ' Filtered Speed: ' + str(filtered_Twist))
    # rospy.loginfo('Actual angular: ' + str(Actual_ang_speed) + ' Noisy angular: ' + str(Noisy_angular) + ' Filtered angular: ' + str(filtered_Twist))
    
    # create filtered pose() and twist() message
    Filtered_position = Pose()
    Filtered_position.position.x = filtered_Pose[0]
    Filtered_position.position.y = filtered_Pose[1]
    Filtered_position.position.z = filtered_Pose[2]
    Filtered_position.orientation.x = filtered_Pose[3]
    Filtered_position.orientation.y = filtered_Pose[4]
    Filtered_position.orientation.z = filtered_Pose[5]
    Filtered_Speed = Twist()
    Filtered_Speed.linear.x = filtered_Twist[0]
    Filtered_Speed.linear.y = filtered_Twist[1]
    Filtered_Speed.linear.z = filtered_Twist[2]
    Filtered_Speed.angular.x = filtered_Twist[3]
    Filtered_Speed.angular.y = filtered_Twist[4]
    Filtered_Speed.angular.z = filtered_Twist[5]
    Filtered_States = ModelState()
    # Filtered_States.name = msg.name
    Filtered_States.model_name = 'ackermann_vehicle'
    Filtered_States.reference_frame = 'world'
    Filtered_States.pose = Filtered_position
    Filtered_States.twist = Filtered_Speed
    
    filtered_pose_x.append(Filtered_position.position.x)
    filtered_pose_y.append(Filtered_position.position.y)
    filtered_pose_z.append(Filtered_position.position.z)
    filtered_orientation_x.append(Filtered_position.orientation.x)
    filtered_orientation_y.append(Filtered_position.orientation.y)
    filtered_orientation_z.append(Filtered_position.orientation.z)
    filtered_Speed_x.append(Filtered_Speed.linear.x)
    filtered_Speed_y.append(Filtered_Speed.linear.y)
    filtered_Speed_z.append(Filtered_Speed.linear.z)
    filtered_ang_speed_x.append(Filtered_Speed.angular.x)
    filtered_ang_speed_y.append(Filtered_Speed.angular.y)
    filtered_ang_speed_z.append(Filtered_Speed.angular.z)

    # print(Filtered_States)
    # publish filtered pose and twist
    # print('msg about to be sent: \n',msg)
    # print('msg sent: \n',Filtered_States)
    # print('Filtered Values: \n',Filtered_States)
    pub.publish(Filtered_States)
sub= rospy.Subscriber('/gazebo/model_states', ModelStates, model_states_callback)

def kalman_filter(measurement):
    global state_estimate, covariance_estimate

    # Prediction step
    predicted_state = state_estimate
    predicted_covariance = covariance_estimate + Q

    # Correction step
    kalman_gain = predicted_covariance @ np.linalg.inv(
        predicted_covariance + R)
    state_estimate = predicted_state + \
        kalman_gain @ (measurement - predicted_state)
    covariance_estimate = (np.eye(6) - kalman_gain) @ predicted_covariance
    return state_estimate, predicted_state


while 1 and not rospy.is_shutdown():
    atexit.register(plot_graphs)
    rospy.spin()
