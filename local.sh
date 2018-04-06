# Build AMI with aegea ami-e6c7cd9c


aegea launch --iam-role S3fromEC2 --ami-tags Name=czbiohub-miniconda -t m4.4xlarge  olgabot-igrec-m4
# aegea ssh ubuntu@olgabot-igrec-m4
ssh -i ~/.ssh/aegea.launch.olgabot.Olgas-MacBook-Pro.pem ubuntu@ec2-34-210-67-18.us-west-2.compute.amazonaws.com


## For running igrec on tabula muris fastqs
aegea launch --iam-role S3fromEC2 --ami-tags Name=czbiohub-miniconda -t m4.4xlarge  olgabot-igrec-tabula-muris
ssh -i ~/.ssh/aegea.launch.olgabot.Olgas-MacBook-Pro.pem ubuntu@ec2-35-166-114-251.us-west-2.compute.amazonaws.com
