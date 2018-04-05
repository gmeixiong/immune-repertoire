
import StringIO
import os

import click

import run_igrec


# Stolen from http://www.genomearchitecture.com/2014/01/how-to-gunzip-on-the-fly-with-python
class gzopen(object):
   """Generic opener that decompresses gzipped files
   if needed. Encapsulates an open file or a GzipFile.
   Use the same way you would use 'open()'.
   """
   def __init__(self, fname):
      f = open(fname)
      # Read magic number (the first 2 bytes) and rewind.
      magic_number = f.read(2)
      f.seek(0)
      # Encapsulated 'self.f' is a file or a GzipFile.
      if magic_number == '\x1f\x8b':
         self.f = gzip.GzipFile(fileobj=f)
      else:
         self.f = f

   # Define '__enter__' and '__exit__' to use in
   # 'with' blocks. Always close the file and the
   # GzipFile if applicable.
   def __enter__(self):
      return self
   def __exit__(self, type, value, traceback):
      try:
         self.f.fileobj.close()
      except AttributeError:
         pass
      finally:
         self.f.close()

   # Reproduce the interface of an open file
   # by encapsulation.
   def __getattr__(self, name):
      return getattr(self.f, name)
   def __iter__(self):
      return iter(self.f)
   def next(self):
      return next(self.f)


@click.command()
@click.argument('fastqs', nargs=-1)
@click.argument('output_prefix10')
@click.option('--barcoded', is_flag=True)
def cli(fastqs, output_prefix, barcoded):

    for fastq in fastqs:
        # Only operate on R1s to avoid duplication
        if "R2" in fastqs:
            continue
        read1 = fastq
        read2 = fastq.replace('_R1_', '_R2_')

        subfolder = os.path.basename(read1).split('.fastq')[0]
        output_folder = os.path.join(output_prefix, subfolder)

        run_igrec.cli(read1, read2, output_folder, barcoded)


if __name__ == '__main__':
    cli()
