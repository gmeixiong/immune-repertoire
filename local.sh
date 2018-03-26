# Build AMI with aegea ami-e6c7cd9c


aegea launch --iam-role S3fromEC2 --ami-tags Name=czbiohub-miniconda -t m4.4xlarge  olgabot-igrec-m4
aegea ssh ubuntu@olgabot-igrec-m4
