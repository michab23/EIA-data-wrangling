import requests
import csv
import datetime

daily = 'https://api.eia.gov/series/?api_key=4d7348d17faec3ce8bf2af9c662ec140&series_id=NG.RNGWHHD.D'
monthly = 'https://api.eia.gov/series/?api_key=4d7348d17faec3ce8bf2af9c662ec140&series_id=NG.RNGWHHD.M'


def generate_csv(period_type, report_type, format):
    # get  data
    response = requests.get(period_type)
    parsed_data = response.json()['series'][0]['data']
    # open a file for writing
    price_report = open('/tmp/'+report_type+'.csv', 'w')
    # create the csv writer object
    csvwriter = csv.writer(price_report)
    # write headers
    csvwriter.writerow(["Date", "Price"])

    for emp in parsed_data:
        # write rows

        csvwriter.writerow([datetime.datetime.strptime(emp[0], format).date(),
                            emp[1]])
    price_report.close()


generate_csv(daily, 'daily_report',  "%Y%m%d")
generate_csv(monthly, 'monthly_report', "%Y%m")




