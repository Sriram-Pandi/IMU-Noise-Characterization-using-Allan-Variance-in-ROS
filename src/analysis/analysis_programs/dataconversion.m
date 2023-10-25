title = readtable("imu.csv")
gy=title{:,15}
la=title{:,19}
save('samedatq','gy','la')