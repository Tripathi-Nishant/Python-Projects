from bs4 import BeautifulSoup
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}


def weather(city):
    city=city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    print("Searching in google......\n")
    soup = BeautifulSoup(res.text,'html.parser')   
    if soup.select('#wob_loc'):
        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()       
        info = soup.select('#wob_dc')[0].getText().strip() 
        weather = soup.select('#wob_tm')[0].getText().strip()

        print(location)
        print(time)
        print(info)
        print(weather + "°C")
    else:
        print("❌ Weather data not found. Google may have blocked the request or changed layout.")


print("enter the city name")
city=input()
city=city+" weather"
weather(city)