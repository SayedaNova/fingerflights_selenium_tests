from faker import Faker
import random
from datetime import datetime, timedelta, date
fake = Faker()
def generate_fake_leads(n):
    sources = ["Phone Call", "Facebook", "Reference", "Repeat Customer", "Walking", "Friends & Family", "B2B",
               "Man Power"]
    statuses = ["Lead", "Ongoing", "Negotiating", "Booking Done", "Wating For Final Confirmation", "Won", "Closed"]

    leads = []
    for _ in range(n):
        closing_date = date.today() + timedelta(days=random.randint(1, 60))
        lead = {
            "phone": "01" + str(random.randint(300000000, 999999999)),
            "name": fake.name(),
            "email": fake.unique.email(),
            "potentiality": random.randint(1, 5),
            "source": random.choice(sources),
            "status": random.choice(statuses),
            # "division": division,
            # "district": district,
            # "upazila": upazila,
            "address": fake.address().replace("\n", ", "),
            "description": fake.text(max_nb_chars=20),
            "closing_date": closing_date.strftime('%B %d, %Y')
        }
        leads.append(lead)

    return leads
# Example usage
leads_to_create = generate_fake_leads(n=2)

# from faker import Faker
# import random
# from datetime import datetime, timedelta
#
# fake = Faker()
#
# def generate_fake_leads(n):
#     sources = ["Phone Call", "Facebook", "Reference", "Repeat Customer", "Walking", "Friends & Family", "B2B", "Man Power"]
#     statuses = ["Lead", "Ongoing", "Negotiating", "Booking Done", "Wating For Final Confirmation", "Won", "Closed"]
#     # divisions = {
#     #     "Dhaka": {
#     #         "districts": {
#     #             "Dhaka": {
#     #                 "upazilas": [
#     #                     "Dhamrai" , "Dohar" , "Keraniganj" , "Nawabganj" , "Savar" ,"Bangshal" , "Chakbazar" , "Demra" ,
#     #                     "Dhanmondi" , "Gendaria" ,"Hazaribag" , "Jatrabari" , "Kadamtali" , "Kalabagan" , "Kamrangichar" ,
#     #                     "Khilgaon" , "Kotwali" , "Lalbag" , "Motijheel" , "Mugda" ,"Newmarket" , "Paltan" , "Ramna" ,
#     #                     "Sabujbag" , "Shahjahanpur" , "Shahbag" , "Shyampur" , "Shere Bangla Nagar" , "Sutrapur" , "Wari" ,
#     #                     "Adabar" , "Badda" , "Bimanbandar" , "Banani" , "Cantonment" , "Dakkhinkhan" , "Darussalam" , "Bhasantek" ,
#     #                     "Bhatara" , "Gulshan" , "Hatirjheel" , "Kafrul" , "Khilkhet" , "Mirpur" , "Mohammadpur" ,"Pallabi" ,"Rampura" ,
#     #                     "Rupnagar" , "Shah Ali" , "Tejgaon" , "Tejgaon Shilpa Elaka" ,"Turag" , "Uttra Pashchim" , "Uttara Purba" , "Uttarkhan"
#     #                 ]
#     #             },
#     #
#     #             "Faridpur": {
#     #                 "upazilas": [
#     #                     "Alfadanga", "Bhanga", "Boalmari", "Char Bhadrasan", "Faridpur Sadar", "Madhukhali", "Nagarkanda", "Sadarpur", "Saltha"
#     #                 ]
#     #             },
#     #
#     #             "Gazipur": {
#     #                 "upazilas": [
#     #                     "Basan" , "Gachha" , "Gazipur Sadar" , "Kaliakair" , "Kaliganj" ,  "Kapasia" ,  "Kashimpur" , "Konabari" , "Pubail" ,
#     #                     "Sadar" , "Sreepur" , "Tongi Pashchim" , "Tongi Purba"
#     #                 ]
#     #             },
#     #
#     #             "Gopalganj": {
#     #                 "upazilas": [
#     #                     "Gopalganj Sadar", "Kashiani", "Kotalipara", "Muksudpur", "Tungipara"
#     #                 ]
#     #             },
#     #
#     #             "Kishoreganj": {
#     #                 "upazilas": [
#     #                     "Austagram", "Bajitpur", "Bhairab", "Hossainpur", "Itna", "Karimganj", "Katiadi",
#     #                     "Kishoreganj Sadar", "Kuliarchar", "Mithamain", "Nikli", "Pakundia", "Tarail"
#     #                 ]
#     #             },
#     #
#     #             "Madaripur": {
#     #                 "upazilas": [
#     #                     "Kalkini", "Madaripur Sadar", "Rajoir", "Shibchar"
#     #                 ]
#     #             },
#     #
#     #             "Manikganj": {
#     #                 "upazilas": [
#     #                     "Daulatpur", "Ghior", "Harirampur", "Manikganj Sadar", "Saturia", "Shibalay", "Singair"
#     #                 ]
#     #             },
#     #
#     #             "Munshiganj": {
#     #                 "upazilas": [
#     #                     "Gazaria", "Louhajang", "Munshiganj Sadar", "Sirajdikhan", "Sreenagar", "Tongibari"
#     #                 ]
#     #             },
#     #
#     #             "Narayanganj": {
#     #                 "upazilas": [
#     #                     "Araihazar", "Sonargaon", "Bandar", "Narayanganj Sadar", "Rupganj"
#     #                 ]
#     #             },
#     #
#     #             "Narsingdi": {
#     #                 "upazilas": [
#     #                     "Belabo", "Manohardi", "Narsingdi Sadar", "Palash", "Raipura", "Shibpur"
#     #                 ]
#     #             },
#     #
#     #             "Rajbari": {
#     #                 "upazilas": [
#     #                     "Baliakandi", "Goalanda", "Kalukhali", "Pangsha", "Rajbari Sadar"
#     #                 ]
#     #             },
#     #
#     #             "Shariatpur": {
#     #                 "upazilas": [
#     #                     "Bhedarganj", "Damudya", "Gosairhat", "Naria", "Shariatpur Sadar", "Zajira"
#     #                 ]
#     #             },
#     #
#     #             "Tangail": {
#     #                 "upazilas": [
#     #                     "Basail", "Bhuanpur", "Delduar", "Dhanbari", "Ghatail", "Gopalpur", "Kalihati", "Madhupur", "Mirzapur","Nagarpur", "Sakhipur", "Tangail Sadar"
#     #                 ]
#     #             }
#     #         }
#     #     },
#     #
#     #     "Chattagram": {
#     #         "districts": {
#     #             "Cox's Bazar": {
#     #                 "upazilas": [
#     #                     "Chakaria", "Coxs Bazar Sadar", "Kutubdia", "Maheshkhali", "Pekua", "Ramu", "Teknaf", "Ukhia"
#     #                 ]
#     #             },
#     #
#     #             "Chattogram": {
#     #                 "upazilas": [
#     #                     "Akbarshah", "Anwara", "Bayejid Bostami", "Banshkhali", "Bakalia", "Boalkhali",
#     #                     "Chalk Bazar", "Chandanaish", "Chandgaon", "Chattogram Port", "Doublemooring", "Epz",
#     #                     "Fatikchhari", "Halishahar", "Hathazari", "Karnaphuli", "Kotwali", "Khulshi", "Lohagara",
#     #                     "Mirsarai", "Pahartali", "Panchlaish", "Patiya", "Patenga", "Rangunia", "Raozan",
#     #                     "Sadarghat", "Sandwip", "Satkania", "Sitakunda"
#     #                 ]
#     #             },
#     #
#     #             "Bandarban": {
#     #                 "upazilas": [
#     #                     "Alikadam", "Bandarban Sadar", "Lama", "Naikkhongchhari", "Rowangchhari", "Ruma","Thanchi"
#     #                 ]
#     #             },
#     #
#     #             "Brahmanbaria": {
#     #                 "upazilas": [
#     #                     "Akhaura", "Banchharampur", "Bijoynagar", "Brahmanbaria Sadar", "Ashuganj", "Kasba","Nabinagar", "Nasirnagar", "Sarail"
#     #                 ]
#     #             },
#     #
#     #             "Chandpur": {
#     #                 "upazilas": [
#     #                     "Chandpur Sadar", "Faridganj", "Haimchar", "Hajiganj", "Kachua", "Matlab Dakkhin","Matlab Uttar", "Shahrasti"
#     #                 ]
#     #             },
#     #
#     #             "Coxs Bazar": {
#     #                 "upazilas": [
#     #                     "Chakaria", "Coxs Bazar Sadar", "Kutubdia", "Maheshkhali", "Pekua", "Ramu", "Teknaf", "Ukhia"
#     #                 ]
#     #             },
#     #
#     #             "Feni": {
#     #                 "upazilas": [
#     #                     "Chhagalnaiya", "Daganbhuiyan", "Feni Sadar", "Fulgazi", "Parashuram", "Sonagazi"
#     #                 ]
#     #             },
#     #
#     #             "Khagrachhari": {
#     #                 "upazilas": [
#     #                     "Dighinala", "Guimara", "Khagrachhari Sadar", "Lakkhichhari", "Mahalchhari",
#     #                     "Manikchhari", "Matiranga", "Panchhari", "Ramgarh"
#     #                 ]
#     #             },
#     #
#     #             "Lakshmipur": {
#     #                 "upazilas": [
#     #                     "Kamalnagar", "Lakshmipur Sadar", "Raipur", "Ramganj", "Ramgati"
#     #                 ]
#     #             },
#     #
#     #             "Noakhali": {
#     #                 "upazilas": [
#     #                     "Begumganj", "Chatkhil", "Companiganj", "Hatiya", "Kabirhat", "Senbag", "Sonaimuri","Subarnachar", "Noakhali Sadar"
#     #                     ]
#     #             },
#     #
#     #             "Rangamati": {
#     #                 "upazilas": [
#     #                     "Baghaichhari", "Barkal", "Kawkhali", "Belaichhari", "Kaptai", "Jurachhari", "Langadu",
#     #                     "Naniarchar", "Rajasthali", "Rangamati Sadar"
#     #                 ]
#     #             },
#     #
#     #             "Comilla": {
#     #                 "upazilas": [
#     #                     "Barura", "Brahmanpara", "Burichang", "Chandina", "Chauddagram", "Sadar Dakkhin",
#     #                     "Daudkandi", "Debidwar", "Homna", "Adarsha Sadar", "Laksam", "Lalmai", "Manoharganj",
#     #                     "Meghna", "Muradnagar", "Nangalkot", "Titas"
#     #                 ]
#     #             }
#     #         }
#     #     },
#     #
#     #     "Khulna": {
#     #         "districts":{
#     #             "Bagerhat": {
#     #                 "upazilas": [
#     #                     "Bagerhat Sadar", "Chitalmari", "Fakirhat", "Kachua", "Mollahat", "Mongla", "Morelganj","Rampal", "Sharankhola"
#     #                 ]
#     #             },
#     #
#     #             "Chuadanga": {
#     #                 "upazilas": [
#     #                     "Alamdanga", "Chuadanga Sadar", "Damurhuda", "Jibannagar"
#     #                 ]
#     #             },
#     #
#     #             "Jashore": {
#     #                 "upazilas": [
#     #                     "Abhaynagar", "Bagharpara", "Chaugachha", "Jhikargachha", "Keshabpur", "Jashore Sadar","Manirampur", "Sharsha"
#     #                 ]
#     #             },
#     #
#     #             "Jhenaidah": {
#     #                 "upazilas": [
#     #                     "Harinakundu", "Jhenaidah Sadar", "Kaliganj", "Kotchandpur", "Maheshpur", "Shailkupa"
#     #                 ]
#     #             },
#     #
#     #             "Khulna": {
#     #                 "upazilas": [
#     #                     "Batiaghata", "Dacope", "Daulatpur", "Dumuria", "Dighalia", "Khalishpur", "Khan Jahan Ali",
#     #                     "Khulna Sadar", "Koyra", "Paikgachha", "Phultala", "Rupsa", "Sonadanga", "Terokhada"
#     #                 ]
#     #             },
#     #
#     #             "Kushtia": {
#     #                 "upazilas": [
#     #                     "Bheramara", "Daulatpur", "Khoksa", "Kumarkhali", "Kushtia Sadar", "Mirpur"
#     #                 ]
#     #             },
#     #
#     #             "Magura": {
#     #                 "upazilas": [
#     #                     "Magura Sadar", "Mohammadpur", "Shalikha", "Sreepur"
#     #                 ]
#     #             },
#     #
#     #             "Meherpur": {
#     #                 "upazilas": [
#     #                     "Gangni", "Mujibnagar", "Meherpur Sadar"
#     #                 ]
#     #             },
#     #
#     #             "Narail": {
#     #                 "upazilas": [
#     #                     "Kalia", "Lohagara", "Narail Sadar"
#     #                 ]
#     #             },
#     #
#     #             "Satkhira": {
#     #                 "upazilas": [
#     #                     "Ashashuni", "Debhata", "Kalaroa", "Kaliganj", "Satkhira Sadar", "Shyamnagar", "Tala"
#     #                 ]
#     #             }
#     #         }
#     #     },
#     #
#     #     "Mymensingh": {
#     #         "districts": {
#     #             "Jamalpur": {
#     #                 "upazilas": [
#     #                     "Bakshiganj", "Dewanganj", "Islampur", "Jamalpur Sadar", "Madarganj", "Melandaha", "Sarishabari"
#     #                 ]
#     #             },
#     #
#     #             "Mymensingh": {
#     #                 "upazilas": [
#     #                     "Bhaluka", "Dhobaura", "Fulbaria", "Gafargaon", "Gouripur", "Haluaghat", "Ishwarganj",
#     #                     "Mymensingh Sadar", "Muktagachha", "Nandail", "Fulpur", "Tarakanda", "Trishal"]
#     #                 },
#     #
#     #             "Netrakona": {
#     #                 "upazilas": [
#     #                     "Atpara", "Barhatta", "Durgapur", "Khaliajuri", "Kalmakanda", "Kendua", "Madan", "Mohanganj","Netrakona Sadar", "Purbadhala"
#     #                 ]
#     #             },
#     #
#     #             "Sherpur": {
#     #                 "upazilas": [
#     #                     "Jhenaigati", "Nakla", "Nalitabari", "Sherpur Sadar", "Sreebardi"
#     #                 ]
#     #             }
#     #         }
#     #     },
#     #
#     #     "Rajshahi": {
#     #         "districts": {
#     #             "Bogura": {
#     #                 "upazilas": [
#     #                     "Adamdighi", "Bogura Sadar", "Dhunat", "Dupchachia", "Gabtali", "Kahaloo", "Nandigram",
#     #                     "Sariakandi", "Shajahanpur", "Sherpur", "Shibganj", "Sonatala"
#     #                 ]
#     #             },
#     #
#     #             "Joypurhat": {
#     #                 "upazilas": [
#     #                     "Akkelpur", "Joypurhat Sadar", "Kalai", "Khetlal", "Panchbibi"
#     #                 ]
#     #             },
#     #
#     #             "Naogaon": {
#     #                 "upazilas": [
#     #                     "Atrai", "Badalgachhi", "Dhamoirhat", "Manda", "Mahadebpur", "Naogaon Sadar", "Niamatpur","Patnitala", "Porsha", "Raninagar", "Sapahar"
#     #                 ]
#     #             },
#     #             "Natore": {
#     #                 "upazilas": [
#     #                     "Bagatipara", "Baraigram", "Gurudaspur", "Lalpur", "Naldanga", "Natore Sadar", "Singra"
#     #                 ]
#     #             },
#     #
#     #             "Chapainababganj": {
#     #                 "upazilas": [
#     #                     "Bholahat", "Gomastapur", "Nachole", "Chapainawabganj Sadar", "Shibganj"
#     #                 ]
#     #             },
#     #
#     #             "Pabna": {
#     #                 "upazilas": [
#     #                     "Atgharia", "Bera", "Bhangura", "Chatmohar", "Faridpur", "Ishwardi", "Pabna Sadar", "Santhia","Sujanagar"
#     #                 ]
#     #             },
#     #
#     #             "Rajshahi": {
#     #                 "upazilas": [
#     #                     "Bagha", "Bagmara", "Boalia", "Chandrima", "Charghat", "Durgapur", "Godagari", "Kashiadanga",
#     #                     "Matihar", "Mohanpur", "Paba", "Puthia", "Rajpara", "Shah Makhdum", "Tanore"
#     #                 ]
#     #             },
#     #
#     #             "Sirajganj": {
#     #                 "upazilas": [
#     #                     "Belkuchi", "Chouhali", "Kamarkhanda", "Kazipur", "Rayganj", "Shahjadpur", "Sirajganj Sadar", "Tarash", "Ullapara"
#     #                 ]
#     #             }
#     #         }
#     #     },
#     #
#     #     "Rangpur": {
#     #         "districts": {
#     #             "Dinajpur": {
#     #                 "upazilas": [
#     #                     "Birampur", "Birganj", "Birol", "Bochaganj", "Chirirbandar", "Fulbari", "Ghoraghat",
#     #                     "Hakimpur", "Kaharole", "Khansama", "Dinajpur Sadar", "Nababganj", "Parbatipur"
#     #                 ]
#     #             },
#     #
#     #             "Gaibandha": {
#     #                 "upazilas": [
#     #                     "Fulchhari", "Gaibandha Sadar", "Gobindaganj", "Palashbari", "Sadullapur", "Saghata","Sundarganj"
#     #                 ]
#     #             },
#     #
#     #             "Kurigram": {
#     #                 "upazilas": [
#     #                     "Bhurungamari", "Rajibpur", "Chilmari", "Phulbari", "Kurigram Sadar", "Nageshwari", "Rajarhat","Roumari", "Ulipur"
#     #                 ]
#     #             },
#     #
#     #             "Lalmonirhat": {
#     #                 "upazilas": [
#     #                     "Aditmari", "Hatibandha", "Kaliganj", "Lalmonirhat Sadar", "Patgram"
#     #                 ]
#     #             },
#     #
#     #             "Nilphamari": {
#     #                 "upazilas": [
#     #                     "Dimla", "Domar", "Jaldhaka", "Kishoreganj", "Nilphamari Sadar", "Saidpur"
#     #                 ]
#     #             },
#     #
#     #             "Panchagarh": {
#     #                 "upazilas": [
#     #                     "Atowari", "Boda", "Debiganj", "Panchagarh Sadar", "Tentulia"
#     #                 ]
#     #             },
#     #
#     #             "Rangpur": {
#     #                 "upazilas": [
#     #                     "Badarganj", "Gangachara", "Kaunia", "Rangpur Sadar", "Mithapukur", "Pirgachha", "Pirganj","Taraganj"
#     #                 ]
#     #             },
#     #
#     #             "Thakurgaon": {
#     #                 "upazilas": [
#     #                     "Baliadangi", "Haripur", "Pirganj", "Ranishankail", "Thakurgaon Sadar"
#     #                 ]
#     #             }
#     #         }
#     #     },
#     #
#     #     "Sylhet": {
#     #         "districts": {
#     #             "Habiganj": {
#     #                 "upazilas": [
#     #                     "Ajmiriganj", "Bahubal", "Baniachong", "Chunarughat", "Habiganj Sadar", "Lakhai", "Madhabpur","Nabiganj", "Shayestaganj"
#     #                 ]
#     #             },
#     #
#     #             "Moulvibazar": {
#     #                 "upazilas": [
#     #                     "Baralekha", "Juri", "Kamalganj", "Kulaura", "Moulvibazar Sadar", "Rajnagar", "Sreemangal"
#     #                 ]
#     #             },
#     #
#     #             "Sunamganj": {
#     #                 "upazilas": [
#     #                     "Bishwambharpur", "Chhatak", "Dakkhin Sunamganj", "Derai", "Dharmapasha", "Dowarabazar","Jagannathpur", "Jamalganj", "Shalla", "Sunamganj Sadar", "Tahirpur"
#     #                 ]
#     #             },
#     #
#     #             "Sylhet": {
#     #                 "upazilas": [
#     #                     "Airport", "Balaganj", "Beanibazar", "Bishwanath", "Companiganj", "Dakkhin Surma", "Fenchuganj","Golapganj", "Gowainghat", "Jalalabad", "Jaintapur",
#     #                     "Kotwali", "Moglabazar", "Kanaighat", "Osmaninagar", "Sylhet Sadar", "Shahparan", "Zakiganj"
#     #                 ]
#     #             }
#     #         }
#     #     },
#     #
#     #     "Barisal": {
#     #         "districts": {
#     #             "Barguna": {
#     #                 "upazilas": [
#     #                     "Amtali", "Bamna", "Barguna Sadar", "Betagi", "Patharghata", "Taltali"
#     #                 ]
#     #             },
#     #
#     #             "Barishal": {
#     #                 "upazilas": [
#     #                     "Agailjhara", "Babuganj", "Bakerganj", "Banaripara", "Gaurnadi", "Hijla","Barishal Sadar (kotwali)", "Mehendiganj", "Muladi", "Ujirpur",
#     #                     "Barishal Sadar(kaownia)","Barishal Sadar(airport)"
#     #                 ]
#     #             },
#     #
#     #             "Bhola": {
#     #                 "upazilas": [
#     #                     "Bhola Sadar", "Borhanuddin", "Charfasson", "Daulatkhan", "Lalmohan", "Monpura", "Tazumuddin"
#     #                 ]
#     #             },
#     #
#     #             "Jhalokati": {
#     #                 "upazilas": [
#     #                     "Jhalokathi Sadar", "Kanthalia", "Nalchhity", "Rajapur"
#     #                 ]
#     #             },
#     #
#     #             "Patuakhali": {
#     #                 "upazilas": [
#     #                     "Bauphal", "Dashmina", "Dumki", "Galachipa", "Kalapara", "Mirzaganj", "Patuakhali Sadar","Rangabali"
#     #                 ]
#     #             },
#     #
#     #             "Pirojpur": {
#     #                 "upazilas": [
#     #                     "Bhandaria", "Kawkhali", "Mathbaria", "Nazirpur", "Pirojpur Sadar", "Nesarabad (swarupkathi)","Indurkani"
#     #                 ]
#     #             }
#     #         },
#     #     }
#     # }
#
