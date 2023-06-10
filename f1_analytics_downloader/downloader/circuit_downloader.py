import click
from downloader import APIDataDownloader


class CircuitDataDownloader(APIDataDownloader):
  def __init__(self, url, output_file,season):
        self.url = url.replace("season",season)
        self.output_file = output_file
        self.season = season
 
  def json_digger(self,json):
            return json['MRData']['RaceTable']['Races']
  
#   def custom_transformation(self,data): 
#             data[0].update({'id_season': self.season})
#             data[0].update({'id_round': self.round})
#             return data
  

@click.command()
@click.option("--url", prompt="API URL", help="URL of the API")
@click.option("--output", prompt="Output CSV", help="Output CSV file name")
@click.option("--season", prompt="f1 season year", help="f1 season year")

def main(url, output,season):
    downloader = CircuitDataDownloader(url, output,season)
    downloader.download_data()

#http://ergast.com/api/f1/2023.json

# poetry run python ./downloader/circuit_downloader.py --url http://ergast.com/api/f1/season.json --output ../csv_files/circuit.csv --season 2023 
if __name__ == "__main__":
    main()