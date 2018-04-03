sample_freq = 60

SRC_KML = "/home/nightrider/Downloads/gps_log (6).kml"
DST_KML = "/home/nightrider/Downloads/gps_log (6)_subsampled.kml"


def write_start(src_file=None, dst_file=None):
    count = 0
    for line in src_file:
        if count < 3:
            dst_file.write(line)
        else:
            return


def main():
    with open(SRC_KML, "r") as src_kml:
        with open(DST_KML, "w") as dst_kml:

            lines = src_kml.readlines()

            dst_kml.write(lines[0])
            dst_kml.write(lines[1])
            dst_kml.write(lines[2])

            print(len(lines))

            count = 0
            for idx, line in enumerate(lines[3:-2]):
                if "<Placemark" in line:
                    if count % sample_freq == 0 and count >= 3000 and count <= 18000:
                        print(count)
                        dst_kml.write(line)
                        dst_kml.write(lines[idx + 3 + 1])
                        dst_kml.write(lines[idx + 3 + 2])
                        dst_kml.write(lines[idx + 3 + 3])
                        dst_kml.write(lines[idx + 3 + 4])
                        dst_kml.write(lines[idx + 3 + 5])
                        dst_kml.write(lines[idx + 3 + 6])
                        dst_kml.write(lines[idx + 3 + 7])
                        
                    count += 1

            dst_kml.write(lines[-2])
            dst_kml.write(lines[-1])

            print(len(lines))
            print(count)


if __name__ == "__main__":
    main()