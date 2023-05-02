# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from scrapurls import fetch_table_to_csv
from searchitem import fetch_sim_type
from scrapurls import fetch_table_to_csv,fetch_header_to_csv

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# fetch header to csv file with stativ link
fetch_header_to_csv(f"https://www.rond.ir/SearchSim?page=1"
                        "&SimOrderBy=&ItemPerPage=&SixthDigit="
                        "&FifthDigit=&FourthDigit=&ThirdDigit="
                        "&SecondDigit=&FirstDigit=&Code=&PreCode="
                        "&SimOperatorE=2&StateId=&SimType=2&CityId="
                        "&SimStatus=&SimCoPrice=&SimQuality=&PriceFrom="
                        "&SimQualityTypeId=25"
                        "&PriceTo=&VendorType=", 'rond_data.csv')

# for support paging
isHaveNextPage = True
page = 1

round_type = []
sim_type = []
sim_status = []
round_type, sim_type, sim_status = fetch_sim_type()

# change URL dynamically
for sim_t in sim_type:
    for ro_type in round_type:
        fetch_table_to_csv(f"https://www.rond.ir/SearchSim?page={page}",
                        "&SimOrderBy=&ItemPerPage=&SixthDigit="
                        "&FifthDigit=&FourthDigit=&ThirdDigit="
                        "&SecondDigit=&FirstDigit=&Code=&PreCode="
                        f"&SimOperatorE=2&StateId=&SimType={sim_t}&CityId="
                        "&SimStatus=&SimCoPrice=&SimQuality=&PriceFrom="
                        f"&SimQualityTypeId={ro_type}"
                        "&PriceTo=&VendorType=", 'rond_data.csv')