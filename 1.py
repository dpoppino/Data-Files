import numpy as np
import requests
import pandas as pd
import json
import pickle
from tqdm import tqdm
import collections
pd.options.mode.chained_assignment = None  # default='warn' #This is in place to remove the warning for the copy error generated by copying a columns in the dataframes.


def year(x):
    if x < 1:
        return 2005
    if x < 2:
        return 2006
    if x < 3:
        return 2007
    if x < 4:
        return 2008
    if x < 5:
        return 2009
    if x < 6:
        return 2010
    if x < 7:
        return 2011
    if x < 8:
        return 2012
    if x < 9:
        return 2013
    if x < 10:
        return 2014
    if x < 11:
        return 2015
    if x < 12:
        return 2016
    if x < 13:
        return 2017
    if x < 14:
        return 2018
    if x < 15:
        return 2019

final_df = pd.DataFrame()
final_list = []

for i in tqdm(range(15)): #15 is the number of years being pulled.  This would have to be manually updated to add more years
    temp = str(year(i))
    call = "https://api.census.gov/data/" + temp + "/cps/basic/jan?get=PEMNTVTY,PEFNTVTY,GTCBSA,HRYEAR4,HRMONTH&key=63b83cdcd2e0c848c7bbe79b98d90c7e47312366"
    temp_list = (requests.get(call).text)

    jsonLocales = json.loads(temp_list)
    newdata = pd.DataFrame(jsonLocales)
    newdata1 = newdata.iloc[1:, :]
    newdata1[0] = newdata1[0].replace(" ", "")
    newdata1[1] = newdata1[1].replace(" ", "")
    newdata1[2] = newdata1[2].replace(" ", "")
    newdata1[3] = newdata1[3].replace(" ", "")
    newdata1[4] = newdata1[4].replace(" ", "")
    for i in tqdm(newdata1.index):
        a = int(newdata1.loc[i].at[0])
        b = int(newdata1.loc[i].at[1])
        c = int((newdata1.loc[i].at[2]))
        if a is not 57 and b is not 57 and c is not 0:
            data = newdata1.loc[i].to_dict()
            final_list.append(data)


final_df = pd.DataFrame.from_dict(final_list)

# final_df.to_pickle("/Users/dpops/Library/CloudStorage/OneDrive-Facebook/School1/MBA/Tools for Data Analysis/api data.pkl")

