# REST-API

Modules required to run:
- argparse
- json
- requests

There are 7 files in total:
- 3 json files that contain test data, that can be modified to add more tests
- 4 python files
- All files should be located in the same directory
- testscript1.json defines test data for test script 1 as defined in pdf file. It is a list of dictionary, where each dictionary represents a testcase.
- same above holds for testscript2.json & testscript3.json
- the json files are passed as arguments to the tests and the keys in respective json files can be found in "python3 tests.py -h"
- rest_api_tests.py is where the test code is written
- zipcode_city_map.py contains zipcode to city mapping for test script 3

Run the tests.py file using the args as shown below (preferred python3):
- python3 tests.py "api.openweathermap.org/data/2.5/weather" $username $password $apikey -ts1 testscript1.json -ts2 testscript2.json -ts3 testscript3.json
To get info on the args used you can do "python3 tests.py -h"



Test Results:
- Total 7 testcases added by me, feel free to add more tests in the format defined
- 6 testcases will pass, 1 testcase fails on purpose
- The test report is printed to the console at the end of the file
  - It prints per test id, input, the result & the error msg
  - At the end it summarizes the total tests run, pass & failed
