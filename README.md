# BraCeR and TraCeR
Immune repertoire sequencing reflow workflows using BraCeR and TraCeR pipelines from https://github.com/teichlab. These pipelines reconstruct B and T cell receptor sequences using single-cell RNAseq data. You can find more info on each at https://github.com/Teichlab/tracer and https://github.com/Teichlab/bracer.

# Setup Reflow locally or through packer image to run

## Local

Install go and reflow:
https://golang.org/doc/install
https://github.com/grailbio/reflow

Remember to 'go build' the go/src/github.com/grailbio/reflow/cmd/reflow directory.

After reflow is successfuly installed and built, configure to the czbiohub ec2 security group and s3 cache. If you do not have aws command line, download from here: https://docs.aws.amazon.com/cli/latest/userguide/installing.html. Make sure you have czbiohub permissions to create s3 buckets and dynamodbs or the configuration will not work. Contact james.webber@czbiohub.org for permissions questions.

```
aws configure
AWS_SDK_LOAD_CONFIG=1 reflow setup-ec2
AWS_SDK_LOAD_CONFIG=1 reflow setup-s3-repository czbiohub-reflow-quickstart-cache
AWS_SDK_LOAD_CONFIG=1 reflow setup-dynamodb-assoc czbiohub-reflow-quickstart
export AWS_REGION=us-west-2
```

## Aegea instance with packer image
```
aegea launch --iam-role S3fromEC2 --ami-tags Name=czbiohub-reflow -t t2.micro  [name]-reflow
aegea ssh ubuntu@[name]-reflow
aws configure
```

You may need to move your key pair pem file to ~/.ssh/ before launching or run ssh-keygen if you cannot find the pem file. 

```
AWS_SDK_LOAD_CONFIG=1 reflow setup-ec2
AWS_SDK_LOAD_CONFIG=1 reflow setup-s3-repository czbiohub-reflow-quickstart-cache
AWS_SDK_LOAD_CONFIG=1 reflow setup-dynamodb-assoc czbiohub-reflow-quickstart
export AWS_REGION=us-west-2
```

# Workflow Input
```
reflow run [bt]racer.rf -read1 [read1] -read2 [read2] -cell_name [cell name] -results_bucket s3://[bucket]
```
read1 and read2 are fastq files corresponding to R1 and R2 from a paired-end sequencing read. These files can be s3 files ("s3://[bucket]/path/to/file.fastq") or local files. 

If you're running on an aegea instance, make sure to transfer your files to the ec2 machine. 

```
scp -r [this github folder] ubuntu@[ec2 instance]:~/reflow
scp -r [fastq folder] ubuntu@[ec2 instance]:~/reflow
```

cell name can be any name used for identifying the experiment. Results will use the cell name to save data to the s3 bucket. 

# Use Case
## Single Runs
Assuming reflow is properly installed and configured and your fastq folders are in s3 or stored locally:
```
cd reflow/
reflow [-cache off] run [bt]racer.rf -read1 <read1> -read2 <read2> -cell_name <cell name> -results_bucket <s3://bucket>
``` 

Results are saved under s3://results_bucket/cell_name/tracer or s3://results_bucket/cell_name/bracer.

## Batch Runs
Use a batch run to run multiple [bt]racer experiments at once. Reflow will instantiate an ec2 instance for each run, and they run in parallel.

Modify experiments/tracer_batch/tracer_run.csv with the desired data. reid dictates the run ID that reflow will use for logs. The other columns are the same inputs you would use for a single run. After filling out a row for each desired run, cd to the tracer_batch directory.

```
cd experiments/
cd tracer_batch/
reflow -cache off runbatch --reset
```
Results will be saved at the s3 bucket under the given cell name. 

# Questions
If you have questions or comments, contact gerry.meixiong@czbiohub.org
