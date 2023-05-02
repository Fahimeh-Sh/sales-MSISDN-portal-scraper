import requests
from bs4 import BeautifulSoup

def fetch_sim_type():

    url = requests.get('https://www.rond.ir/SearchSim?SimOrderBy=&ItemPerPage=&SixthDigit=&'
                       'FifthDigit=&FourthDigit=&ThirdDigit=&SecondDigit=&FirstDigit=&Code=&'
                       'PreCode=&SimOperatorE=2&StateId=&SimType=2&CityId=&SimStatus=&'
                       'SimCoPrice=&SimQuality=&PriceFrom=&SimQualityTypeId=32&PriceTo=&VendorType=')
    soup = BeautifulSoup(url.text, 'html.parser')
    # fetch search table in table var
    rond_typeid = soup.find('select', attrs={'id': 'SimQualityTypeId'})
    sim_type = soup.find('select', attrs={'id': 'SimType'})
    sim_status = soup.find('select', attrs={'id': 'SimStatus'})

    # getting All Column For Header
    get_options = rond_typeid.findAll('option')
    get_sim_options = sim_type.findAll('option')
    get_simstatus_options = sim_status.findAll('option')

    round_type_options = []
    sim_options = []
    simstaus_options = []
    # Looping for appending text to list Headers
    for r in get_options:
        # round_type_options.append(r.text.strip())
        round_type_options.append(r["value"])

    for st in get_simstatus_options:
        # simstaus_options.append(st.text.strip())
        simstaus_options.append(st["value"])

    for st in get_sim_options:
        # sim_options.append(st.text.strip())
        sim_options.append(st["value"])

    # return parameters as list
    return round_type_options, sim_options, simstaus_options


