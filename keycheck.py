import requests
import argparse


def color_text(text, color):
    paints = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'reset': '\033[0m',
    }
    return paints[color] + text + paints['reset']



def check_google_maps(g_maps_url, verbose=False):
    try:
        response = requests.get(g_maps_url)
        print(f"URL:  {g_maps_url}")
        status_code = response.status_code
        colored_status = (
            color_text(f"Status Code: {status_code}  ", 'red' ) if status_code == 403 else
            color_text(f"Status Code: {status_code}", 'green') if status_code == 200 else
            color_text(f"Status Code: {status_code}", 'yellow') if status_code == 301 else
            color_text(f"Status Code: {status_code}", 'red') if status_code == 400 else
            f"Status Code: {status_code}"
        )
        print(colored_status)

        if verbose and response.status_code == 200:
            print("Response Content: ")
            print(response.json())
        

        print("\n" + "="*50 + "\n")
    except Exception as e:
        print(f"Error making request in {g_maps_url}: {type(e).__name__} - {e}")
        print("\n" + "="*50 + "\n")

# Put all urls in main function for  to make arg parser 
#Dest is check the values in  nampesapce
def google_recaptcha_key(api_key , verbose=False):
    recapthca_url = "https://www.google.com/recaptcha/api/siteverify"
    recaptcha_secret = api_key
    recaptcha_response = "Response for test"


    try:
        response = requests.post(recapthca_url, data={"secret": recaptcha_secret, "response": recaptcha_response})
        print("ReCaptcha Verification.")
        print(response.json())
        print("\n" + "="*50 + "\n")
    except Exception as e:
        print(f"Error making ReCAPTCHA request: {type(e).__name__} - {e}")
        print("\n" + "="*50 + "\n")


def main():
    parser = argparse.ArgumentParser(description="For api key check")
    parser.add_argument("-api-key",  dest="api_key", help="APi key for google maps", required=True)
    parser.add_argument("--type", dest="key_type", help="Types of key (google_maps or recaptcha)", required=True)
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode. ")

    args = parser.parse_args()

    
    
    if args.key_type == "gm":
        
        google_maps_urls = [f'https://maps.googleapis.com/maps/api/staticmap?center=45%2C10&zoom=7&size=400x400&key={args.api_key}',
        f'https://maps.googleapis.com/maps/api/streetview?size=400x400&location=40.720032,-73.988354&fov=90&heading=235&pitch=10&key={args.api_key}',
        f'https://www.google.com/maps/embed/v1/place?q=place_id:ChIJyX7muQw8tokR2Vf5WBBk1iQ&key={args.api_key}',
        f'https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood4&key={args.api_key}',
        f'https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key={args.api_key}',
        f'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101,-73.89188969999998&destinations=40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key={args.api_key}',
        f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key={args.api_key}',
        f'https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Bingh&types=%28cities%29&key={args.api_key}',
        f'https://maps.googleapis.com/maps/api/elevation/json?locations=39.7391536,-104.9847034&key={args.api_key}',
        f'https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810,-119.6822510&timestamp=1331161200&key={args.api_key}',
        f'https://roads.googleapis.com/v1/nearestRoads?points=60.170880,24.942795%7C60.170879,24.942796%7C60.170877,24.942796&key={args.api_key}'
        ]
        for url in google_maps_urls:
            check_google_maps(url, verbose=args.verbose)
    elif args.key_type == "rc":
        google_recaptcha_key(args.api_key, verbose=args.verbose)
    else:
        print("Something went wrong. Invalid Supported type.")


if __name__ == "__main__":
    main()

    

