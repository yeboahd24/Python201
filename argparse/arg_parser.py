import argparse
from typing import List, Tuple
import sys

"""p1 = latitude and longitude
	p2 = latitude and longitude
	point_type validate the input, it convert string to latitude and longitude
"""

def point_type(text: str) -> Tuple[float,float]:
	try:
		last_str, lon_str = text.split()
		lat = float(last_str)
		lon = float(lon_str)
		return lat, lon
	except ValueError as ex:
		raise argparse.ArgumentTypeError(ex)

def get_options(argv: List[str]) -> argparse.Namespace:
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--units", action="store", choices=("MN", "MI", "KM"), default="MN")
	parser.add_argument("p1", action="store", type=point_type)
	parser.add_argument("p2", action="store", type=point_type)
	options = parser.parse_args(argv)
	return options

def main(argv: List[str] = sys.argv[1:]) -> None:
	"""This main script connects the user inputs to the diplayed output."""
	options =get_options(argv)
	lat_1, lon_1 = options.p1
	lat_2, lon_2 = options.p2
	display(lat_1, lat_2, lat_2, lon_2)
if __name__ == "__main__":
	main()