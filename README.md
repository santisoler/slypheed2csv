# Slypheed2CSV

> ⚠️ Work in Progress! ⚠️

Convert Slypheed address book to a CSV file.

## How to install

Install `pip` using your package manager.

- On Ubuntu:
    ```
    sudo apt install python3-pip
    ```
- On Arch:
    ```
    sudo pacman -S python-pip
    ```

Then install the latest version of Slypheed2CSV:

```
pip install https://github.com/santisoler/slypheed2csv/archive/main.zip
```

Check your installation by running:

```
slypheed2csv
```

## How to use

Export the Slypheed address book into a XML file, for example
`addressbook.xml`.

Then use `slypheed2csv` to convert it to a CSV file:

```
slypheed2csv addressbook.xml -o address.csv
```

## License

[MIT](https://github.com/santisoler/slypheed2csv/blob/main/LICENSE)
