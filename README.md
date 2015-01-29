# tsv2md
Tab separated values to markdown filter.

## Install
    Consider using virtualenv(wrapper).

    git clone https://github.com/wouteroostervld/tsv2md.git
    cd tsv2md
    pip install .

## Upgrade

    cd tsv2md
    git pull
    pip install --upgrade .

## Example

    tsv2md ~/Downloads/SOME.tsv | pandoc -s -r markdown -t html >SOME.html
