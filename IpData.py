import requests
from bs4 import BeautifulSoup


class IpData:
    def __init__(self):
        self.data = {None}
        self.response = None
        self.results = {None}

    def query_ip_address(self, ip_addr):
        """
        Takes the IP to be searched and begins the data request process
        :param ip_addr: string
        """
        self.data = {"query": str(ip_addr),
                     "submit": "IP+Lookup"}
        self.__make_request()
        self.__parse_response()

    def __make_request(self):
        """
        Makes a connection with the endpoint using the URL using a POST request, fetching the HTML containing the IP data being queried
        """
        try:
            res = requests.post("https://www.iplocation.net/ip-lookup", self.data)
            self.response = BeautifulSoup(res.content, "html.parser")
        except Exception as e:
            print(f"Error: {e}")

    def __parse_response(self):
        """
        Takes the HTTP scraped from the endpoint and then finds the IP data within the HTML
        """
        table = self.response.find("table")
        #head_one, head_two = table.find_all("thead")
        body_one, body_two = table.find_all("tbody")

        ip_addr, country, region, city = body_one.find_all("td")
        isp, organization, latitude, longitude = body_two.find_all("td")

        self.results = {"Ip_Address": ip_addr.getText(),
                        "Country": country.getText(),
                        "Region": region.getText(),
                        "City": city.getText(),
                        "ISP": isp.getText(),
                        "Organization": organization.getText(),
                        "Latitude": latitude.getText(),
                        "Longitude": longitude.getText()}

    def get_ip_address(self):
        """
        Returns the queried IP Address
        :return: string
        """
        return self.results["Ip_Address"]

    def get_country(self):
        """
        Returns the country of the IP Address
        :return: string
        """
        return self.results["Country"]

    def get_region(self):
        """
        Returns the region of the IP Address
        :return: string
        """
        return self.results["Region"]

    def get_city(self):
        """
        Returns the city of the IP Address
        :return: string
        """
        return self.results["City"]

    def get_isp(self):
        """
        Returns the ISP of the IP Address
        :return: string
        """
        return self.results["ISP"]

    def get_organization(self):
        """
        Returns the organization of the IP Address
        :return: string
        """
        return self.results["Organization"]

    def get_latitude(self):
        """
        Returns the latitude of the IP Address
        :return: string
        """
        return self.results["Latitude"]

    def get_longitude(self):
        """
        Returns the longitude of the IP Address
        :return: string
        """
        return self.results["Longitude"]

    def get_all(self):
        """
        Returns all the data held about the IP Address
        :return: Dict
        """
        return self.results
