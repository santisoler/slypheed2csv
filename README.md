# Slypheed2CSV

Convert Slypheed address book to a CSV file.

> :warning: **Software under heavy development**: This package is on early
> stages of development, please be very careful when trying to use it for
> backing up important information. **Keep always the original address book**
> exported by Slypheed in case something goes wrong. :warning:


## How to install

### On Ubuntu

Install `pip` using your package manager:

```
sudo apt install python3-pip
```

Then install the latest version of Slypheed2CSV:

```
pip3 install https://github.com/santisoler/slypheed2csv/archive/main.zip
```

Check your installation by running:

```
slypheed2csv
```

#### Another way

If this didn't work for you (it didn't work for me on Xubuntu 18.04), try the
following:

1. Install `python3` through `apt`:
    ```
    sudo apt install python3
    ```
2. Download a zip file containing the latest version of this repository and
   unzip it:
    ```
    wget https://github.com/santisoler/slypheed2csv/archive/main.zip
    unzip main.zip
    ```
3. Change directory to the unzipped one and install `slypheed2csv` by actually
   running the `setup.py`:
    ```
    cd slypheed2csv-main
    sudo python3 setup.py install
    ```
4. Check your installation by running:
    ```
    slypheed2csv
    ```

### On Arch

Install `pip` using your package manager:

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
