global unit


class City():

    def __init__(self, city_name):
        from geopy.geocoders import Nominatim

        geolocator = Nominatim()
        location = geolocator.geocode(city_name)

        self.latitude = location.latitude
        self.longitude = location.longitude


def distance(city1, city2, units):
    global unit
    vertical = abs(city1.longitude - city2.longitude)
    horizontal = abs(city1.latitude - city2.latitude)

    if units == 1:
        multi = 111
        unit = 'km'
    elif units == 2:
        multi = 69
        unit = 'miles'

    vertical *= multi
    horizontal *= multi

    return(vertical, horizontal)


def exact(dists):
    from math import sqrt

    final = sqrt(dists[0]**2 + dists[1]**2)
    return final


def main():
    print('============== CITY DISTANCE ==============')
    print('              author: typho0s')

    units = int(input('Specifiy the distance unit:\n1) Kilometers\n2) Miles\n: '))
    if units != 1 and units != 2:
        print('Input a proper value')
        quit()

    city1_name = input('Name of the first city: ')
    city2_name = input('Name of the second city: ')

    city1 = City(city1_name)
    city2 = City(city2_name)

    dists = (distance(city1, city2, units))
    print('The distance between the two cities is:')
    print('{0:.2f} '.format(exact(dists)) + unit)


if __name__ == '__main__':
    main()
