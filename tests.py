import argparse
import json

from rest_api_tests import get_weather_by_city_name, get_weather_by_lattitude_logitude, get_weather_by_zip_code


'''
example to run this file: with following args:
python tests.py "api.openweathermap.org/data/2.5/weather", "username", "password", "nfw4383j24j2k4j524kj242kj42" -ts1 testscript1.json -ts2 testscript2.json -ts3 testscript3.json

do tests.py -h, to get details on arguments
'''

parser = argparse.ArgumentParser(description='Process some arguments')
parser.add_argument('baseurl', type=str, help='Base URL to be passed, eg: api.openweathermap.org/data/2.5/weather')
parser.add_argument('username', type=str, help='login username')
parser.add_argument('password', type=str, help='login password')
parser.add_argument('apikey', type=str, help='api key assigned to user')
parser.add_argument('-ts1', '--testscript1', type=argparse.FileType('r'), help="keys allowed in json file: city, state, country")
parser.add_argument('-ts2', '--testscript2', type=argparse.FileType('r'), help="keys allowed in json file: lat, lon")
parser.add_argument('-ts3', '--testscript3', type=argparse.FileType('r'), help="keys allowed in json file: zip, country")

argsc = parser.parse_args()
print(argsc)

test_results = {}
tests_total = 0
tests_passed = 0
tests_failed = 0

if argsc.testscript1:
    test1_data = json.load(argsc.testscript1)
    count = 1
    for test in test1_data:
        key = 'test1' + str(count)
        # test_results[key] = {'input': test, 'output': get_weather_by_city_name(argsc.baseurl, argsc.username, argsc.password, argsc.apikey, test.get('city'), test.get('state'), test.get('country'))}
        op = get_weather_by_city_name(argsc.baseurl, argsc.username, argsc.password, argsc.apikey, test.get('city'), test.get('state'), test.get('country'))
        test_results[key] = {'input': test, 'result': op.result, 'error_msg': op.err_msg}
        count += 1
        tests_total += 1
        if op.result:
            tests_passed += 1
        else:
            tests_failed += 1


if argsc.testscript2:
    test2_data = json.load(argsc.testscript2)
    count = 1
    for test in test2_data:
        key = 'test2' + str(count)
        # test_results[key] = {'input': test, 'output': get_weather_by_lattitude_logitude(argsc.baseurl, argsc.username, argsc.password, argsc.apikey, test.get('lat'), test.get('lon'))}
        op = get_weather_by_lattitude_logitude(argsc.baseurl, argsc.username, argsc.password, argsc.apikey, test.get('lat'), test.get('lon'))
        test_results[key] = {'input': test, 'result': op.result, 'error_msg': op.err_msg}
        count += 1
        tests_total += 1
        if op.result:
            tests_passed += 1
        else:
            tests_failed += 1

if argsc.testscript3:
    test3_data = json.load(argsc.testscript3)
    count = 1
    for test in test3_data:
        key = 'test3' + str(count)
        # test_results[key] = {'input': test, 'output': get_weather_by_zip_code(argsc.baseurl, argsc.username, argsc.password, argsc.apikey, test.get('zip'), test.get('country'))}
        op = get_weather_by_zip_code(argsc.baseurl, argsc.username, argsc.password, argsc.apikey, test.get('zip'), test.get('country'))
        test_results[key] = {'input': test, 'result': op.result, 'error_msg': op.err_msg}
        count += 1
        tests_total += 1
        if op.result:
            tests_passed += 1
        else:
            tests_failed += 1


for k, v in test_results.items():
    print(k, v)

print("Test Coverage Report: ")
print("Total Tests Run : ", tests_total)
print("Total Tests Passed : ", tests_passed)
print("Total Tests Failed : ", tests_failed)
print("Tests pass percentage : ", tests_passed/tests_total * 100, "%")
print("Tests fail percentage : ", tests_failed/tests_total * 100, "%")