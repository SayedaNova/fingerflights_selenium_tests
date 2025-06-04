import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.Demo_Data.update_vendor_data import generate_updated_vendor


def update_vendor(driver, original_vendor):

    updated_vendor = generate_updated_vendor(original_vendor)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

    time.sleep(3)

    # Find the row containing the user by email
    rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'hover:shadow-md')]")
    for row in rows:
        if original_vendor["name"] in row.text:
            edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/update/')]")
            edit_button.click()
            WebDriverWait(driver, 10).until(EC.url_contains("/vendor/update"))
            break
    else:
        raise Exception(f"❌ Could not find vendor with name: {original_vendor["name"]}")

    # --- ✅ Handle Country Dropdown
    country_mapping = {
        "Afghanistan": "1",
        "Åland Islands": "2",
        "Albania": "3",
        "Algeria": "4",
        "American Samoa": "5",
        "Andorra": "6",
        "Angola": "7",
        "Anguilla": "8",
        "Antarctica": "9",
        "Antigua and Barbuda": "10",
        "Argentina": "11",
        "Armenia": "12",
        "Aruba": "13",
        "Australia": "14",
        "Austria": "15",
        "Azerbaijan": "16",
        "Bahamas": "17",
        "Bahrain": "18",
        "Bangladesh": "19",
        "Barbados": "20",
        "Belarus": "21",
        "Belgium": "22",
        "Belize": "23",
        "Benin": "24",
        "Bermuda": "25",
        "Bhutan": "26",
        "Bosnia and Herzegovina": "27",
        "Botswana": "28",
        "Brazil": "29",
        "British Indian Ocean Territory": "30",
        "Bulgaria": "31",
        "Burkina Faso": "32",
        "Burundi": "33",
        "Cambodia": "34",
        "Cameroon": "35",
        "Canada": "36",
        "Cape Verde": "37",
        "Cayman Islands": "38",
        "Central African Republic": "39",
        "Chad": "40",
        "Chile": "41",
        "China": "42",
        "Christmas Island": "43",
        "Cocos (Keeling) Islands": "44",
        "Colombia": "45",
        "Comoros": "46",
        "Cook Islands": "47",
        "Costa Rica": "48",
        "Croatia": "49",
        "Cuba": "50",
        "Cyprus": "51",
        "Czech Republic": "52",
        "Denmark": "53",
        "Djibouti": "54",
        "Dominica": "55",
        "Dominican Republic": "56",
        "Ecuador": "57",
        "Egypt": "58",
        "El Salvador": "59",
        "Equatorial Guinea": "60",
        "Eritrea": "61",
        "Estonia": "62",
        "Ethiopia": "63",
        "Faroe Islands": "64",
        "Fiji": "65",
        "Finland": "66",
        "France": "67",
        "French Guiana": "68",
        "Gabon": "69",
        "Gambia": "70",
        "Georgia": "71",
        "Germany": "72",
        "Ghana": "73",
        "Gibraltar": "74",
        "Greece": "75",
        "Greenland": "76",
        "Grenada": "77",
        "Guadeloupe": "78",
        "Guam": "79",
        "Guatemala": "80",
        "Guernsey": "81",
        "Guinea": "82",
        "Guinea-Bissau": "83",
        "Guyana": "84",
        "Haiti": "85",
        "Honduras": "86",
        "Hong Kong": "87",
        "Hungary": "88",
        "Iceland": "89",
        "India": "90",
        "Indonesia": "91",
        "Iraq": "92",
        "Ireland": "93",
        "Isle of Man": "94",
        "Israel": "95",
        "Italy": "96",
        "Jamaica": "97",
        "Japan": "98",
        "Jersey": "99",
        "Jordan": "100",
        "Kazakhstan": "101",
        "Kenya": "102",
        "Kiribati": "103",
        "Kuwait": "104",
        "Kyrgyzstan": "105",
        "Latvia": "106",
        "Lebanon": "107",
        "Lesotho": "108",
        "Liberia": "109",
        "Libya": "110",
        "Liechtenstein": "111",
        "Lithuania": "112",
        "Luxembourg": "113",
        "Madagascar": "114",
        "Malawi": "115",
        "Malaysia": "116",
        "Maldives": "117",
        "Mali": "118",
        "Malta": "119",
        "Marshall Islands": "120",
        "Martinique": "121",
        "Mauritania": "122",
        "Mauritius": "123",
        "Mayotte": "124",
        "Mexico": "125",
        "Monaco": "126",
        "Mongolia": "127",
        "Montenegro": "128",
        "Montserrat": "129",
        "Morocco": "130",
        "Mozambique": "131",
        "Myanmar": "132",
        "Namibia": "133",
        "Nauru": "134",
        "Nepal": "135",
        "Netherlands": "136",
        "New Caledonia": "137",
        "Nicaragua": "138",
        "Niger": "139",
        "Nigeria": "140",
        "Niue": "141",
        "Norfolk Island": "142",
        "Northern Mariana Islands": "143",
        "Norway": "144",
        "Oman": "145",
        "Pakistan": "146",
        "Palau": "147",
        "Panama": "148",
        "Papua New Guinea": "149",
        "Paraguay": "150",
        "Peru": "151",
        "Philippines": "152",
        "Poland": "153",
        "Portugal": "154",
        "Puerto Rico": "155",
        "Qatar": "156",
        "Romania": "157",
        "Rwanda": "158",
        "Réunion": "159",
        "Saint Barthélemy": "160",
        "Samoa": "161",
        "San Marino": "162",
        "Saudi Arabia": "163",
        "Senegal": "164",
        "Serbia": "165",
        "Seychelles": "166",
        "Sierra Leone": "167",
        "Singapore": "168",
        "Slovakia": "169",
        "Slovenia": "170",
        "Solomon Islands": "171",
        "Somalia": "172",
        "Spain": "173",
        "Sri Lanka": "174",
        "Sudan": "175",
        "Suriname": "176",
        "Svalbard and Jan Mayen": "177",
        "Swaziland": "178",
        "Sweden": "179",
        "Switzerland": "180",
        "Tajikistan": "181",
        "Thailand": "182",
        "Timor-Leste": "183",
        "Togo": "184",
        "Tokelau": "185",
        "Tonga": "186",
        "Trinidad and Tobago": "187",
        "Tunisia": "188",
        "Turkey": "189",
        "Turkmenistan": "190",
        "Turks and Caicos Islands": "191",
        "Tuvalu": "192",
        "Uganda": "193",
        "Ukraine": "194",
        "United Arab Emirates": "195",
        "Uruguay": "196",
        "Uzbekistan": "197",
        "Vanuatu": "198",
        "Wallis and Futuna": "199",
        "Yemen": "200",
        "Zambia": "201",
        "Zimbabwe": "202",
        "Brunei": "203",
        "Falkland Islands": "204",
        "French Polynesia": "205",
        "South Korea": "206",
        "New Zealand": "207",
        "Pitcairn Islands": "208",
        "Saint Helena, Ascension and Tristan Da Cunha": "209",
        "Saint Kitts and Nevis": "210",
        "Saint Lucia": "211",
        "Saint Martin": "212",
        "Saint Pierre and Miquelon": "213",
        "Saint Vincent and the Grenadines": "214",
        "South Africa": "215",
        "South Sudan": "216",
        "South Georgia": "217",
        "United Kingdom": "218",
        "United States": "219",
        "British Virgin Islands": "220",
        "United States Virgin Islands": "221",
        "Bolivia": "222",
        "Congo": "223",
        "DR Congo": "224",
        "Vatican City": "225",
        "Iran": "226",
        "North Korea": "227",
        "Laos": "228",
        "Macau": "229",
        "Macedonia": "230",
        "Micronesia": "231",
        "Moldova": "232",
        "Palestine": "233",
        "Russia": "234",
        "Sao Tome and Príncipe": "235",
        "Syria": "236",
        "Taiwan": "237",
        "Tanzania": "238",
        "Venezuela": "239",
        "Vietnam": "240",
        "Ivory Coast": "241"
    }

    country_value = country_mapping.get(updated_vendor["country"])
    if not country_value:
        raise ValueError(f"❌ Unknown country '{updated_vendor['country']}' provided!")

    # Select the correct combobox button (e.g. first of multiple)
    country_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
        By.XPATH, "(//button[@role='combobox' and contains(@class, 'rounded-md')])[1]"
    )))
    country_button.click()

    # Set country via JavaScript (hidden select)
    driver.execute_script("""
        const select = document.querySelectorAll('select[aria-hidden="true"]')[0];
        if (select) {
            select.value = arguments[0];
            select.dispatchEvent(new Event('change', { bubbles: true }));
        }
    """, country_value)

    print(f"✅ Set country to: {updated_vendor['country']} (value='{country_value}')")

    # Close dropdown by sending Escape key
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.ESCAPE)
    time.sleep(2)

    # Fill the name and balance fields
    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "name").send_keys(updated_vendor["name"])
    driver.find_element(By.NAME, "balance").clear()
    driver.find_element(By.NAME, "balance").send_keys(str(updated_vendor["balance"]))

    # Set status radio button
    status_value = "1" if updated_vendor["status"].lower() == "active" else "0"
    status_button = driver.find_element(By.XPATH, f"//button[@role='radio' and @value='{status_value}']")
    driver.execute_script("arguments[0].click();", status_button)
    print(f"✅ Status set to: {updated_vendor['status']}")

    # Fill Description Field
    description_input = driver.find_element(By.ID, "description")
    description_input.clear()
    description_input.send_keys(updated_vendor["description"])

    try:
        submit_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((
            By.XPATH, "//button[@type='submit' and contains(text(), 'Submit')]"
        )))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit_button)
        time.sleep(0.5)

        if submit_button.is_displayed() and submit_button.is_enabled():
            driver.execute_script("arguments[0].click();", submit_button)
            print("✅ Form submitted via JavaScript click.")
        else:
            print("⚠️ Submit button found but not interactable. Trying JS click directly.")
            driver.execute_script("arguments[0].click();", submit_button)

        WebDriverWait(driver, 20).until(EC.url_contains("/vendor/list"))
        print("✅ Redirected to Vendor List after submission.")
        print(updated_vendor)
    except Exception as e:
        print(f"❌ Could not submit form or redirect failed: {e}")
