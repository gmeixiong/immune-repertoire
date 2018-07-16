# immune-repertoire
Immune repertoire sequencing

# Reflow workflows for bracer and tracer.

cd reflow/
reflow -cache off run tracer.rf -read1 [read1] -read2 [read2] -cell_name [cell name] -results_bucket s3://[bucket]



For batch run:

cd experiments/
cd tracer/

Fill out tracer_run.csv with appropriate information

reflow -cache off runbatch --reset
