import tkinter as tk
from tkinter import ttk

parent = tk.Tk()

with open("GDP.txt", "r") as a:
    GDP = a.read()

with open("Population.txt", "r") as a:
    population = a.read()


def test():
    with open("Date Rate.txt", "r") as daterate:
        for line in daterate:
            if line.lower().__contains__(country.get().lower()):
                print(line)
                break


countries = ['Angola', 'Niger', 'Mali', 'Chad', 'Uganda', 'Zambia', 'Burundi', 'Malawi', 'Somalia', 'Liberia',
             'Mozambique', 'Afghanistan', 'Guinea-Bissau', 'Burkina Faso', 'South Sudan', 'Guinea', 'Ethiopia',
             'Sierra Leone', 'Tanzania', 'Nigeria', 'Cameroon', 'Benin', 'Sudan', 'Central African Republic',
             'Zimbabwe', 'Congo, Democratic Republic of the', 'Senegal', 'Timor-Leste', 'Congo, Republic of the',
             'Togo', 'Equatorial Guinea', 'Sao Tome and Principe', 'Madagascar', 'Gaza Strip', 'Ghana', "Cote d'Ivoire",
             'Iraq', 'Mauritania', 'Rwanda', 'Eritrea', 'Western Sahara', 'Egypt', 'Gambia, The', 'Yemen', 'Namibia',
             'Gabon', 'West Bank', 'Eswatini', 'Comoros', 'Guatemala', 'Solomon Islands', 'Lesotho', 'Marshall Islands',
             'Oman', 'Tuvalu', 'Jordan', 'Vanuatu', 'Philippines', 'Djibouti', 'Papua New Guinea', 'Laos', 'Nauru',
             'Belize', 'Tajikistan', 'Haiti', 'Kenya', 'Cambodia', 'Honduras', 'Tonga', 'Botswana', 'Bolivia',
             'Kyrgyzstan', 'Pakistan', 'Algeria', 'Kiribati', 'Syria', 'Samoa', 'South Africa', 'Cabo Verde',
             'Micronesia, Federated States of', 'Guam', 'Nepal', 'American Samoa', 'Dominican Republic', 'Turkmenistan',
             'Kuwait', 'Malaysia', 'India', 'Bangladesh', 'Venezuela', 'Fiji', 'Mongolia', 'Mexico', 'Israel', 'Burma',
             'Ecuador', 'Panama', 'Peru', 'Kazakhstan', 'Morocco', 'Nicaragua', 'Iran', 'Tunisia', 'Libya', 'Bhutan',
             'Brunei', 'Paraguay', 'Uzbekistan', 'Argentina', 'Jamaica', 'El Salvador', 'Maldives', 'Indonesia',
             'Colombia', 'Antigua and Barbuda', 'Saudi Arabia', 'Suriname', 'Guyana', 'Turkey', 'Azerbaijan',
             'Costa Rica', 'Grenada', 'Vietnam', 'Bahamas, The', 'Dominica', 'Northern Mariana Islands',
             'Turks and Caicos Islands', 'New Caledonia', 'Sri Lanka', 'Korea, North', 'Faroe Islands',
             'French Polynesia', 'Greenland', 'Lebanon', 'Brazil', 'Gibraltar', 'Ireland', 'Cook Islands', 'Curacao',
             'Iceland', 'Chile', 'Seychelles', 'Albania', 'Bahrain', 'New Zealand', 'Saint Lucia', 'Sint Maarten',
             'Saint Kitts and Nevis', 'Saint Vincent and the Grenadines', 'Uruguay', 'Wallis and Futuna', 'Mauritius',
             'Armenia', 'Jersey', 'Virgin Islands', 'Anguilla', 'United States', 'Aruba', 'Trinidad and Tobago',
             'Norway', 'China', 'France', 'Georgia', 'Sweden', 'Australia', 'Cayman Islands', 'United Kingdom',
             'Montenegro', 'Barbados', 'Luxembourg', 'Belgium', 'Bermuda', 'Palau', 'Cyprus', 'Moldova',
             'British Virgin Islands', 'Thailand', 'Denmark', 'Falkland Islands (Islas Malvinas)', 'Isle of Man',
             'Netherlands', 'Macedonia', 'Finland', 'Russia', 'Cuba', 'Montserrat', 'Switzerland', 'Liechtenstein',
             'Canada', 'Ukraine', 'Belarus', 'Malta', 'Estonia', 'Guernsey', 'Lithuania', 'United Arab Emirates',
             'Latvia', 'Slovakia', 'Austria', 'Qatar', 'Saint Helena, Ascension, and Tristan da Cunha', 'Poland',
             'Czechia', 'Slovenia', 'Spain', 'Hungary', 'Serbia', 'Croatia', 'Hong Kong', 'Bosnia and Herzegovina',
             'Romania', 'Singapore', 'Germany', 'San Marino', 'Bulgaria', 'Italy', 'Macau', 'Greece', 'Korea, South',
             'Portugal', 'Taiwan', 'Puerto Rico', 'Japan', 'Andorra', 'Saint Pierre and Miquelon', 'Monaco']
country = ttk.Combobox(master=parent)
country['options'] = countries
country.pack()
guess = ttk.Button(text="Retrieve", master=parent, width=10, command=test)
guess.pack()
country.focus_set()

parent.mainloop()
