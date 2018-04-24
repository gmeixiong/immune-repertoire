## On m4.10xlarge (160GB ram)

cd /mnt/data/krista/
mkdir fastq
cd fastq
aws s3 sync s3://olgabot-antibody/fastqs/BX1_underscore/ .
sudo /home/ubuntu/anaconda/envs/python2.7-env/bin/python2.7 /home/ubuntu/ig_repertoire_constructor/barcoded_igrec.py -1 /mnt/data/fastq/BX-R1_primers-pass_underscore_separated.fastq -2 /mnt/data/fastq/BX-R2_primers-pass_underscore_separated.fastq -o igrec_on_presto_primers_pass_underscore_separated_v2  -l IGH

