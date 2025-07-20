import argparse

import gpxpy


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path")
    parser.add_argument("output_path")
    return parser.parse_args()


def main():
    args = parse_args()

    with open(args.input_path, mode="r") as file:
        gpx = gpxpy.parse(file)

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if point.elevation is not None:
                    point.elevation *= 1000

    with open(args.output_path, mode="w") as file:
        file.write(gpx.to_xml())


if __name__ == "__main__":
    main()
