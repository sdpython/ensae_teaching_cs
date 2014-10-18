pandoc -t beamer $1 -V theme:Warsaw -o ./`basename $1 .txt`.pdf
