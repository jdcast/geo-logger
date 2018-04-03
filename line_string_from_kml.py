def write_start(src_file=None, dst_file=None):
    count = 0
    for line in src_file:
        if count < 3:
            dst_file.write(line)
        else:
            return


def main():
    with open("/Users/jdcast/Desktop/gps_log (6)_subsampled.kml", "r") as src_kml:
        with open("/Users/jdcast/Desktop/gps_log (6)_subsampled_line_string.kml", "w") as dst_kml:

            lines = src_kml.readlines()

            dst_kml.write(lines[0])
            dst_kml.write(lines[1])
            dst_kml.write(lines[2])

            print(len(lines))

            count = 0
            for idx, line in enumerate(lines[3:-2]):
                if "<Placemark" in line:
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
    # main()
    import simplekml

    kml = simplekml.Kml()
    ls = kml.newlinestring(name='A LineString')
    ls.coords = [(18.333868, -34.038274, 10.0), (18.370618, -34.034421, 10.0)]
    ls.extrude = 1
    ls.altitudemode = simplekml.AltitudeMode.relativetoground
    kml.save("/Users/jdcast/Desktop/LineString.kml")