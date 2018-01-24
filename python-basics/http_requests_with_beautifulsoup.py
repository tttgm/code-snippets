### HTTP REQUESTS WITH BEAUTIFULSOUP ###

#Can parse HTML with BeautifulSoup and make HTTP requests as follows:
#e.g.
from bs4 import BeautifulSoup   # imports BeautifulSoup
import requests     # imports the 'requests' Python module

def extract_data(page):
    data = {"eventvalidation": "", "viewstate": ""}
    with open(page, "r") as html: 
        soup = BeautifulSoup(html, "html.parser")   
        # parses HTML doc 'html' into 'soup' (which is a BeautifulSoup Object)

        ev = soup.find(id="__EVENTVALIDATION")  
        # finds element/tag with "__EVENTVALIDATION" as the 'id' attribute

        data["eventvalidation"] = ev["value"]   
        # updates the dict value to the data stored in the "value" attribute of the element with "__EVENTVALIDATION" as the 'id'

        vs = soup.find(id="__VIEWSTATE")
        data["viewstate"] = vs["value"]
        # as above, but for 'View State' element

    return data

def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
        data={'AirportList': "BOS",
            'CarrierList': "VX",
            'Submit': 'Submit',
            "__EVENTARGET": "",
            "__EVENTARGUMENT": "",
            "__EVENTVALIDATION": eventvalidation,
            "__VIEWSTATE": viewstate
        }
        )
    # the above code creates a 'post' request to the specified URL, with the 'data' dictionary provided with ALL the required elements specified - i.e., this asks for the data for the aiport defined as "BOS" and the carrier defined as "VX" (Virgin Airlines). The 'event validation' and 'view state' values are assigned to the values extracted in the extract_data() function above.

    return r.text   # returns the plain text stored in this specific request

'''
BEST PRACTICES FOR WEB SCRAPING:

1. Look at how the browser makes requests (make use of 'Inspect->Element' and 'Inspect->Network')
2. Emulate this in code
3. If stuff blows up, look at your HTTP traffic
4. Repeat the above steps as necessary
'''