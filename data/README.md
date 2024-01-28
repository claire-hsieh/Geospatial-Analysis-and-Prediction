# Geospatial-Analysis-and-Prediction

- `sample.csv` is a sample data set of weather station data collected from the NOAA website

- `010010-99999-2024` is data gathered from the [NOAA database](https://www.ncei.noaa.gov/pub/data/noaa/)
	- 010010: USAF (US Air Force) identifier
	- 99999: WBAN (station identifier)
	- 2024: year
	
- `isd-history.txt` : contains USAF, WBAN, names, and various other information

- `ish-abbreviated.txt`: contains the abbreviations used in the database


# Data Processing Tools

- `data_processing.py` : contains function to convert pdf to csv
	- requirements: `tabula-py`

- `isd_display.py` : contains function to display raw data from NOAA database
	- requirements: `pandas`

- `download_data.py` : contains function to download data from NOAA database
	- requirements: `pandas`, `regex`, `urllib`, `beautifulsoup4`
	- usage:
		- `python3 download_data.py -a True` : download all data
		- `python3 download_data.py -y "2024"` : download data from 2024 
		- `python3 download_data.py -y "2020-2024"` : download data from 2020 to 2024