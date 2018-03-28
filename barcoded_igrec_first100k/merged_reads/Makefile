include ../Makefile_vars

all:
	$(MAKE) merged_reads.fastq

merged_reads.fastq: /mnt/data/krista/rawdata/IgSeqBX1_S1_R1_001_first100k.fastq /mnt/data/krista/rawdata/IgSeqBX1_S1_R2_001_first100k.fastq $(BIN)/paired_read_merger
	$(BIN)/paired_read_merger \
	/mnt/data/krista/rawdata/IgSeqBX1_S1_R1_001_first100k.fastq \
	/mnt/data/krista/rawdata/IgSeqBX1_S1_R2_001_first100k.fastq \
	merged_reads.fastq

clean:
	$(RM) merged_reads.fastq
