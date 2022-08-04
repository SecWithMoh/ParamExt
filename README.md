# Description

Since I didn’t find any offline tool to extract the query strings parameters of a URL, I decided to write such a tool. This tool extracts the existing parameters in a URL.

## Requirements

1.	You need GNU\Linux in order to use this tool.
2.	Install Unfurl, which is a great tool written by TomNomNom. You can find the instruction about how to install this tool from this URL: `https://github.com/tomnomnom/unfurl`
3.	Install Python 3.7.





## Installation


```bash
sudo apt update

sudo apt install python3.8

sudo apt install golang-go

go get -u github.com/tomnomnom/unfurl

git clone https://github.com/SecWithMoh/ParamExt.git

cd ParamExt

python3 ParamExt.py

```

## Usage

```bash
python3 ParamExt.py archive.txt results.txt
```

Here `archive.txt` is the input file which contains the result URLs of different tools such as WaybackURl, etc.
`results.txt` is the output file, which can be named by the user and it will contain the final output of ParamExt.


## Output:

After running this tool, you will have 3 `.txt` files as output:

`Query.txt` : contain unfurl output

`Output.txt` : contains the raw output of the processed inputs (it is not unique)

`Trash.txt` : contains junk parameters

The final output file name can be defined by the user. For example , in this example command:

```bash
python3 ParamExt.py archive.txt results.txt
```
The `results.txt` is the final output file, which is named by the user.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
