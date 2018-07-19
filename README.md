# immune-repertoire
Immune repertoire sequencing


# Install Go and Reflow locally for local runs. 

https://golang.org/doc/install
https://github.com/grailbio/reflow

Run 'aws configure' and input credentials.

Run:

AWS_SDK_LOAD_CONFIG=1 reflow setup-ec2
AWS_SDK_LOAD_CONFIG=1 reflow setup-s3-repository czbiohub-reflow-quickstart-cache
AWS_SDK_LOAD_CONFIG=1 reflow setup-dynamodb-assoc czbiohub-reflow-quickstart

Then: 'export AWS_REGION=us-west-2'

# Or launch aegea instance with reflow installed. 

Run 'aws configure' and input your AWS credentials. 
Run 'aegea launch --iam-role S3fromEC2 --ami-tags Name=czbiohub-reflow -t t2.micro  [name]-reflow'
Run 'ssh ubuntu@[name]-reflow'

You may need to run 'aws configure' once again as well as 'ssh-keygen'.

From this machine, run:

AWS_SDK_LOAD_CONFIG=1 reflow setup-ec2
AWS_SDK_LOAD_CONFIG=1 reflow setup-s3-repository czbiohub-reflow-quickstart-cache
AWS_SDK_LOAD_CONFIG=1 reflow setup-dynamodb-assoc czbiohub-reflow-quickstart

Then: 'export AWS_REGION=us-west-2'

From outside this machine, make sure to transfer your files to the reflow machine. 'scp -r [this folder] ubuntu@[ec2 instance]:~/reflow'

# Reflow workflows for bracer and tracer.

cd reflow/

reflow -cache off run tracer.rf -read1 [read1] -read2 [read2] -cell_name [cell name] -results_bucket s3://[bucket]





# For batch run:


cd experiments/

cd tracer/


Fill out tracer_run.csv with appropriate information


reflow -cache off runbatch --reset