locationdict = {
    "12420": "Austin-Round Rock, TX",
    "14540": "Bowling Green, KY",
    "29940": "Lawrence, KS",
    "48060": "Watertown-Fort Drum, NY",
    "19340": "Davenport-Moline-Rock Island, IA-IL",
    "36500": "Olympia, WA",
    "14260": "Boise, ID",
    "24020": "Glens Falls, NY",
    "26820": "Idaho Falls, ID",
    "31700": "Manchester-Nashua, NH",
    "41180": "Saint Louis, MO-IL",
    "12540": "Bakersfield, CA",
    "13820": "Birmingham-Hoover, AL",
    "33660": "Mobile, AL",
    "11300": "Anderson, IN",
    "27100": "Jackson, MI",
    "37460": "Panama City, FL",
    "49660": "Youngstown-Warren-Boardman, OH-PA",
    "49740": "Yuma, AZ",
    "49180": "Winston-Salem, NC",
    "29740": "Las Cruces, NM",
    "33460": "Minneapolis-St Paul-Bloomington, MN-WI",
    "39300": "Providence-Warwick, RI-MA",
    "33340": "Milwaukee-Waukesha-West Allis, WI",
    "34900": "Napa, CA",
    "12700": "Barnstable, MA",
    "17420": "Cleveland, TN",
    "20260": "Duluth, MN-WI",
    "26100": "Holland-Grand Haven, MI",
    "37340": "Palm Bay-Melbourne-Titusville, FL",
    "71650": "Boston-Cambridge-Quincy, MA-NH",
    "19820": "Detroit-Warren-Dearborn, MI",
    "39340": "Provo-Orem, UT",
    "29460": "Lakeland-Winter Haven, FL",
    "29540": "Lancaster, PA",
    "36740": "Orlando, FL",
    "41700": "San Antonio, TX",
    "46940": "Vero Beach, FL",
    "73450": "Hartford-West Hartford-East Hartford, CT",
    "17980": "Columbus, GA-AL",
    "32580": "McAllen-Edinburg-Mission, TX",
    "22420": "Flint, MI",
    "26420": "Houston-Baytown-Sugar Land, TX",
    "30460": "Lexington-Fayette, KY",
    "37860": "Pensacola-Ferry Pass-Brent, FL",
    "39100": "Poughkeepsie-Newburgh-Middletown, NY",
    "44100": "Springfield, IL",
    "11540": "Appleton, WI",
    "40140": "Riverside-San Bernardino-Ontario, CA",
    "10900": "Allentown-Bethlehem-Easton, PA-NJ",
    "28020": "Kalamazoo-Portage, MI",
    "41420": "Salem, OR",
    "41860": "San Francisco-Oakland-Fremont, CA",
    "47380": "Waco, TX",
    "15680": "California-Lexington Park, MD",
    "17860": "Columbia, MO",
    "30780": "Little Rock-North Little Rock, AR",
    "35980": "Norwich-New London, CT",
    "79600": "Worcester, MA-CT",
    "29820": "Las Vegas-Paradise, NV",
    "28700": "Kingsport-Bristol, TN-VA",
    "39740": "Reading, PA",
    "43620": "Sioux Falls, SD",
    "16580": "Champaign-Urbana, IL",
    "22900": "Fort Smith, AR-OK",
    "35620": "New York-Newark- Jersey City, NY-NJ-PA (White Plains central city recoded to balance of metropolitan)",
    "36100": "Ocala, FL",
    "37100": "Oxnard-Thousand Oaks-Ventura, CA",
    "39380": "Pueblo, CO",
    "41060": "Saint Cloud, MN",
    "48620": "Wichita, KS",
    "22660": "Fort Collins, CO",
    "47260": "Virginia Beach-Norfolk-Newport News, VA-NC",
    "30020": "Lawton, OK",
    "71950": "Bridgeport-Stamford-Norwalk, CT",
    "10180": "Abilene, TX",
    "45460": "Terre Haute, IN",
    "10580": "Albany-Schenectady-Troy, NY",
    "21500": "Erie, PA",
    "78700": "Waterbury, CT",
    "18140": "Columbus, OH",
    "25260": "Hanford-Corcoran, CA",
    "41620": "Salt Lake City, UT",
    "42060": "Santa Barbara-Santa Maria-Goleta, CA",
    "42140": "Santa Fe, NM",
    "12020": "Athens-Clarke County, GA",
    "19100": "Dallas-Fort Worth-Arlington, TX",
    "22500": "Florence, SC",
    "25540": "Hartford-West Hartford-East Hartford, CT",
    "30980": "Longview, TX",
    "36220": "Odessa, TX",
    "76450": "Norwich-New London, CT-RI",
    "20100": "Dover, DE",
    "23580": "Gainesville, GA",
    "47940": "Waterloo-Cedar Falls, IA",
    "13380": "Bellingham, WA",
    "31180": "Lubbock, TX",
    "44060": "Spokane-Spokane Valley, WA",
    "11340": "Anderson, SC",
    "21340": "El Paso, TX",
    "23020": "Fort Walton Beach-Crestview-Destin, FL",
    "42020": "San Luis Obispo-Paso Robles, CA",
    "42540": "Scranton--Wilkes-Barre, PA",
    "46220": "Tuscaloosa, AL",
    "47220": "Vineland-Bridgeton, NJ",
    "10420": "Akron, OH",
    "46540": "Utica-Rome, NY",
    "12100": "Atlantic City-Hammonton, NJ",
    "12220": "Auburn-Opelika, AL",
    "22220": "Fayetteville-Springdale-Rogers, AR-MO",
    "35300": "New Haven-Milford, CT",
    "24780": "Greenville, NC",
    "31540": "Madison, WI",
    "36140": "Ocean City, NJ",
    "36540": "Omaha-Council Bluffs, NE-IA",
    "76750": "Portland-South Portland, ME",
    "13740": "Billings, MT",
    "16980": "Chicago-Naperville-Elgin, IL-IN-WI",
    "35840": "North-Port-Sarasota-Bradenton, FL",
    "23060": "Fort Wayne, IN",
    "32780": "Medford, OR",
    "74500": "Leominster-Fitchburg-Gardner, MA",
    "31420": "Macon, GA",
    "44180": "Springfield, MO",
    "12940": "Baton Rouge, LA",
    "27740": "Johnson City, TN",
    "41940": "San Jose-Sunnyvale-Santa Clara, CA",
    "47580": "Warner Robins, GA",
    "35380": "New Orleans-Metairie, LA",
    "14500": "Boulder, CO",
    "25500": "Harrisonburg, VA",
    "36260": "Ogden-Clearfield, UT",
    "29340": "Lake Charles, LA",
    "29700": "Laredo, TX",
    "42660": "Seattle-Tacoma-Bellevue, WA",
    "10500": "Albany, GA",
    "14010": "Bloomington, IL",
    "17140": "Cincinnati, OH-KY-IN",
    "19660": "Deltona-Daytona Beach-Ormond Beach, FL",
    "34740": "Muskegon-Norton Shores, MI",
    "45300": "Tampa-St. Petersburg-Clearwater, FL",
    "70900": "Barnstable, MA",
    "46340": "Tyler, TX",
    "78100": "Springfield, MA-CT",
    "26180": "Honolulu, HI",
    "33740": "Monroe, LA",
    "38940": "Port Saint Lucie-Fort Pierce, FL",
    "11500": "Anniston-Oxford-Jacksonville, AL",
    "12580": "Baltimore-Columbia-Towson, MD",
    "25180": "Hagerstown-Martinsburg, MD-WV",
    "46140": "Tulsa, OK",
    "48660": "Wichita Falls, TX",
    "27140": "Jackson, MS",
    "19300": "Daphne-Fairhope-Foley, AL",
    "17660": "Coeur d Alene, ID",
    "27780": "Johnstown, PA",
    "29180": "Lafayette, LA",
    "33780": "Monroe, MI",
    "10740": "Albuquerque, NM",
    "17900": "Columbia, SC",
    "19460": "Decatur, AL",
    "19500": "Decatur, IL",
    "39140": "Prescott, AZ",
    "43900": "Spartanburg, SC",
    "14860": "Bridgeport-Stamford-Norwalk, CT",
    "11020": "Altoona, PA",
    "40420": "Rockford, IL",
    "45220": "Tallahassee, FL",
    "28420": "Kennewick-Richland, WA",
    "40380": "Rochester, NY",
    "41740": "San Diego-Carlsbad-San Marcos, CA",
    "46700": "Vallejo-Fairfield, CA",
    "72850": "Danbury, CT",
    "29100": "La Crosse, WI-MN",
    "31140": "Louisville, KY-IN",
    "34820": "Myrtle Beach-Conway-North Myrtle Beach, SC-NC",
    "77200": "Providence-Fall River-Warwick, RI-MA",
    "28740": "Kingston, NY",
    "33860": "Montgomery, AL",
    "40220": "Roanoke, VA",
    "42100": "Santa Cruz-Watsonville, CA",
    "49020": "Winchester, VA-WV",
    "46060": "Tucson, AZ",
    "32820": "Memphis, TN-MS-AR",
    "12260": "Augusta-Richmond County, GA-SC",
    "20500": "Durham-Chapel Hill, NC",
    "22520": "Florence-Muscle Shoals, AL",
    "77350": "Rochester-Dover, NH-ME",
    "24340": "Grand Rapids-Wyoming, MI",
    "19740": "Denver-Aurora-Lakewood, CO",
    "28100": "Kankakee-Bradley, IL",
    "24140": "Goldsboro, NC",
    "28140": "Kansas City, MO-KS",
    "42260": "Sarasota-Bradenton-Venice, FL",
    "49340": "Worcester, MA-CT",
    "15980": "Cape Coral-Fort Myers, FL",
    "33700": "Modesto, CA",
    "39460": "Punta Gorda, FL",
    "11700": "Asheville, NC",
    "14060": "Bloomington-Normal, IL",
    "15540": "Burlington-South Burlington, VT",
    "27500": "Janesville-Beloit, WI",
    "34980": "Nashville-Davidson-Murfreesboro, TN",
    "47900": "Washington-Arlington-Alexandria, DC-VA-MD-WV",
    "18580": "Corpus Christi, TX",
    "35660": "Niles-Benton Harbor, MI",
    "12060": "Atlanta-Sandy Springs-Roswell, GA",
    "16620": "Charleston, WV",
    "17460": "Cleveland-Elyria, OH",
    "34580": "Mount Vernon-Anacortes, WA",
    "46520": "Honolulu, HI",
    "19380": "Dayton, OH",
    "25060": "Gulfport-Biloxi, MS",
    "41500": "Salinas, CA",
    "45060": "Syracuse, NY",
    "16060": "Carbondale-Marion, IL",
    "20700": "East Stroudsburg, PA",
    "26980": "Iowa City, IA",
    "20740": "Eau Claire, WI",
    "15380": "Buffalo-Cheektowaga-Niagara Falls, NY",
    "24580": "Green Bay, WI",
    "44140": "Springfield, MA",
    "22180": "Fayetteville, NC",
    "26620": "Huntsville, AL",
    "28660": "Killeen-Temple-Fort Hood, TX",
    "70750": "Bangor, ME",
    "75700": "New Haven, CT",
    "12620": "Bangor, ME",
    "30340": "Lewiston-Auburn, ME",
    "45820": "Topeka, KS",
    "25420": "Harrisburg-Carlisle, PA",
    "31100": "Los Angeles-Long Beach-Santa Ana, CA",
    "31460": "Madera, CA",
    "17820": "Colorado Springs, CO",
    "42340": "Savannah, GA",
    "49420": "Yakima, WA",
    "15500": "Burlington, NC",
    "16820": "Charlottesville, VA",
    "23540": "Gainesville, FL",
    "40980": "Saginaw, MI",
    "45940": "Trenton, NJ",
    "48700": "Williamsport, PA",
    "27900": "Joplin, MO",
    "44220": "Springfield, OH",
    "12980": "Battle Creek, MI",
    "19780": "Des Moines-West Des Moines, IA",
    "27980": "Kahului-Wailuku-Lahaina, HI",
    "40060": "Richmond, VA",
    "43300": "Sherman-Dennison, TX",
    "17020": "Chico, CA",
    "27340": "Jacksonville, NC",
    "13140": "Beaumont-Port Arthur, TX",
    "24860": "Greenville, SC",
    "15180": "Brownsville-Harlingen, TX",
    "34940": "Naples-Immokalee-Marco Island, FL",
    "43340": "Shreveport-Bossier City, LA",
    "20940": "El Centro, CA",
    "29200": "Lafayette-West Lafayette, IN",
    "33100": "Miami-Fort Lauderdale-West Palm Beach, FL",
    "43780": "South Bend-Mishawaka, IN-MI",
    "24540": "Greeley, CO",
    "33260": "Midland, TX",
    "37900": "Peoria, IL",
    "38900": "Portland-Vancouver-Hillsboro, OR-WA",
    "17300": "Clarksville, TN-KY",
    "36780": "Oshkosh-Neenah, WI",
    "47020": "Victoria, TX",
    "11100": "Amarillo, TX",
    "31340": "Lynchburg, VA",
    "41100": "Saint George, UT",
    "45780": "Toledo, OH",
    "23420": "Fresno, CA",
    "41540": "Salisbury, MD",
    "16540": "Chambersburg-Waynesboro, PA",
    "47300": "Visalia-Porterville, CA",
    "13980": "Blacksburg-Christiansburg-Radford, VA",
    "25940": "Hilton Head Island-Bluffton-Beaufort, SC",
    "39580": "Raleigh, NC",
    "16860": "Chattanooga, TN-GA",
    "44700": "Stockton, CA",
    "72400": "Burlington-South Burlington, VT",
    "46660": "Valdosta, GA",
    "16700": "Charleston-North Charleston, SC",
    "21660": "Eugene, OR",
    "26580": "Huntington-Ashland, WV-KY-OH",
    "38860": "Portland-South Portland, ME",
    "40900": "Sacramento--Arden-Arcade-Roseville, CA",
    "11460": "Ann Arbor, MI",
    "26900": "Indianapolis, IN",
    "33140": "Michigan City-La Porte, IN",
    "36420": "Oklahoma City, OK",
    "22020": "Fargo, ND-MN",
    "13780": "Binghamton, NY",
    "37980": "Philadelphia-Camden-Wilmington, PA-NJ-DE",
    "14020": "Bloomington, IN",
    "14460": "Boston-Cambridge-Newton, MA-NH",
    "17780": "College Station-Bryan, TX",
    "21140": "Elkhart-Goshen, IN",
    "27260": "Jacksonville, FL",
    "42220": "Santa Rosa-Petaluma, CA",
    "49620": "York, PA",
    "16740": "Charlotte-Concord-Gastonia, NC-SC",
    "31080": "Los Angeles-Long Beach-Anaheim, CA",
    "34060": "Morgantown, WV",
    "38220": "Pine Bluff, AR",
    "22140": "Farmington, NM",
    "24660": "Greensboro-High Point, NC",
    "29620": "Lansing-East Lansing, MI",
    "32900": "Merced, CA",
    "38300": "Pittsburgh, PA",
    "25860": "Hickory-Morganton-Lenoir, NC",
    "28940": "Knoxville, TN",
    "14740": "Bremerton-Silverdale, WA",
    "15940": "Canton-Massillon, OH",
    "38060": "Phoenix-Mesa-Scottsdale, AZ",
    "39900": "Reno-Sparks, NV",
    "13460": "Bend-Redmond, OR",
    "21780": "Evansville, IN-KY",
    "39540": "Racine, WI",
    "48140": "Wausau, WI",
    "16300": "Cedar Rapids, IA",
    "39820": "Redding, CA"
}
USHome = pd.DataFrame(locationdict.items())
USHome.columns = ['Code', 'Location']

