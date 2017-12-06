import json,sys


def load_data(filepath):
    with open(filepath, 'r') as source_file:
    	source_json = json.loads(source_file.read())
    return source_json

def get_biggest_bar(bars_array):
    biggest_bar = max(bars_array, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    print('The biggest bar is:')
    print(json.dumps(biggest_bar, indent=4, ensure_ascii=False))

def get_smallest_bar(bars_array):
    smallest_bar = min(bars_array, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    print('The smallest bar is:')
    print(json.dumps(smallest_bar, indent=4, ensure_ascii=False))

def get_closest_bar(bars_array, longitude, latitude):
    closest_bar = min(bars_array, key=lambda x: (((x['geometry']['coordinates'][0]-longitude)**2)+((x['geometry']['coordinates'][1]-latitude)**2))**0.5)
    print('The closest bar is:')
    print(json.dumps(closest_bar, indent=4, ensure_ascii=False))

def main():
	source_data = load_data(sys.argv[1])
	bars_array = source_data['features']
	get_biggest_bar(bars_array)
	get_smallest_bar(bars_array)
	get_closest_bar(bars_array, float(sys.argv[2]), float(sys.argv[3]))


if __name__ == '__main__':
    main()
