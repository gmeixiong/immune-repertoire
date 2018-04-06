
import StringIO
import os

import click

import run_igrec


@click.command()
@click.argument('fastqs', nargs=-1)
@click.argument('output_prefix')
@click.option('--barcoded', is_flag=True)
def cli(fastqs, output_prefix, barcoded):

    for fastq in fastqs:
        # Only operate on R1s to avoid duplication
        if "R2" in fastqs:
            continue
        read1 = fastq
        read2 = fastq.replace('_R1_', '_R2_')

        subfolder = os.path.basename(read1).split('_R1_')[0]
        output_folder = os.path.join(output_prefix, subfolder)

        run_igrec.cli(read1, read2, output_folder, barcoded)


if __name__ == '__main__':
    cli()
