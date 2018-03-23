import gps
import simplekml

avg_lat     = 0.0
avg_lon     = 0.0
avg_speed   = 0.0
avg_alt     = 0.0

num_samples = 0
 
# Listen on port 2947 (gpsd) of localhost
kml     = simplekml.Kml()
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

with open('gps_test_output.txt', 'w') as f:
    while True:
        try:
            report = session.next()
            # Wait for a 'TPV' report and display the current time
            # To see all report data, uncomment the line below
            #f.write("{}\n\n".format(report))
	    #print(report)
            if report['class'] == 'TPV':
                if hasattr(report, 'lat') and hasattr(report, 'lon') \
                   and hasattr(report, 'alt') and hasattr(report, 'speed'):
                    print(report.lat)
                    print(report.lon)
		    print(report.alt)
		    print(report.speed)			
                    print("\n")
                    
                    avg_lat     += report.lat
                    avg_lon     += report.lon
                    avg_alt     += report.alt
                    avg_speed   += report.speed

                    kml.newpoint(name="point_{}".format(num_samples),
                                 coords=[(report.lon, report.lat, report.alt)],
				 description="velocity: {}".format(report.speed),
                                 altitudemode="absolute")
                    
                    num_samples += 1
        except KeyError:
            print("KeyError")
            pass
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            print("{}".format(avg_lat/num_samples))
            print("{}".format(avg_lon/num_samples))
            print("{}".format(avg_alt/num_samples))
            print("{}".format(avg_speed/num_samples))
            
            f.write("Average latitude: {}\n".format(avg_lat/num_samples))
            f.write("Average longitude: {}\n".format(avg_lon/num_samples))
            f.write("Average altitude: {}\n".format(avg_alt/num_samples))
            f.write("Average speed: {}\n".format(avg_speed/num_samples))

            kml.save('gps_log.kml')
            
            quit()
        except StopIteration:
            print("StopIteration")
            session = None
            print("GPSD has terminated")
