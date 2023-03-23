import requests
from bs4 import BeautifulSoup
import re
import datetime



def crawl(url):
	# Alle HTML-Infos der Website abrufen
	start_date = 'not found'
	end_date = 'not found'
	# Speichere die Webseite in eine Variable
	page_link = url
	page_response = requests.get(page_link, timeout=5)
	# Parse die Webseite mit BeautifulSoup
	soup = BeautifulSoup(page_response.content, "html.parser")
	# Definiere das Datumsformat der Webseite
	date_format = '%d.%m.%Y'
	# Definiere das Datumsformat für die SQL-Datenbank
	sql_date_format = '%Y-%m-%d'
	# Erstelle eine leere Liste für die zukünftigen Termine
	future_dates = []
	# Suche alle DIVs auf der Webseite
	divs = soup.find_all('div')
	# Gehe durch jeden DIV
	for div in divs:
		# Suche nach einem Datumsstring
		date_string = div.text
		# Prüfe, ob ein Datumsstring gefunden wurde
		if re.search(r'\d{1,2}\.\d{1,2}\.\d{4}', date_string):
			# Konvertiere den Datumsstring
			try:
				date = datetime.strptime(date_string, date_format).date()
				# Prüfe, ob der Termin in der Zukunft liegt
				if date > datetime.now().date():
					# Speichere den Termin in der Liste
					future_dates.append((date_string, date.strftime(sql_date_format)))
			except ValueError:
				# Konvertiere den Datumsstring
				try:
					date = datetime.strptime(date_string, '%d. %B %Y').date()
					# Prüfe, ob der Termin in der Zukunft liegt
					if date > datetime.now().date():
						# Speichere den Termin in der Liste
						future_dates.append((date_string, date.strftime(sql_date_format)))
				except ValueError:
					# Konvertiere den Datumsstring
					try:
						date = datetime.strptime(date_string, '%Y/%m/%d').date()
						# Prüfe, ob der Termin in der Zukunft liegt
						if date > datetime.now().date():
							# Speichere den Termin in der Liste
							future_dates.append((date_string, date.strftime(sql_date_format)))
					except ValueError:
						pass
	# Gehe durch die Liste mit den zukünftigen Terminen
	for date in future_dates:
		# Gib die Originalzeile und das konvertierte Datum aus
		start_date = date[0]
	return {'divtext': 'div.text', 'start_date': start_date, 'end_date': end_date, 'url': url}
