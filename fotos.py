
import time
import io 
from PIL import Image 
from rcr.robots.scribbler2.Scribbler2 import Scribbler2 
robot = Scribbler2( "COM3", 9600, 500 ) 
motors = robot.getS2Motors()
cam = robot.getF2Camera() 
cam.setPicSize( cam.IMAGE_SMALL ) 
motors.setMotors( 30, -30 )
time.sleep( 2 )
motors.setMotorsOff() 
data =  cam.getImage( cam.IMAGE_GRAYJPEG_FAST )
image = Image.open( io.BytesIO( data.image ) )
image.show() 
motors.setMotors( 30, -30 ) 
time.sleep( 2 )
motors.setMotorsOff()
data =  cam.getImage( cam.IMAGE_JPEG_FAST )
image = Image.open( io.BytesIO( data.image ) )
image.show()
robot.close()
