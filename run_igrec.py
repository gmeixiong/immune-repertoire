#!/usr/bin/env python3.6

import os
import shlex
import subprocess

import click

"""
May need to set "locales" for Unicode because ASCII is stupid.

e.g. for a ENglish, US machine:

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
"""

def maybe_make_directory(folder):
    try:
        os.makedirs(folder)
    except OSError:
        pass


def run_igrec(read1, read2, output_folder, barcoded=False):
    maybe_make_directory(output_folder)

    if barcoded:
        igrec = '/home/ubuntu/ig_repertoire_constructor/barcoded_igrec.py'
    else:
        igrec = '/home/ubuntu/ig_repertoire_constructor/igrec.py'

    command = ['sudo',
               '/home/ubuntu/anaconda/envs/python2.7-env/bin/python2.7 ',
               igrec,
              f'-1 $(gunzip -c {read1}) ',
              f'-2 $(gunzip -c {read2}) ',
              f'--output {output_folder} ',
               '--loci IGH ']
    # command = shlex.split(command)

    stdout = f'{output_folder}/stdout.txt'
    stderr = f'{output_folder}/stderr.txt'

    with open(stdout, 'w') as file_out:
        with open(stderr, 'w') as file_err:
            subprocess.Popen(command, stdout=file_out, stderr=file_err)

@click.command()
@click.argument('read1')
@click.argument('read2')
@click.argument('output_folder')
@click.option('--barcoded', is_flag=True)
def cli(read1, read2, output_folder, barcoded):
    run_igrec(read1, read2, output_folder, barcoded)


if __name__ == '__main__':
    cli()
