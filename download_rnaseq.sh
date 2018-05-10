cd code
wget --output-document sratoolkit.tar.gz http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz
tar xzvf sratoolkit.tar.gz
sudo ln -s --force $PWD/sratoolkit.2.9.0-ubuntu64/bin/* /usr/local/bin

# Download SRA files from NCBI
sudo apt-get install --yes nodejs npm
sudo npm install -g n
sudo n stable
sudo npm install bionode-ncbi -g
#npm install bionode-sra -g
bionode-ncbi search bioproject PRJNA183192
bionode-ncbi download sra PRJNA183192 --pretty


# Change to mnt data and mkdir
cd /mnt/data/
mkdir rawdata
cd rawdata

cd /mnt/data/rawdata/sra/mnt/data/rnaseq/sra

# Extract SRA files to fastq in parallel
export CORES=16
# Suggested fastq-dump parameters: https://edwards.sdsu.edu/research/fastq-dump/
export FASTQ_DUMP_FLAGS='--outdir /mnt/data/fastq_dump_v1 --gzip --skip-technical  --readids --read-filter pass --dumpbase --split-3 --clip'
ls -1  /mnt/data/rawdata/sra/mnt/data/rnaseq/sra/*/*.sra | xargs -P ${CORES} -I{} bash -c "fastq-dump $FASTQ_DUMP_FLAGS {}"

# Suggested fastq-dump parameters: https://edwards.sdsu.edu/research/fastq-dump/
export FASTQ_DUMP_FLAGS='--outdir /mnt/data/fastq_dump_v2 --defline-seq '@$sn[_$rn]/$ri' --split-files'
ls -1  /mnt/data/rawdata/sra/mnt/data/rnaseq/sra/*/*.sra | xargs -P ${CORES} -I{} bash -c "fastq-dump $FASTQ_DUMP_FLAGS {}"


export FASTQ_DUMP_FLAGS='--outdir /mnt/data/fastq_dump_v3 --gzip --skip-technical  --readids --read-filter pass --dumpbase --clip --defline-seq '@$sn[_$rn]/$ri' --split-files'
ls -1  /mnt/data/rawdata/sra/mnt/data/rnaseq/sra/*/*.sra | xargs -P ${CORES} -I{} bash -c "fastq-dump $FASTQ_DUMP_FLAGS {}"

ls -1  /mnt/data/rawdata/sra/mnt/data/rnaseq/sra/*/*.sra | xargs -P ${CORES} -I{} bash -c "fastq-dump --outdir /mnt/data/fastq_dump_v4 --gzip --skip-technical  --readids --read-filter pass --dumpbase --clip --defline-seq '@$sn[_$rn]/$ri' --split-files {}"


## No xarg,