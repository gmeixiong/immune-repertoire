package main

import (
  "io"
  "github.com/biogo/biogo/io/seqio/fastq"
  "os"
  "github.com/biogo/biogo/seq/linear"
  "github.com/biogo/biogo/alphabet"
  "fmt"
  "github.com/biogo/biogo/io/seqio/fasta"
  "regexp"
)

func main() {
  // Open the fastq file specified on the command line
  // for reading:
  fh, err := os.Open(os.Args[1])
  // Check for open errors and abort:
  if err != nil {
	panic(err)
  }

  // Create a template sequence for the reader:
  template := linear.NewQSeq("", alphabet.QLetters{}, alphabet.DNA, alphabet.Sanger)
  // Create a fastq reader:
  reader := fastq.NewReader(fh, template)


  // Open the output file for writing:
  fho, err := os.Create(os.Args[2])
  // Close the file after we finished writing:
  defer fho.Close()
  if err != nil {
	panic(err)
  }

  pattern := regexp.Compile("BARCODE=(?P<r1_barcode>[ACGT]+),(?P<r2_barcode>[ACGT]+)")

  // Create a fasta writer with width 80:
  writer := fasta.NewWriter(fho, 80)

  for {
	// Read the next record:
	seq, err := reader.Read()
	// Break loop if we reached the end of the file:
	if err == io.EOF {
	  break
	}
	fmt.Println(seq.CloneAnnotation().Desc)

	// -1 means return all found
	findall := pattern.FindAllString(seq.CloneAnnotation().Desc, -1)
	fmt.Println(findall)

	writer.Write(seq)
  }
}
