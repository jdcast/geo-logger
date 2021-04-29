# geo-logger

Python software to record GPS, velocity and elevation on headless Raspberry Pi 3B+.

See [my project page](https://www.johndallascast.com/project/other/geo_logger/) for a demo and necessary hardware.

The steps to run the code and produce a *kml* file (that is viewable in Google Earth) is fairly straightforward:                                                                                                                                                            
1. Setup Raspberry Pi to run in headless mode (so that it can be ran in the field) 
2. *init.sh* starts the *gpsd* (GPS) service for the Raspberry Pi.  The Raspberry Pi listens to the output of the service on port 2947.
3. The user starts *gps_test.py*
4. The Raspberry Pi then samples *gpsd* service (~1Hz) and writes this output to a file: *gps_log.kml*
5. *subsample_kml.py* is used to subsample the logged points in *gps_log.kml* and outputs a subsampled version of it: *gps_log_subsampled.kml*
6. Because *gps_log_subsampled.kml* will just be disconnected location pins if viewed in Google Earth, we use *line_string_from_kml.py* to convert datapoints in *gps_log_subsampled.kml* to a format that when viewed in Google Earth, will be a connected line                                                                    


**gps_log_kayak_test.kml**, **gps_log_subsampled_kayak_test.kml** and **gps_log_subsampled_line_string_kayak_test.kml** originated from steps `4`, `5` and `6` respectively.
These three files can be viewed in Google Earth.

**gps_log_initial_test.kml** is the first log created when I wrote the software and cab be ignored.
It has been stored only for record keeping.

Preview of **gps_log_subsampled_line_string_kayak_text.kml** in Google Earth (path in top and elevation in bottom):
![alt text](https://www.johndallascast.com/project/other/geo_logger/featured_hu7b726e58572fbfee33e58549bd3bda3a_2392043_720x0_resize_lanczos_2.png)
