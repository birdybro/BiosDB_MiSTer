import json
import zipfile

with open('db.json', 'r') as file:
    data = json.load(file)

data['zips'] = {
    "neogeo_unibios": {
        "contents_file": {
            "hash": "1986c39676354d19ae648a914bd914f7",
            "size": 101498,
            "url": "http://unibios.free.fr/download/uni-bios-40.zip"
        },
        "description": "Extracting NeoGeo UniBios from http://unibios.free.fr",
        "files_count": 1,
        "folders_count": 0,
        "internal_summary": {
            "files": {
                "|games/NEOGEO/uni-bios.rom": {
                    "hash": "4f0aeda8d2d145f596826b62d563c4ef",
                    "size": 131072,
                    "tags": [
                        data['tag_dictionary']['bios'],
                        data['tag_dictionary']['games'],
                        data['tag_dictionary']['neogeo']
                    ],
                    "zip_id": "neogeo_unibios",
                    "zip_path": "uni-bios.rom"
                }
            },
            "folders": {}
        },
        "kind": "extract_single_files",
        "raw_files_size": 131072
    }
}

with open('bios_db.json', 'w') as output_file:
    json.dump(data, output_file)

with zipfile.ZipFile('bios_db.json.zip', 'w', zipfile.ZIP_DEFLATED) as zipped_file:
    zipped_file.writestr('bios_db.json', json.dumps(data))
