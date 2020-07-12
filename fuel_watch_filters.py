def Brand():
    """Returns a dict of Brands available in fuelwatch @ 26/03/2020
    """

    Brand = {
        'FilterName': 'Brand',
        '7-Eleven': '29', 'BOC': '4', 'BP': '5', 'Better Choice': '3',
        'Caltex': '6', 'Caltex Woolworths': '19', 'Coles Express': '20',
        'Eagle': '24', 'FastFuel 24/7': '25', 'Gull': '7',
        'Independent': '15', 'Kleenheat': '8', 'Kwikfuel': '9',
        'Liberty': '10', 'Metro Petroleum': '30', 'Mobil': '11',
        'Peak': '13', 'Puma': '26', 'Shell': '14', 'United': '23',
        'Vibe': '27', 'WA Fuels': '31', 'Wesco': '16',
    }

    return Brand


def Day():
    """Returns a dict of Day options available in fuelwatch @ 26/03/2020
    """
    Day = {
        'FilterName': 'Day',
        'today': 'today',
        'today_tomorrow': 'today_tomorrow',
        'tomorrow': 'tomorrow',
        'yesterday': 'yesterday'}

    return Day


def Product():
    """Returns a dict of Products available in fuelwatch @ 26/03/2020
    """
    Product = {
        'FilterName': 'Product',
        'Unleaded': '1', 'Premium': '2', 'Diesel': '4',
        'LPG': '5', '98-RON': '6', 'E85': '10', 'Brand-diesel': '11'
    }
    return Product


def Region():
    """Returns a dict of Regions available in fuelwatch @ 26/03/2020
    """
    Region = {
        'FilterName': 'Region',
        'Albany': '15',
        'Augusta/Margaret River': '28', 'Boulder': '1',
        'Bridgetown/Greenbushes': '30', 'Broome': '2',
        'Bunbury': '16', 'Busselton (Shire)': '29',
        'Busselton (Townsite)': '3', 'Capel': '19', 'Carnarvon': '4',
        'Cataby': '33', 'Collie': '5', 'Coolgardie': '34',
        'Cunderdin': '35', 'Dalwallinu': '36', 'Dampier': '6',
        'Dardanup': '20', 'Denmark': '37', 'Derby': '38',
        'Dongara': '39', 'Donnybrook/Balingup': '31', 'Esperance': '7',
        'Exmouth': '40', 'Fitzroy Crossing': '41', 'Geraldton': '17',
        'Greenough': '21', 'Harvey': '22', 'Jurien': '42',
        'Kalgoorlie': '8', 'Kambalda': '43', 'Karratha': '9',
        'Kellerberrin': '44', 'Kojonup': '45', 'Kununurra': '10',
        'Mandurah': '18', 'Manjimup': '32', 'Meckering': '58',
        'Meekatharra': '46', 'Metro : East/Hills': '27',
        'Metro : North of River': '25', 'Metro : South of River': '26',
        'Moora': '47', 'Mt Barker': '48', 'Munglinup': '61',
        'Murray': '23', 'Narrogin': '11', 'Newman': '49',
        'Norseman': '50', 'North Bannister': '60', 'Northam': '12',
        'Port Hedland': '13', 'Ravensthorpe': '51', 'Regans Ford': '57',
        'South Hedland': '14', 'Tammin': '53', 'Waroona': '24',
        'Williams': '54', 'Wubin': '55', 'Wundowie': '59',
        'York': '56'
    }

    return Region


def StateRegion():
    """Returns a dict of State Regions available in fuelwatch @ 26/03/2020
    """

    StateRegion = {
        'FilterName': 'StateRegion',
        'Gascoyne': '1', 'Goldfields-Esperance': '2',
        'Great Southern': '3', 'Kimberley': '4',
        'Metro': '98', 'Mid-West': '5',
        'Peel': '6', 'Pilbara': '7',
        'South-West': '8', 'Wheatbelt': '9'
    }

    return StateRegion


