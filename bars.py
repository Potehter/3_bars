import json
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as source_file:
        source_content = json.loads(source_file.read())
    return source_content


def get_biggest_bar(bars_array):
    biggest_bar = max(bars_array, key=lambda x:
                      x['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(bars_array):
    smallest_bar = min(bars_array, key=lambda x:
                       x['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_closest_bar(bars_array, longitude, latitude):
    '''
    блишайший бар ищем по формуле: sqrt((x1 - x2)**2 + (y1 - y2)**2)
    https://algebra24.ru/rasstojanie-mezhdu-dvumja-tochkami
    '''
    closest_bar = min(bars_array, key=lambda x:
                      (((x['geometry']['coordinates'][0] - longitude)**2) +
                      ((x['geometry']['coordinates'][1] - latitude)**2))**0.5)
    return closest_bar


def print_bar_main_data(bar, lead_property):
    bar_attributes = bar['properties']['Attributes']
    bar_main_data = (lead_property,
                     bar_attributes['Name'],
                     bar_attributes['Address'],
                     bar_attributes['PublicPhone'][0]['PublicPhone'],
                     bar_attributes['SeatsCount'])
    string_to_print = '{0} бар: {1}, по адресу {2}; телефон: {3}, мест: {4}'
    print(string_to_print.format(*bar_main_data))


def main():
    source_data = load_data(sys.argv[1])
    bars_array = source_data['features']
    biggest_bar = get_biggest_bar(bars_array)
    print_bar_main_data(biggest_bar, 'Самый большой')
    smallest_bar = get_smallest_bar(bars_array)
    print_bar_main_data(smallest_bar, 'Самый маленький')
    closest_bar = get_closest_bar(bars_array,
                                  float(sys.argv[2]), float(sys.argv[3]))
    print_bar_main_data(closest_bar, 'Ближайший')


if __name__ == '__main__':
    main()
