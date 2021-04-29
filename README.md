# geo-logger

See [my project page](https://www.johndallascast.com/project/other/geo_logger/) for a demo.

The steps to run the code and produce a *kml* file (that is viewable in Google Earth) is fairly straightforward:                                                                                                                                                            
1. Setup Raspberry Pi to run in headless mode[^8] (so that it can be ran in the field) 
2. *init.sh* starts the *gpsd* (GPS) service for the Raspberry Pi.  The Raspberry Pi listens to the output of the service on port 2947.
3. The user starts *gps_test.py*
4. The Raspberry Pi then samples *gpsd* service (~1Hz) and writes this output to a file: *gps_log.kml*
5. *subsample_kml.py* is used to subsample the logged points in *gps_log (6).kml* and outputs a subsampled version of it: *gps_log_subsampled.kml*
6. Because *gps_log_subsampled.kml* will just be disconnected location pins if viewed in Google Earth, we use *line_string_from_kml.py* to convert datapoints in *gps_log_subsampled.kml* to a format that when viewed in Google Earth, will be a connected line                                                                    
