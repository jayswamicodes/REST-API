import requests
from requests.auth import HTTPBasicAuth

from requests.compat import urljoin
from zipcode_city_map import zip_city
from utils import ResultForTests


def get_weather_by_city_name(url_base, username, password, api_key, city_name, state_code=None, country_code=None):
    """
    Test: Request the weather based on city , state , country name
    Result: verify the city name received in response with the expected city name passed in the request
    
    args:
        url_base: str: base url eg: api.openweathermap.org/data/2.5/weather
        username: str: valid username
        password: str: valid password
        api_key: str: api assigned to each user
        city_name: str: Name of the city
        state_code: str: state name
        country_code: str: country name
    """
    resultstats = ResultForTests()
    
    # Build the url partly based on city name, state & country name passed
    city_url = [city_name]
    if state_code is not None:
        city_url.append(state_code)
        if country_code is not None:
            city_url.append(country_code)
            
    # Build the entire url as list and join it as string as the url to be queried
    url_query_list = ["http://", url_base, "?q=", ",".join(city_url), '&appid=', api_key]
    url_query = urljoin(url_base, "".join(url_query_list))

    # capture the url query response here
    response = requests.get(url_query, auth=HTTPBasicAuth(username, password))
    
    # if status code is 200 then move with the remaining tests else return
    if response.status_code != 200:
        resultstats.result = False
        resultstats.err_msg = f"response code received is {response.status_code}"
        return resultstats
    
    # verify the city name in response and request and return result accordingly
    city_attribute = response.json().get('name')
    if city_attribute is not None and city_attribute.lower() != city_name.lower():
        resultstats.result = False
        resultstats.err_msg = f"city name received in response is {city_attribute} and expected is {city_name}, ignore the case"
        return resultstats
    
    return resultstats

def get_weather_by_lattitude_logitude(url_base, username, password, api_key, lattitude, longitude):
    """
    Test: Request the weather based on lattitude and longitude and
    Result: verify the lattitude and longitude received in response with the expected lattitude and longitude passed in the request
    
    args:
        url_base: str: base url eg: api.openweathermap.org/data/2.5/weather
        username: str: valid username
        password: str: valid password
        api_key: str: api assigned to each user
        lattitude: int: lattitude coordinate
        longitude: int: longitude coordinate
    """
    resultstats = ResultForTests()
    
    # Build the entire url as list and join it as string as the url to be queried
    url_query_list = ["http://", url_base, f"?lat=", str(lattitude), f"&lon=", str(longitude), '&appid=', api_key]
    url_query = urljoin(url_base, "".join(url_query_list))

    # capture the url query response here
    response = requests.get(url_query, auth=HTTPBasicAuth(username, password))
    
    # if status code is 200 then move with the remaining tests else return
    if response.status_code != 200:
        resultstats.result = False
        resultstats.err_msg = f"response code received is {response.status_code}"
        return resultstats

    # verify the lattitude and longitude coordinates in response and request and return result accordingly
    lat_attribute = response.json().get('coord', {}).get('lat')
    lon_attribute = response.json().get('coord', {}).get('lon')
    lat_result = False
    lon_result = False
    
    if lat_attribute is not None and int(lat_attribute) == lattitude:
        lat_result = True    
    if lon_attribute is not None and int(lon_attribute) == longitude:
        lon_result = True
        
    if lat_result and lon_result:
        pass
    else:
        resultstats.result = False
        resultstats.err_msg = f"Lattitude in response {lat_attribute}, and expected value in test {lattitude}, Longitude in response {lon_attribute}, and expected value in test {longitude}"
    
    return resultstats
        

def get_weather_by_zip_code(url_base, username, password, api_key, zipcode, countrycode=None):
    """
    Test: Request the weather based on zipcode and country code
    Result: verify the city name received in response to the city name that corresponds to the zipcode passed in request
    
    args:
        url_base: str: base url eg: api.openweathermap.org/data/2.5/weather
        username: str: valid username
        password: str: valid password
        api_key: str: api assigned to each user
        zipcode: int: area zipcode
        countrycode: str: country name
    """
    resultstats = ResultForTests()
    
    # Build the url partly based on zip code & country name passed
    zip_url = [str(zipcode)]
    if countrycode is not None:
        zip_url.append(countrycode)

    # Build the entire url as list and join it as string as the url to be queried
    url_query_list = ["http://", url_base, f"?zip=", ",".join(zip_url), '&appid=', api_key]
    url_query = urljoin(url_base, "".join(url_query_list))

    # capture the url query response here
    response = requests.get(url_query, auth=HTTPBasicAuth(username, password))
    
    # if status code is 200 then move with the remaining tests else return
    if response.status_code != 200:
        resultstats.result = False
        resultstats.err_msg = f"response code received is {response.status_code}"
        return resultstats
    
     # verify the city name in response corresponds to the zipcode in the request
    city_attribute = response.json().get('name')
    city = zip_city.get(zipcode, "")
    
    if city_attribute.lower() != city.lower():
        resultstats.result = False
        resultstats.err_msg = f"city name is {city}, but response has city {city_attribute}, please update the dictionary zip_city with zipcode and city name to get updated test results, if the zipcode is Not US based then pass the country code as well else the response is incorrect"
        return resultstats
    
    return resultstats

