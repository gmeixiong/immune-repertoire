#!/bin/bash

sudo /home/ubuntu/anaconda/envs/python2.7-env/bin/python2.7 /home/ubuntu/ig_repertoire_constructor/barcoded_igrec.py \
     -1 /mnt/data/krista/rawdata/IgSeqBX1_S1_R1_001_first10k.fastq \
     -2 /mnt/data/krista/rawdata/IgSeqBX1_S1_R2_001_first10k.fastq \
     --output ~/olgabot-aws-scratch/barcoded_igrec_first10k --loci IGH \
     > >(tee -a barcoded_igrec_first10k.sh.out) 2> >(tee -a barcoded_igrec_first10k.sh.err >&2)


#sudo /home/ubuntu/anaconda/envs/python2.7-env/bin/python2.7 /home/ubuntu/ig_repertoire_constructor/barcoded_igrec.py \
#     -1 /mnt/data/krista/rawdata/IgSeqBX1_S1_R1_001.fastq \
#     -2 /mnt/data/krista/rawdata/IgSeqBX1_S1_R2_001.fastq \
#     --output /mnt/data/krista/barcoded_igrec --loci IGH \
#     > >(tee -a barcoded_igrec.sh.out) 2> >(tee -a barcoded_igrec.sh.err >&2)
