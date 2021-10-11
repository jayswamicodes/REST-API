# REST-API

Modules required to run:
- argparse
- json
- requests

There are 7 files in total:
- 3 json files that contain test data, that can be modified to add more tests
- 4 python files
- All files should be located in the same directory

Run the tests.py file using the args as shown below (preferred python3):
python3 tests.py "api.openweathermap.org/data/2.5/weather", $username, $password, $apikey -ts1 testscript1.json -ts2 testscript2.json -ts3 testscript3.json
To get info on the args used you can do "python3 tests.py -h"

The test report is printed to the console at the end of the file