temploc = USHome['Location'].str.split(',', expand=True)

USHome.insert(2, "City", temploc[0], True)
USHome.insert(3, "State", temploc[1], True)

tempCity = USHome['City'].str.split('-', expand=True)
tempState = USHome['State'].str.split('-', expand=True)

USHome['City'] = tempCity[0]
USHome['State'] = tempState[0]
USHome['State'] = USHome['State'].str.replace(' ', '')


print(USHome)
locales = []

for i in tqdm(USHome.index):
    call = "https://api.zippopotam.us/us/{0}/{1}".format((USHome.loc[i].at["State"]), (USHome.loc[i].at["City"]))
    locales.append(requests.get(call).text)

jsonLocales = [json.loads(i) for i in locales]
places = pd.DataFrame(jsonLocales)
print(places)

latList = []
logList = []

for i in USHome.index:
    temp = pd.DataFrame(places.loc[i, 'places'])
    tempLat = (temp.loc[0].at['latitude'])
    tempLog = (temp.loc[0].at['longitude'])
    logList.append(tempLat)
    latList.append(tempLog)


USHome['lat'] = logList  # when I ran my final table these two values got mixed up.  went back and looked and it makes
USHome['lon'] = latList  # no sense how they got swapped so I just flipped the variables names here.
print(USHome)

