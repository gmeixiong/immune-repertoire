cd ~/ && git clone https://github.com/olgabot/rcfiles && cp rcfiles/.* .
screen

conda create --yes -n python2.7-env python=2.7 biopython matplotlib scipy numpy pandas seaborn
source activate python2.7-env
# Force linking of env python2
sudo ln -s /home/ubuntu/anaconda/envs/python2.7-env/bin/python2.7 /usr/bin/python2

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


cd /mnt/data
mkdir krista
cd krista
sudo aws s3 cp --recursive \
  s3://czbiohub-seqbot/fastqs/180128_M05295_0078_000000000-BJNBT .

DATA_DIR=/mnt/data/krista/rawdata


# Make subset of first 10k reads
sudo head -n 40000 $DATA_DIR/IgSeqBX1_S1_R1_001.fastq > $DATA_DIR/IgSeqBX1_S1_R1_001_first10k.fastq
sudo head -n 40000 $DATA_DIR/IgSeqBX1_S1_R2_001.fastq > $DATA_DIR/IgSeqBX1_S1_R2_001_first10k.fastq

./run_barcoded_igrec.py $DATA_DIR/IgSeqBX1_S1_R1_001_first10k.fastq \
    $DATA_DIR/IgSeqBX1_S1_R2_001_first10k.fastq barcoded_igrec_first10k

# Make subset of first 100k reads
sudo head -n 400000 $DATA_DIR/IgSeqBX1_S1_R1_001.fastq > $DATA_DIR/IgSeqBX1_S1_R1_001_first100k.fastq
sudo head -n 400000 $DATA_DIR/IgSeqBX1_S1_R2_001.fastq > $DATA_DIR/IgSeqBX1_S1_R2_001_first100k.fastq

./run_barcoded_igrec.py $DATA_DIR/IgSeqBX1_S1_R1_001_first100k.fastq \
    $DATA_DIR/IgSeqBX1_S1_R2_001_first100k.fastq barcoded_igrec_first100k

# Make subset of first 1 million reads
sudo head -n 4000000 $DATA_DIR/IgSeqBX1_S1_R1_001.fastq > $DATA_DIR/IgSeqBX1_S1_R1_001_first1M.fastq
sudo head -n 4000000 $DATA_DIR/IgSeqBX1_S1_R2_001.fastq > $DATA_DIR/IgSeqBX1_S1_R2_001_first1M.fastq

./run_barcoded_igrec.py $DATA_DIR/IgSeqBX1_S1_R1_001_first1M.fastq \
    $DATA_DIR/IgSeqBX1_S1_R2_001_first1M.fastq barcoded_igrec_first1M


source activate python2.7-env
/home/ubuntu/ig_repertoire_constructor/barcoded_igrec.py \
  -1 $DATA_DIR/IgSeqBX1_S1_R1_001.fastq -2 $DATA_DIR/IgSeqBX1_S1_R2_001.fastq \
  --output barcoded_igrec --loci 'all BCRs'
