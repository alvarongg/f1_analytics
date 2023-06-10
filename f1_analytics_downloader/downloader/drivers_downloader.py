
import click
from downloader import APIDataDownloader


class DriversDataDownloader(APIDataDownloader):
  def __init__(self, url, output_file,season):
        self.url = url.replace("season",season)
        self.output_file = output_file
        self.season = season

  def json_digger(self,json):
            return json['MRData']['DriverTable']['Drivers']
  

@click.command()
@click.option("--url", prompt="API URL", help="URL of the API")
@click.option("--output", prompt="Output CSV", help="Output CSV file name")
@click.option("--season", prompt="f1 season year", help="f1 season year")

def main(url, output,season):
    downloader = DriversDataDownloader(url, output,season)
    downloader.download_data()

#poetry run python ./downloader/drivers_downloader.py --url http://ergast.com/api/f1/season/drivers.json --output ../csv_files/drivers.csv --season 2023
if __name__ == "__main__":
    main()