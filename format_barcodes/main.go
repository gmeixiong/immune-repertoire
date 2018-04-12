package format_barcodes

import (
  "io"
  "github.com/biogo/biogo/io/seqio/fastq"
  "os"
  "github.com/biogo/biogo/seq/linear"
  "github.com/biogo/biogo/alphabet"
  "fmt"
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

  for {
	// Read the next record:
	seq, err := reader.Read()
	// Break loop if we reached the end of the file:
	if err == io.EOF {
	  break
	}
	fmt.Println(seq.CloneAnnotation().Desc)
  }
}
