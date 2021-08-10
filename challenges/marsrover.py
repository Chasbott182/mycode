#!/usr/bin/python3
import urllib.request
import json

## uncomment this import if you run in a GUI
## and want to open the URL in a browser
## import webbrowser

NASAAPI = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?"

def main():
    user = input("What mars photo do you want. ").strip()

    ## Define creds
    with open("../nasa/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    ## remove any "extra" new line feeds on our key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    camerafilter = "&sol=1000&camera=" + user
    ## Call the webservice with our key
    roverurlobj = urllib.request.urlopen(NASAAPI + nasacreds + camerafilter)

    ## read the file-like object
    roverread = roverurlobj.read()

    ## decode JSON to Python data structure
    rover = json.loads(roverread.decode("utf-8"))

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(rover)
    for photo in rover.values():
        for list in photo:
            print("\nRover Name:", list["rover"]["name"] + "\n")
            print("Date of photo:", list["earth_date"] + "\n")
            print("Camera full name:", list["camera"]["full_name"] + "\n")
            print("Camera short name:", list["camera"]["name"] + "\n")
            print("Image URL:", list["img_src"])

    ## Uncomment the code below if running in a GUI
    ## and you want to open the URL in a browser
    ## use Firefox to open the HTTPS URL
    ## input("\nPress Enter to open NASA Picture of the Day in Firefox")
    ## webbrowser.open(decodeapod["url"])
if __name__ == "__main__":
    main()
