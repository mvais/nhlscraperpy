"""
	scrape_pbp.py
	~~~~~~~~~~~~~
	scrape_pbp.py scrapes the play by play information and returns it in a list
	of list format.

    Copyright: (C) 2016 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

from lxml import html

def scrape_pbp(pbp_html):

	tree = html.fromstring(pbp_html)

	rows = tree.xpath('//tr[@class="evenColor"]')
	cleaned_data = []

	for row in rows:
		columns = row.findall('td')
		data = [columns[0].text, columns[1].text,
				columns[2].text.replace('\xa0', ""),
		        columns[3].text, _clean_event(columns[4].text),
				columns[5].text.replace('\xa0', " ")]

		visit_players = _clean_player(columns[6].xpath('.//td/font'))
		home_players = _clean_player(columns[7].xpath('.//td/font'))

		cleaned_data.append(data + visit_players + home_players)

	return cleaned_data

def _clean_player(player_columns):
	""" Clean the player name """

	players = []

	for player in player_columns:
		player_name = player.xpath('./@title')[0].split('- ')[1]
		player_number = player.xpath('./text()')[0]

		players.append(player_name + ' ' + player_number)

	return players
