from faker import Faker
import random

fake = Faker()

def generate_fake_vendors(n):
    countries = [
        "Afghanistan", "Åland Islands", "Albania", "Algeria", "American Samoa", "Andorra", "Angola",
        "Anguilla", "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia",
        "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
        "Belize", "Benin", "Bermuda", "Bhutan", "Bosnia and Herzegovina", "Botswana", "Brazil",
        "British Indian Ocean Territory", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon",
        "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China",
        "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Cook Islands",
        "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica",
        "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea",
        "Estonia", "Ethiopia", "Faroe Islands", "Fiji", "Finland", "France", "French Guiana", "Gabon",
        "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada",
        "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
        "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iraq", "Ireland",
        "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan",
        "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Latvia", "Lebanon", "Lesotho", "Liberia",
        "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia",
        "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius",
        "Mayotte", "Mexico", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique",
        "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Caledonia", "Nicaragua", "Niger",
        "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan",
        "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal",
        "Puerto Rico", "Qatar", "Romania", "Rwanda", "Réunion", "Saint Barthélemy", "Samoa",
        "San Marino", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
        "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "Spain", "Sri Lanka", "Sudan", "Suriname",
        "Svalbard and Jan Mayen", "Swaziland", "Sweden", "Switzerland", "Tajikistan", "Thailand",
        "Timor-Leste", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey",
        "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
        "Uruguay", "Uzbekistan", "Vanuatu", "Wallis and Futuna", "Yemen", "Zambia", "Zimbabwe",
        "Brunei", "Falkland Islands", "French Polynesia", "South Korea", "New Zealand", "Pitcairn Islands",
        "Saint Helena, Ascension and Tristan Da Cunha", "Saint Kitts and Nevis", "Saint Lucia",
        "Saint Martin", "Saint Pierre and Miquelon", "Saint Vincent and the Grenadines", "South Africa",
        "South Sudan", "South Georgia", "United Kingdom", "United States", "British Virgin Islands",
        "United States Virgin Islands", "Bolivia", "Congo", "DR Congo", "Vatican City", "Iran",
        "North Korea", "Laos", "Macau", "Macedonia", "Micronesia", "Moldova", "Palestine", "Russia",
        "Sao Tome and Príncipe", "Syria", "Taiwan", "Tanzania", "Venezuela", "Vietnam", "Ivory Coast"
    ]

    statuses = ["Active", "Disabled"]

    vendors = []
    for _ in range(n):
        vendor = {
            "country": random.choice(countries),
            "name": fake.name(),
            "balance": round(random.uniform(1000, 100000)),  # Balance between 1,000 and 100,000 with 2 decimals
            "status": random.choice(statuses),
            "description": fake.text(max_nb_chars=20)
        }
        vendors.append(vendor)
    return vendors

# Example usage:
vendors_to_create = generate_fake_vendors(2)
