# Check Dublikate File

If you process files every day and you need to delete duplicates, this script can make your life easier.
___
![](https://img.shields.io/badge/python-3.9-blueviolet)
![](https://img.shields.io/github/last-commit/OverPotter/RemoteImport?color=blueviolet)
![](https://img.shields.io/github/issues-pr/OverPotter/RemoteImport?color=blueviolet)
![](https://img.shields.io/github/forks/OverPotter/RemoteImport?style=social)
___
## Usage
After download create folders near with python file:
```bash
---Input
---log
---sha256
```
Upload the files to the Input folder and run the python file.

The script checks the contents of the files, it opens the file in bytes, its hash is calculated and compared with the hash in the database (sha256 folder), if the hashes match, the file is deleted and this information is recorded in the logs.
## Installation
Use the git to install remote import.
```bash
git clone https://github.com/OverPotter/CheackDublikate.git
```
___
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
___ 
## License
[MIT](https://choosealicense.com/licenses/mit/)