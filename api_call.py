import requests


if __name__ == "__main__":
    # response = requests.get('https://rest.busradar.conterra.de/prod/haltestellen/8',
    #             headers="accept: application/json",
    #             verify=False)
    # response.json()
    token = 'gyhtVejgaTn4jdBcQqzy4MzR'
    locs = requests.get('http://twitter.com/search?q=munster',
                      headers={'Content-Type': 'Application/json',
                               'X-API-Token': 'gyhtVejgaTn4jdBcQqzy4MzR'})
    #print(re.status_code)
    #print(locs.json())
    location_nums = [100, 117, 296, 310]
    location_num = 100
    from_ts = '2023-09-21T00%3A00%3A00'
    to_ts = '2023-09-22T00%3A00%3A00'
    all_data = requests.get(f"https://static.hystreet.com/api/https://api.hystreet.com/locations/{location_num}?from={from_ts}&to={to_ts}&resolution=day",
                            headers={'Content-Type': 'Application/json',
                                     'X-API-Token': 'gyhtVejgaTn4jdBcQqzy4MzR'})
    print(all_data.status_code)
    pedestrian_json = all_data.json()
    print(pedestrian_json['measurements'])

    main(pedestrian_json)