import simplekml

SRC_KML = "/home/nightrider/Downloads/gps_log_subsampled.kml"
DST_KML = "/home/nightrider/Downloads/gps_log_subsampled_line_string.kml"


def main():
    with open(SRC_KML, "r") as src_kml:

        lines = src_kml.readlines()

        kml = simplekml.Kml()
        ls = kml.newlinestring(name='Path')
        coords = []

        print('num lines: {}'.format(len(lines)))

        count = 0
        for idx, line in enumerate(lines[3:-2]):
            if "<Placemark" in line:
                coords_alt_line = lines[idx + 3 + 4]

                coords_alt_line = coords_alt_line.lstrip(' ')[13:-15]

                nums = [float(num) for num in coords_alt_line.split(',')]

                coords.append((nums))

                count += 1

        ls.coords = coords
        ls.extrude = 1
        ls.altitudemode = simplekml.AltitudeMode.absolute
        kml.save(DST_KML)

        print('num points processed: {}'.format(count))


if __name__ == "__main__":
    main()
