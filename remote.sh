cd ~/ && git clone https://github.com/olgabot/rcfiles && cp rcfiles/.* .
screen

conda create --yes -n python2.7-env python=2.7 biopython matplotlib scipy numpy pandas seaborn
source activate python2.7-env

sudo apt install cmake

git clone https://github.com/yana-safonova/ig_repertoire_constructor/
cd ig_repertoire_constructor
make