USHome.to_pickle("/Users/dpops/Library/CloudStorage/OneDrive-Facebook/School1/MBA/Tools for Data Analysis/location.pkl")

parent_country = {
      "163": "Russia",
      "501": "Australia",
      "414": "Egypt",
      "340": "St. Vincent and the Grenadines",
      "137": "Switzerland",
      "238": "Sri Lanka",
      "078": "U. S. Virgin Islands",
      "245": "United Arab Emirates",
      "313": "Guatemala",
      "523": "Tonga",
      "400": "Algeria",
      "362": "Brazil",
      "209": "Hong Kong",
      "248": "Yemen",
      "512": "Micronesia",
      "073": "Puerto Rico",
      "110": "Germany",
      "235": "Saudi Arabia",
      "364": "Columbia",
      "246": "Uzbekistan",
      "151": "Croatia",
      "155": "Estonia",
      "203": "Bhutan",
      "236": "Singapore",
      "457": "Uganda",
      "228": "Mongolia",
      "332": "Haiti",
      "106": "Denmark",
      "555": "Elsewhere",
      "130": "Azores",
      "149": "Slovakia",
      "311": "Costa Rica",
      "427": "Kenya",
      "429": "Liberia",
      "361": "Bolivia",
      "108": "Finland",
      "207": "China",
      "243": "Turkey",
      "156": "Latvia",
      "148": "Czech Republic",
      "343": "West Indies, not specified",
      "508": "Fiji",
      "407": "Cameroon",
      "217": "Korea",
      "511": "Marshall Islands",
      "372": "Uruguay",
      "449": "South Africa",
      "239": "Syria",
      "315": "Nicaragua",
      "138": "United Kingdom",
      "399": "Americas, not specified",
      "117": "Hungary",
      "329": "Dominican Republic",
      "233": "Philippines",
      "126": "Netherlands",
      "127": "Norway",
      "416": "Ethiopia",
      "370": "Peru",
      "150": "Bosnia & Herzegovina",
      "323": "Bahamas",
      "066": "Guam",
      "069": "Northern Marianas",
      "134": "Spain",
      "109": "France",
      "369": "Paraguay",
      "100": "Albania",
      "339": "St. Lucia",
      "104": "Bulgaria",
      "129": "Portugal",
      "301": "Canada",
      "166": "Europe, not specified",
      "105": "Czechoslovakia",
      "116": "Greece",
      "215": "Japan",
      "374": "South America, not specified",
      "321": "Antigua and Barbuda",
      "140": "Scotland",
      "448": "Somalia",
      "408": "Cape Verde",
      "060": "American Samoa",
      "460": "Zambia",
      "214": "Israel",
      "159": "Azerbaijan",
      "202": "Bangladesh",
      "314": "Honduras",
      "453": "Tanzania",
      "417": "Eritrea",
      "226": "Malaysia",
      "165": "USSR",
      "118": "Iceland",
      "316": "Panama",
      "247": "Vietnam",
      "162": "Moldova",
      "312": "El Salvador",
      "328": "Dominica",
      "324": "Barbados",
      "157": "Lithuania",
      "136": "Sweden",
      "154": "Serbia",
      "119": "Ireland",
      "120": "Italy",
      "454": "Togo",
      "224": "Lebanon",
      "158": "Armenia",
      "412": "Congo",
      "103": "Belgium",
      "139": "England",
      "142": "Northern Ireland",
      "210": "India",
      "327": "Cuba",
      "515": "New Zealand",
      "360": "Argentina",
      "222": "Kuwait",
      "161": "Georgia",
      "444": "Senegal",
      "462": "Africa, Not Specified",
      "147": "Yugoslavia",
      "211": "Indonesia",
      "436": "Morocco",
      "242": "Thailand",
      "160": "Belarus",
      "102": "Austria",
      "240": "Taiwan",
      "213": "Iraq",
      "430": "Libya",
      "216": "Jordan",
      "330": "Grenada",
      "303": "Mexico",
      "425": "Ivory Coast",
      "229": "Nepal",
      "447": "Sierra Leone",
      "373": "Venezuela",
      "152": "Macedonia",
      "421": "Ghana",
      "461": "Zimbabwe",
      "459": "Zaire",
      "128": "Poland",
      "440": "Nigeria",
      "368": "Guyana",
      "218": "Kazakhstan",
      "451": "Sudan",
      "231": "Pakistan",
      "206": "Cambodia",
      "057": "United States",
      "341": "Trinidad and Tobago",
      "527": "Samoa",
      "223": "Laos",
      "220": "South Korea",
      "205": "Myanmar (Burma)",
      "164": "Ukraine",
      "249": "Asia, not specified",
      "300": "Bermuda",
      "310": "Belize",
      "365": "Ecuador",
      "363": "Chile",
      "132": "Romania",
      "200": "Afghanistan",
      "212": "Iran",
      "338": "St. Kitts--Nevis",
      "333": "Jamaica",
      "168": "Montenegro",
      "423": "Guinea"
    }
