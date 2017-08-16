
class GasStation(object):
    """
    """
    def __init__(self, gallons_stock, gallons_to_next_gs):
        """
        params:
            * gallons_stock: Amount of gas in gallons at that gas station
            * gallons_next_gs: Amount of gallons of gas needed to get to the
              following gas station
        """
        self.gallons_stock = int(gallons_stock)
        self.gallons_to_next_gs = int(gallons_to_next_gs)


class Car(object):
    """
    """
    def __init__(self):
        # given fuel
        self.gallons = 0

    def traverse_route(self, route):
        """
        params:
            * route: GasStation ordered array
        """
        # geting fuel
        for gs in route:
            self.gallons += gs.gallons_stock
            self.gallons -= gs.gallons_to_next_gs
            if self.gallons < 0:
                raise RuntimeError('Empty Fuel')


class InputParser(object):
    """
    Parse text input to GasStation's objects
    """
    def __init__(self, input_file):
        self.input_file = input_file
        self.inputs = []
        self._read_file()

    def _read_file(self):
        """
        """
        lines = self.input_file.read().splitlines()
        for line in lines:
            gas_stations = []
            line = line.replace('"', '').split(',')
            gs_amount = int(line[0])
            for gs in line[1:gs_amount + 1]:
                gallons_stock, gallons_next_gs = gs.split(':')
                gas_stations.append(
                    GasStation(
                        gallons_stock=gallons_stock,
                        gallons_to_next_gs=gallons_next_gs
                    )
                )
            self.inputs.append(
                Input(gas_stations=gas_stations)
            )


class Input(object):
    """
    Parsed Input
    """
    def __init__(self, gas_stations=[]):
        self.gas_stations = gas_stations

    @property
    def gas_stations_count(self):
        return len(self.gas_stations)


class Router(object):
    """
    Trace circular route betwenn given gas stations
    """
    def trace_route(self, gas_stations):
        """
        Sort Gas stations to make most possible route
        params:
            * gas_stations: array of GasStation objects

        return: tuple: (gas stations route, start index)
        """
        start_gs = sorted(
            gas_stations, key=lambda gs: gs.gallons_stock,
            reverse=True
        )[0]
        start_index = gas_stations.index(start_gs)
        route = gas_stations[start_index:]
        if len(route) < gas_stations:
            route += gas_stations[:start_index]
        return route, start_index





