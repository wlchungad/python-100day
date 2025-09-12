# Configuration
BASE_URL = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
datatype = "flw"
options = {
    "dataType":"flw", # flw, fnd, rhrread, warnsum, warningInfo, swt
    "lang": "en" # en/tc/sc
}
concatenated_options = "&".join(f"{key}={value}"for key, value in options.items())
print(concatenated_options)
url = BASE_URL + "?" + concatenated_options
print (url)
# Fetching API
import urllib.request
contents = urllib.request.urlopen(url).read()
# str_contents = contents.decode("UTF-8") # bytes to str
# print (str_contents)

"""
    By document, the output is JSON, but result of type(content) is bytes, meaning the output should be a BSON.
    In this case, we can call orjson to decode as dictionary
    contents.decode("UTF-8") can be called, and we will get the string of content.
"""
import orjson
try:
    dict_content = orjson.loads(contents)
except Exception as e:
    print(f"Error loading content: {e}")
    exit (1)

# try to pretty-print with pprint library here first
# from pprint import pprint
# pprint (dict_content)

"""
With the format like the following, we can get content by keys
Here, we take Local Weather Forecast (flw) as example
    'fireDangerWarning': '...',
    'forecastDesc': '...',
    'forecastPeriod': '...',
    'generalSituation': '...',
    'outlook': '...',
    'tcInfo': '...',
    'updateTime': '...'
Let's convert to a more reader-friendly paragraph
"""
passage = ""
try:
    passage += "----------\n"
    # Start the passage with "When"
    passage += f"{dict_content['updateTime']} - {dict_content['forecastPeriod']}:\n"
    # and then the forecast content:
    passage += f"{dict_content['forecastDesc']}\n"
    # and the outlook
    passage += f"Outlook of the week: {dict_content['outlook']}\n"
    passage += f"Note: {dict_content['generalSituation']}\n"

    passage += "----------\n"
    # if there is fireDanger warning, append an warning message 
    if dict_content['fireDangerWarning']:
        passage += f"WARN - Fire Danger: {dict_content['fireDangerWarning']}\n"
    else:
        passage += "INFO - There is no fire danger warning now.\n"
    # if there is typhoon warning/signal, append an alert message 

    if dict_content['tcInfo']:
        passage += f"ALERT - Typhoon detected: {dict_content['tcInfo']}\n"
    else:
        passage += "INFO - There is no typhoon within 1000km radius from HK.\n"
    # finally print it out:
    print(passage)

    exit(0)
except KeyError as ke:
    print("The key may be non-existant:", ke)
except Exception as e:
    print("Run-time exception:", e)