#!/usr/bin/env python3.6

import click
import shlex
import subprocess

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
    command = f'sudo /home/ubuntu/anaconda/envs/python2.7-env/bin/python2.7 ' \
              f'/home/ubuntu/ig_repertoire_constructor/barcoded_igrec.py ' \
              f'-1 {read1} ' \
              f'-2 {read2} ' \
              f'--output {output_folder} --loci IGH ' \
              f'> >(tee -a {output_folder}/stdout.txt) 2> ' \
              f'>(tee -a {output_folder}/stderr.txt >&2)'
    command = shlex.split(command)
    subprocess.Popen(command)


if __name__ == '__main__':
    cli()