mother_country_df = pd.DataFrame(parent_country.items())
mother_country_df.columns = ['Mother', 'Mother Country']

father_country_df = pd.DataFrame(parent_country.items())
father_country_df.columns = ['Father', 'Father Country']

api_data = pd.read_pickle("/Users/dpops/Library/CloudStorage/OneDrive-Facebook/School1/MBA/Tools for Data Analysis/api data.pkl")
location_data = pd.read_pickle("/Users/dpops/Library/CloudStorage/OneDrive-Facebook/School1/MBA/Tools for Data Analysis/location.pkl")



api_data.columns =['Mother', 'Father', 'Code', 'Year', 'Month']



combined_data = api_data.merge(location_data, how='inner', on='Code')
combined_data = combined_data.merge(father_country_df, how='inner', on='Father')
combined_data = combined_data.merge(mother_country_df, how='inner', on='Mother')





combined_data['Year'] = combined_data['Year'].astype(int)
print(combined_data)
# combined_data.to_pickle("/Users/dpops/Library/CloudStorage/OneDrive-Facebook/School1/MBA/Tools for Data Analysis/combined data.pkl")

combined_data['Year'] = combined_data['Year'].astype(int)

final_combined_data = combined_data.groupby(combined_data.columns.tolist(), as_index=False).size()

