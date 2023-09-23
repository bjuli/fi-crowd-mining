import geojson

if __name__ == "__main__":
    with open("./data/poi.geojson") as f:
        gj = geojson.load(f)
    print(gj)