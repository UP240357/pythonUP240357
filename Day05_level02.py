# Day 5 lvl 2 - Lists  in Python
# Ruiz Clemente Jorge Alberto

""" 1
The following is a list of 10 students ages:
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
"""
"""1.1 Sort the list and find the min and max age"""
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)
ages.sort()
print(ages)
max_age = ages[-1]
min_age = ages[0]
print(f"Max = {min_age}")
print(f"Min = {max_age}")

"""1.2 Add the min age and the max age again to the list"""
ages.append(max_age)
ages.append(min_age)
print(ages)

"""1.3  Find the median age (one middle item or two middle items 
        divided by two)"""
ages.sort()

middle = (len(ages)+1)//2
print(f"Length = {len(ages)}")
print(f"middle = {ages[middle:middle+1]}")

"""1.4 Find the average age (sum of all items divided by their number )"""
average_age = (sum(ages))/len(ages)
print(average_age)

"""1.5 Find the range of the ages (max minus min)"""
print(f"Max     = {max_age}")
print(f"Min     = {min_age}")
print(f"Range   = {max_age-min_age}")

"""1.6  Compare the value of (min - average) and (max - average), use 
        abs() method"""
fts_comparation = min_age - average_age
snd_comparation = max_age - average_age

print(f"first comparation   = {fts_comparation}")
print(f"second comparation  = {snd_comparation}")
print(f"first comparation abs   = {abs(fts_comparation)}")
print(f"second comparation abs  = {abs(snd_comparation)}")

""" 2
Find the middle country(ies) in the countries list
"""
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
print(f"\n{countries}")
middle = (len(countries)+1)//2
print(f"length = {len(countries)}")
print(f"middle = {countries[middle:middle+1]}")

""" 3
Divide the countries list into two equal lists if it is 
even if not one more country for the first half.
"""
fst_half = countries[:middle]
snd_half = countries[middle:]
print(f"\nfirst half = {fst_half}\n\nsecond half = {snd_half}")

""" 4
['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 
'Denmark']. Unpack the first three countries and the rest
as scandic countries.
"""
countries_p2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
fst_countri, snd_countri, trh_countri, *rest_countries = countries_p2
print(f"1st = {fst_countri}\n2nd = {snd_countri}\n3th = {trh_countri}\nrest of countries = {rest_countries}")