final_combined_data = final_combined_data.drop_duplicates()
final_combined_data.to_csv(
    "/Users/dpops/Library/CloudStorage/OneDrive-Facebook/School1/MBA/Tools for Data Analysis/final.csv")

pie_data = final_combined_data[['Father Country', 'Mother Country', 'Location', 'Year', 'size']]
print(pie_data)
pie_data = pie_data.rename(columns={'Father Country': 'Father_Country'})
pie_data = pie_data.rename(columns={'Mother Country': 'Mother_Country'})



app = Dash(__name__)


app.layout = html.Div([
    html.H4('Immigrant settling city based on home country'),
    dcc.Graph(id="graph"),
    html.P("Father's Country:"),
    dcc.Dropdown(id='father',
                 options=sorted([{'label': i, 'value': i} for i in pie_data.Father_Country.unique()], key = lambda x: x['label']),
                 value='Albania', clearable=False,
                 ),
    html.P("Mother Country:"),
    dcc.Dropdown(id='mother',
                 options=sorted([{'label': i, 'value': i} for i in pie_data.Mother_Country.unique()],
                                key=lambda x: x['label']),
                 value='Albania', clearable=False
                 ),
    html.P("January of Year:"),
    dcc.Dropdown(id='year',
                 options=sorted([{'label': i, 'value': i} for i in pie_data.Year.unique()],
                                key=lambda x: x['label']),
                 value=2009, clearable=False
                 ),

])


@app.callback(
    Output("graph", "figure"),
    Input("father", "value"),
    Input("mother", "value"),
    Input('year', "value"))

def generate_chart(father,mother, year):
    pie_list = []
    for i in pie_data.index:
        a = pie_data.loc[i].at['Father_Country']
        b = pie_data.loc[i].at['Mother_Country']
        c = int(pie_data.loc[i].at['Year'])
        if a == father and b == mother and c == year:
            d = pd.DataFrame(pie_data.loc[i])
            e = d.T
            f = e.to_dict('records')
            pie_list.append(f[0])

    df = pd.DataFrame(pie_list)
    fig = px.pie(df, values='size', names='Location', hole=.3, )
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    return fig


app.run_server(debug=True)
