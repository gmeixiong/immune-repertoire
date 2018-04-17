"""
Formats pRESTO primer-pass_pair-pass.fastq barcodes for IgReC
"""

import datetime
import re
import sys

from Bio import SeqIO
import click


def igrecify_barcode(record, read_number, pattern):
    r1_barcode, r2_barcode = re.findall(pattern, record.description)[0]

    barcode = r1_barcode if read_number == 1 else r2_barcode
    record.description = re.sub(pattern, f'BARCODE:{barcode}',
                                record.description)
    # print(record.description)
    return record


def timestamp():
    return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


@click.command()
@click.argument('fastq', type=click.File())
@click.argument('read_number', type=click.IntRange(1, 2))
@click.option('--time', is_flag=True)
def cli(fastq, read_number, time):
    """Converts presto-barcoded fastqo to igrec-formatted"""

    # print(fastq)
    if time:
        click.echo(timestamp(), err=True)
    pattern = re.compile(
        'BARCODE=(?P<r1_barcode>[ACGTN]+),(?P<r2_barcode>[ACGTN]+)')
    reformatted_records = (igrecify_barcode(record, read_number, pattern)
                           for record in SeqIO.parse(fastq, "fastq"))
    SeqIO.write(reformatted_records, sys.stdout, 'fastq')
    if time:
        click.echo(timestamp(), err=True)


if __name__ == '__main__':
    cli()
