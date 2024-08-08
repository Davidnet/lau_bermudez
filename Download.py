import requests
from pathlib import Path
url = "https://gist.github.com/slopp/ce3b90b9168f2f921784de84fa445651/raw/4ecf3041f0ed4913e7c230758733948bc561f434/penguins.csv"
response_object = requests.get(url)

assets_path = Path('assets')
assets_path.mkdir(parents=True, exist_ok=True)

# Crear la ruta completa para el archivo CSV
csv_file_path = assets_path / 'penguins.csv'
print(csv_file_path.as_posix())

# Guardar el contenido del CSV en un archivo
with csv_file_path.open('wb') as file:
    file.write(response_object.content)