def Suburb():
    """Returns a dict of Suburbs available in fuelwatch @ 26/03/2020
    """
    Suburb = {
         'FilterName': 'Suburb',
         'Albany': 'ALBANY', 'Alexander Heights': 'ALEXANDER HEIGHTS',
         'Alfred Cove': 'ALFRED COVE', 'Alkimos': 'ALKIMOS',
         'Applecross': 'APPLECROSS', 'Armadale': 'ARMADALE', 'Ascot': 'ASCOT',
         'Ashby': 'ASHBY', 'Attadale': 'ATTADALE', 'Augusta': 'AUGUSTA',
         'Australind': 'AUSTRALIND', 'Aveley': 'AVELEY',
         'Balcatta': 'BALCATTA', 'Baldivis': 'BALDIVIS',
         'Balga': 'BALGA', 'Balingup': 'BALINGUP', 'Ballajura': 'BALLAJURA',
         'Banksia Grove': 'BANKSIA GROVE', 'Barragup': 'BARRAGUP',
         'Baskerville': 'BASKERVILLE', 'Bassendean': 'BASSENDEAN',
         'Bayswater': 'BAYSWATER', 'Beckenham': 'BECKENHAM',
         'Bedfordale': 'BEDFORDALE', 'Beechboro': 'BEECHBORO',
         'Beeliar': 'BEELIAR', 'Beldon': 'BELDON', 'Bellevue': 'BELLEVUE',
         'Belmont': 'BELMONT', 'Bentley': 'BENTLEY', 'Bertram': 'BERTRAM',
         'Bibra Lake': 'BIBRA LAKE', 'Bicton': 'BICTON',
         'Binningup': 'BINNINGUP', 'Boulder': 'BOULDER', 'Boyanup': 'BOYANUP',
         'Brentwood': 'BRENTWOOD', 'Bridgetown': 'BRIDGETOWN',
         'Broadwater': 'BROADWATER', 'Broome': 'BROOME',
         'Brunswick': 'BRUNSWICK', 'Bull Creek': 'BULL CREEK',
         'Bullsbrook': 'BULLSBROOK', 'Bunbury': 'BUNBURY',
         'Burswood': 'BURSWOOD', 'Busselton': 'BUSSELTON',
         'Butler': 'BUTLER', 'Byford': 'BYFORD',
         'Canning Vale': 'CANNING VALE', 'Cannington': 'CANNINGTON',
         'Capel': 'CAPEL', 'Carbunup River': 'CARBUNUP RIVER',
         'Carine': 'CARINE', 'Carlisle': 'CARLISLE', 'Carnarvon': 'CARNARVON',
         'Cataby': 'CATABY', 'Caversham': 'CAVERSHAM', 'Chidlow': 'CHIDLOW',
         'Claremont': 'CLAREMONT', 'Clarkson': 'CLARKSON',
         'Cloverdale': 'CLOVERDALE', 'Cockburn Central': 'COCKBURN CENTRAL',
         'Collie': 'COLLIE', 'Como': 'COMO', 'Coolgardie': 'COOLGARDIE',
         'Coolup': 'COOLUP', 'Cowaramup': 'COWARAMUP',
         'Cunderdin': 'CUNDERDIN', 'Currambine': 'CURRAMBINE',
         'Dalwallinu': 'DALWALLINU', 'Dampier': 'DAMPIER',
         'Dardanup': 'DARDANUP', 'Dawesville': 'DAWESVILLE',
         'Dayton': 'DAYTON', 'Denmark': 'DENMARK', 'Derby': 'DERBY',
         'Dianella': 'DIANELLA', 'Dongara': 'DONGARA',
         'Donnybrook': 'DONNYBROOK', 'Doubleview': 'DOUBLEVIEW',
         'Duncraig': 'DUNCRAIG', 'Dunsborough': 'DUNSBOROUGH',
         'Dwellingup': 'DWELLINGUP', 'East Fremantle': 'EAST FREMANTLE',
         'East Perth': 'EAST PERTH', 'East Rockingham': 'EAST ROCKINGHAM',
         'East Victoria Park': 'EAST VICTORIA PARK', 'Eaton': 'EATON',
         'Edgewater': 'EDGEWATER', 'Ellenbrook': 'ELLENBROOK',
         'Embleton': 'EMBLETON', 'Erskine': 'ERSKINE',
         'Esperance': 'ESPERANCE', 'Exmouth': 'EXMOUTH', 'Falcon': 'FALCON',
         'Fitzroy Crossing': 'FITZROY CROSSING', 'Floreat': 'FLOREAT',
         'Forrestdale': 'FORRESTDALE', 'Forrestfield': 'FORRESTFIELD',
         'Fremantle': 'FREMANTLE', 'Gelorup': 'GELORUP',
         'Geraldton': 'GERALDTON', 'Gidgegannup': 'GIDGEGANNUP',
         'Girrawheen': 'GIRRAWHEEN', 'Glen Forrest': 'GLEN FORREST',
         'Glen Iris': 'GLEN IRIS', 'Glendalough': 'GLENDALOUGH',
         'Glenfield': 'GLENFIELD', 'Gnangara': 'GNANGARA',
         'Gosnells': 'GOSNELLS', 'Gracetown': 'GRACETOWN',
         'Greenbushes': 'GREENBUSHES', 'Greenfields': 'GREENFIELDS',
         'Greenough': 'GREENOUGH', 'Greenwood': 'GREENWOOD',
         'Guildford': 'GUILDFORD', 'Gwelup': 'GWELUP',
         'Halls Head': 'HALLS HEAD', 'Hamilton Hill': 'HAMILTON HILL',
         'Harrisdale': 'HARRISDALE', 'Harvey': 'HARVEY',
         'Henderson': 'HENDERSON', 'Henley Brook': 'HENLEY BROOK',
         'Herne Hill': 'HERNE HILL', 'High Wycombe': 'HIGH WYCOMBE',
         'Hillarys': 'HILLARYS', 'Huntingdale': 'HUNTINGDALE',
         'Innaloo': 'INNALOO', 'Jandakot': 'JANDAKOT',
         'Jarrahdale': 'JARRAHDALE', 'Jindalee': 'JINDALEE',
         'Jolimont': 'JOLIMONT', 'Joondalup': 'JOONDALUP',
         'Jurien Bay': 'JURIEN BAY', 'Kalamunda': 'KALAMUNDA',
         'Kalgoorlie': 'KALGOORLIE', 'Kambalda East': 'KAMBALDA EAST',
         'Karawara': 'KARAWARA', 'Kardinya': 'KARDINYA', 'Karnup': 'KARNUP',
         'Karragullen': 'KARRAGULLEN', 'Karratha': 'KARRATHA',
         'Karridale': 'KARRIDALE', 'Karrinyup': 'KARRINYUP',
         'Kellerberrin': 'KELLERBERRIN', 'Kelmscott': 'KELMSCOTT',
         'Kewdale': 'KEWDALE', 'Kiara': 'KIARA', 'Kingsley': 'KINGSLEY',
         'Kojonup': 'KOJONUP', 'Koondoola': 'KOONDOOLA',
         'Kununurra': 'KUNUNURRA', 'Kwinana Beach': 'KWINANA BEACH',
         'Kwinana Town Centre': 'KWINANA TOWN CENTRE',
         'Lakelands': 'LAKELANDS', 'Landsdale': 'LANDSDALE',
         'Langford': 'LANGFORD', 'Leda': 'LEDA',
         'Leederville': 'LEEDERVILLE', 'Leeming': 'LEEMING',
         'Lesmurdie': 'LESMURDIE', 'Lexia': 'LEXIA',
         'Lynwood': 'LYNWOOD', 'Maddington': 'MADDINGTON',
         'Madeley': 'MADELEY', 'Maida Vale': 'MAIDA VALE',
         'Malaga': 'MALAGA', 'Mandurah': 'MANDURAH', 'Manjimup': 'MANJIMUP',
         'Manning': 'MANNING', 'Manypeaks': 'MANYPEAKS',
         'Margaret River': 'MARGARET RIVER',
         'Meadow Springs': 'MEADOW SPRINGS', 'Meckering': 'MECKERING',
         'Meekatharra': 'MEEKATHARRA', 'Merriwa': 'MERRIWA',
         'Middle Swan': 'MIDDLE SWAN', 'Midvale': 'MIDVALE',
         'Mindarie': 'MINDARIE', 'Mirrabooka': 'MIRRABOOKA',
         'Moonyoonooka': 'MOONYOONOOKA', 'Moora': 'MOORA',
         'Morley': 'MORLEY', 'Mosman Park': 'MOSMAN PARK',
         'Mount Barker': 'MOUNT BARKER', 'Mt Helena': 'MT HELENA',
         'Mt Lawley': 'MT LAWLEY', 'Mt Pleasant': 'MT PLEASANT',
         'Mullaloo': 'MULLALOO', 'Mullewa': 'MULLEWA',
         'Mundaring': 'MUNDARING', 'Mundijong': 'MUNDIJONG',
         'Munglinup': 'MUNGLINUP', 'Munster': 'MUNSTER', 'Murdoch': 'MURDOCH',
         'Myalup': 'MYALUP', 'Myaree': 'MYAREE', 'Narngulu': 'NARNGULU',
         'Narrogin': 'NARROGIN', 'Naval Base': 'NAVAL BASE',
         'Nedlands': 'NEDLANDS', 'Neerabup': 'NEERABUP',
         'Newman': 'NEWMAN', 'Nollamara': 'NOLLAMARA', 'Noranda': 'NORANDA',
         'Norseman': 'NORSEMAN', 'North Bannister': 'NORTH BANNISTER',
         'North Dandalup': 'NORTH DANDALUP',
         'North Fremantle': 'NORTH FREMANTLE',
         'North Perth': 'NORTH PERTH', 'North Yunderup': 'NORTH YUNDERUP',
         'Northam': 'NORTHAM', 'Northbridge': 'NORTHBRIDGE',
         'Northcliffe': 'NORTHCLIFFE', 'Nowergup': 'NOWERGUP',
         'O Connor': 'O CONNOR', 'Ocean Reef': 'OCEAN REEF',
         'Osborne Park': 'OSBORNE PARK', 'Padbury': 'PADBURY',
         'Palmyra': 'PALMYRA', 'Pearsall': 'PEARSALL',
         'Pemberton': 'PEMBERTON', 'Perth': 'PERTH',
         'Picton': 'PICTON', 'Picton East': 'PICTON EAST',
         'Pinjarra': 'PINJARRA', 'Port Hedland': 'PORT HEDLAND',
         'Port Kennedy': 'PORT KENNEDY', 'Preston Beach': 'PRESTON BEACH',
         'Queens Park': 'QUEENS PARK', 'Quinns Rocks': 'QUINNS ROCKS',
         'Ravensthorpe': 'RAVENSTHORPE', 'Ravenswood': 'RAVENSWOOD',
         'Redcliffe': 'REDCLIFFE', 'Regans Ford': 'REGANS FORD',
         'Ridgewood': 'RIDGEWOOD', 'Riverton': 'RIVERTON',
         'Rivervale': 'RIVERVALE', 'Rockingham': 'ROCKINGHAM',
         'Roleystone': 'ROLEYSTONE', 'Rosa Brook': 'ROSA BROOK',
         'Safety Bay': 'SAFETY BAY', 'Sawyers Valley': 'SAWYERS VALLEY',
         'Scarborough': 'SCARBOROUGH', 'Secret Harbour': 'SECRET HARBOUR',
         'Serpentine': 'SERPENTINE', 'Seville Grove': 'SEVILLE GROVE',
         'Siesta Park': 'SIESTA PARK', 'Singleton': 'SINGLETON',
         'Sorrento': 'SORRENTO', 'South Fremantle': 'SOUTH FREMANTLE',
         'South Hedland': 'SOUTH HEDLAND', 'South Lake': 'SOUTH LAKE',
         'South Perth': 'SOUTH PERTH', 'South Yunderup': 'SOUTH YUNDERUP',
         'Southern River': 'SOUTHERN RIVER',
         'Spearwood': 'SPEARWOOD', 'Stratham': 'STRATHAM',
         'Stratton': 'STRATTON', 'Subiaco': 'SUBIACO', 'Success': 'SUCCESS',
         'Swan View': 'SWAN VIEW', 'Swanbourne': 'SWANBOURNE',
         'Tammin': 'TAMMIN', 'The Lakes': 'THE LAKES',
         'Thornlie': 'THORNLIE', 'Tuart Hill': 'TUART HILL',
         'Upper Swan': 'UPPER SWAN', 'Vasse': 'VASSE',
         'Victoria Park': 'VICTORIA PARK', 'Waikiki': 'WAIKIKI',
         'Walkaway': 'WALKAWAY', 'Walpole': 'WALPOLE',
         'Wangara': 'WANGARA', 'Wanneroo': 'WANNEROO', 'Warnbro': 'WARNBRO',
         'Waroona': 'WAROONA', 'Warwick': 'WARWICK', 'Waterloo': 'WATERLOO',
         'Wattle Grove': 'WATTLE GROVE', 'Wedgefield': 'WEDGEFIELD',
         'Wellstead': 'WELLSTEAD', 'Welshpool': 'WELSHPOOL',
         'Wembley': 'WEMBLEY', 'West Busselton': 'WEST BUSSELTON',
         'West Kalgoorlie': 'WEST KALGOORLIE',
         'West Perth': 'WEST PERTH', 'West Pinjarra': 'WEST PINJARRA',
         'West Swan': 'WEST SWAN', 'Westminster': 'WESTMINSTER',
         'Willetton': 'WILLETTON', 'Williams': 'WILLIAMS',
         'Witchcliffe': 'WITCHCLIFFE', 'Woodbridge': 'WOODBRIDGE',
         'Woodvale': 'WOODVALE', 'Wubin': 'WUBIN',
         'Wundowie': 'WUNDOWIE', 'Yanchep': 'YANCHEP',
         'Yangebup': 'YANGEBUP', 'Yokine': 'YOKINE', 'York': 'YORK',
         'Youngs Siding': 'YOUNGS SIDING'
         }

    return Suburb


def Surrounding():
    """Returns a dict of Surrounding options available in
    fuelwatch @ 26/03/2020
    """
    Surrounding = {
        'FilterName': 'Surrounding',
        'yes': 'yes',
        'no': 'no',
    }
    return Surrounding


def Sort_on():
    """Returns a dict of Sorting options available
    """
    Sort_on = {
         'Filtername': 'Sort_on ',
         "brand": "brand",
         "location": "location",
         "price": "price"
        }
    return Sort_on


def kwargs_keys():

    """Returns a list of available kwargs keys

    """
    keys = {
       'Filtername': 'kwargs_keys',
       'title': 'title',
       'title_detail': 'title_detail',
       'summary': 'summary',
       'summary_detail': 'summary_detail',
       'brand': 'brand',
       'updated': 'updated',
       'price': 'price',
       'trading-name': 'trading-name',
       'location': 'location',
       'address': 'address',
       'phone': 'phone',
       'latitude': 'latitude',
       'longitude': 'longitude',
        }
    return keys
