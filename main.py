#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import pytz
import random
import os
import pandas as pd
import zombie_func as func 
import zombie_class as zc



time_zone = pytz.timezone("Europe/Moscow")
date = datetime.datetime(2020, 6, 1, 12, 0, 0, 0, time_zone)
'''date = datetime.datetime.now(datetime.timezone.utc)'''


latitude = 57.57
longitude = 37.37
number_of_clouds = 30
cloud_list = list()


for i in range(number_of_clouds):

    center_of_cloud_x = random.randint(-150, 150)
    center_of_cloud_y = random.randint(-150, 150)
    height_cloud = random.randint(50, 150)
    speed_x = random.randint(-10, 10)
    speed_y = random.randint(-10, 10)
    const_x = random.randint(10, 40)
    const_y = random.randint(10, 40)
    cloud_list.append(zc.Cloud(center_of_cloud_x, center_of_cloud_y, height_cloud, speed_x, speed_y, const_x, const_y))


human = zc.Human(x0=0, y0=0, z0=0) # point human
sensor = zc.Sensor()
sensor_zero_status = sensor.check() 

work_time = list()
status = list()



number_of_simulated_hours = 1 # how much hours you want


for t in range(number_of_simulated_hours*60): # hours -> minutes

    checking = list()
    sun = zc.Sun(latitude, longitude, date)
    work_time.append(date.strftime("%Y-%m-%d-%H:%M"))

    for i in range(number_of_clouds):

        cloud = cloud_list[i]

        if func.check(sun, cloud, human) or sun.vec()[2] < 0:

            checking.append(True)

        else:

            checking.append(False)

    if True in checking:

        sensor.on()   # choice of working mode

    else:

        sensor.off()

    func.plotting(sun, cloud_list, human, t,number_of_clouds)  
    status.append(sensor.check())
    sensor_curr_status = sensor.check()

   
    sensor_zero_status = sensor_curr_status

    func.update_field(cloud_list, sun,number_of_clouds)
    date += datetime.timedelta(minutes=1)
func.simulation(number_of_simulated_hours)
os.startfile("Simulation.mp4")
df = pd.DataFrame({'Time since start': work_time, 'Sensor Status': status})
df.to_excel('CHECK_LIST.xlsx')
#func.path_clear()


# In[ ]:





# In[ ]:




