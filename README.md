# Slypheed2CSV

Convert Slypheed address book to a CSV file.

> :warning: **Software under heavy development**: This package is on early
> stages of development, please be very careful when trying to use it for
> backing up important information. **Keep always the original address book**
> exported by Slypheed in case something goes wrong. :warning:


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
