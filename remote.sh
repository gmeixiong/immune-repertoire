cd ~/ && git clone https://github.com/olgabot/rcfiles && cp rcfiles/.* .
screen

conda create --yes -n python2.7-env python=2.7 biopython matplotlib scipy numpy pandas seaborn
source activate python2.7-env

sudo apt install cmake

git clone https://github.com/yana-safonova/ig_repertoire_constructor/
cd ig_repertoire_constructor
make
./igrec.py --test
./barcoded_igrec.py --test


# Get Cells labeled as "B cell" (or a child, e.g. "immature B cell") in MACA data
cd
git clone https://github.com/czbiohub/olgabot-aws-scratch/
cd ~/olgabot-aws-scratch
git checkout igrec
cd /mnt/data
cp ~/olgabot-aws-scratch/maca_bcell_or_children_ids.csv  .
