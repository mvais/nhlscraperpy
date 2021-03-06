"""
    constants.py
    ~~~~~~~~~~~~
    constants.py contains important constants used throughout the package.

    Copyright: (C) 2018 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

MODE = {

    'PRESEASON' : '1',
    'SEASON' : '2',
    'PLAYOFF' : '3'
}

FILES = {

    # {0} : YYYYZZZZ - YYYY (START_YEAR) - ZZZZ (END_YEAR)
    # {1} : XX (Game Type) (01 - 03)
    # {2} : WWWW (Game Number)
    'ROSTER' : 'http://www.nhl.com/scores/htmlreports/{0}/RO{1}{2}.HTM',
    'PBP' : 'http://www.nhl.com/scores/htmlreports/{0}/PL{1}{2}.HTM',
    'TOIV' : 'http://www.nhl.com/scores/htmlreports/{0}/TV{1}{2}.HTM',
    'TOIH' : 'http://www.nhl.com/scores/htmlreports/{0}/TH{1}{2}.HTM',

    # Contains easy to access information about players playing in games. Will
    # consider doing a full scraper based on JSON in the future.
    # {0} : YYYYXXZZZZ - YYYY (Year) - XX (Game Type) - ZZZZ (Game Number)
    'JSON' : 'https://statsapi.web.nhl.com/api/v1/game/{0}/feed/live'
}

SEASONS = {

    "2007" : "20072008",
    "2008" : "20082009",
    "2009" : "20092010",
    "2010" : "20102011",
    "2011" : "20112012",
    "2012" : "20122013",
    "2013" : "20132014",
    "2014" : "20142015",
    "2015" : "20152016",
    "2016" : "20162017",
    "2017" : "20172018"
}

TEAMS = {

    "ANA" : "Anaheim Ducks",
    "ARI" : "Arizona Coyotes",
    "BOS" : "Boston Bruins",
    "BUF" : "Buffalo Sabres",
    "CAR" : "Carolina Hurricanes",
    "CBJ" : "Columbus Blue Jackets",
    "CGY" : "Calgary Flames",
    "CHI" : "Chicago Blackhawks",
    "COL" : "Colorado Avalanche",
    "DAL" : "Dallas Stars",
    "DET" : "Detroit Red Wings",
    "EDM" : "Edmonton Oilers",
    "FLA" : "Florida Panthers",
    "LAK" : "Los Angeles Kings",
    "LVK" : "Las Vegas Knights",
    "MIN" : "Minnesota Wild",
    "MTL" : "Montreal Canadiens",
    "NJD" : "New Jersey Devil",
    "NSH" : "Nashville Predators",
    "NYI" : "New York Islanders",
    "NYR" : "New York Rangers",
    "OTT" : "Ottawa Senators",
    "PHI" : "Philadelphia Flyers",
    "PIT" : "Pittsburgh Penguins",
    "SJS" : "San Jose Sharks",
    "STL" : "St. Louis Blues",
    "TBL" : "Tampa Bay Lightning",
    "TOR" : "Toronto Maple Leafs",
    "VAN" : "Vancouver Canucks",
    "WPG" : "Winnipeg Jets",
    "WSH" : "Washington Capitals",
    "PHX" : "Phoenix Coyotes",
    "ATL" : "Atlanta Trashers"
}
