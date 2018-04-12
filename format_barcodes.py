"""
Formats pRESTO primer-pass_pair-pass.fastq barcodes for IgReC
"""

import re
import sys

from Bio import SeqIO
import click


def igrecify_barcode(record, read_number, pattern):
    r1_barcode, r2_barcode = re.findall(pattern, record.description)[0]

    barcode = r1_barcode if read_number == 1 else r2_barcode
    record.description = re.sub(pattern, f'BARCODE:{barcode}',
                                record.description)
    click.echo(record.description)
    return record


@click.command()
@click.argument('fastq', type=click.File())
@click.argument('read_number', type=click.IntRange(1, 2))
def cli(fastq, read_number):
    """Converts presto-barcoded fastqo to igrec-formatted"""

    click.echo(fastq)
    pattern = re.compile(
        'BARCODE=(?P<r1_barcode>[ACGT]+),(?P<r2_barcode>[ACGT]+)')
    reformatted_records = (igrecify_barcode(record, read_number, pattern)
                           for record in SeqIO.parse(fastq, "fastq"))

    SeqIO.write(reformatted_records, sys.stdout, 'fastq')



