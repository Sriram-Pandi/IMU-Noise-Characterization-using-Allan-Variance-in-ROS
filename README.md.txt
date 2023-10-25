** IMU Noise Characterization using Allan Variance in ROS**

**Description:**

This project delves deep into the intricacies of characterizing the noise in Inertial Measurement Units (IMUs) using the Allan Variance technique. I utilized the Robot Operating System (ROS) to facilitate this analysis. Here's a detailed breakdown of the project:

1. **IMU Device Driver Development**: 
   - I crafted a ROS device driver for the VectorNav IMU that communicates over USB serial.
   - The driver effectively parses the `$VNYMR` string, extracting accelerometer, gyroscope, orientation (roll, pitch, yaw), and magnetometer data.
   - The driver publishes the parsed data using standard ROS `sensor_msgs/Imu` and `sensor_msgs/MagneticField` messages. Euler angles were derived by converting the quaternion data.

2. **Hardware Configuration and Latency Management**:
   - Ensured a smooth communication with the VectorNav VN-100 IMU by implementing specific udev rules to address USB latency issues prevalent in Ubuntu.

3. **Stationary Noise Analysis**:
   - Acquired a minimum of 5 minutes of stationary IMU data.
   - Analyzed the time series and frequency distribution of each axis of the IMU data.
   - Characterized the noise profiles, including mean and standard deviation, of the reported IMU values.

4. **Allan Variance Data Collection and Analysis**:
   - In a team setting, collected approximately 5 hours of stationary IMU data, ensuring the chosen location was devoid of vibrations and other noise sources.
   - Individually, I processed this data using MATLAB to derive the Allan variance. This involved leveraging functions and techniques presented by MathWorks.
   - Through the Allan Variance analysis, I could identify:
     - Types and sources of errors and noise present in the IMU readings.
     - Suitable models for these errors.
     - Comparisons between the derived performance metrics and those listed in the VN100 datasheet.

5. **Documentation and Repository Structuring**: 
   - Assembled a comprehensive report detailing the methodologies, findings, and conclusions derived from both the stationary data analysis and the Allan Variance analysis.
   - Structured the GitHub repository to ensure clarity and ease of access, segregating ROS drivers, analysis scripts, and the final report.

By the conclusion of this project, I gained a comprehensive understanding of IMU noise profiles and their implications. The Allan Variance technique proved instrumental in deriving deeper insights into the nuances of IMU data, paving the way for better-informed decisions in robotics sensing and navigation applications.