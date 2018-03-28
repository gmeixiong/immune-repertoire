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


@click.command()
@click.argument('read1')
@click.argument('read2')
@click.argument('output_folder')
def cli(read1, read2, output_folder):
    os.path.mkdirs(output_folder)

    command = f'sudo /home/ubuntu/anaconda/envs/python2.7-env/bin/python2.7 ' \
              f'/home/ubuntu/ig_repertoire_constructor/barcoded_igrec.py ' \
              f'-1 {read1} ' \
              f'-2 {read2} ' \
              f'--output {output_folder} --loci IGH '
    command = shlex.split(command)

    stdout = f'{output_folder}/stdout.txt'
    stderr = f'{output_folder}/stde4r.txt'

    with open(stdout, 'w') as file_out:
        with open(stderr, 'w') as file_err:
            subprocess.Popen(command, stdout=file_out, stderr=file_err)


if __name__ == '__main__':
    cli()
