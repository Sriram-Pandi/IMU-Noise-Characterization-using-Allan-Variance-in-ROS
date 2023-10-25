import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from bagpy import bagreader

imu_data_5hrbg=bagreader('/home/sriram/EECE5554/LAB3/5hr.bag')

imu_data_5hrf= imu_data_5hrbg.message_by_topic('/imu')

df = pd.read_csv(imu_data_5hrf)
