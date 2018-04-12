package main

import (
  "io"
  "github.com/biogo/biogo/io/seqio/fastq"
  "os"
  "github.com/biogo/biogo/seq/linear"
  "github.com/biogo/biogo/alphabet"
  "fmt"
  "regexp"
  "strconv"
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

  // convert string argument to number
  read_number, err := strconv.Atoi(os.Args[2])
  if err != nil {
	panic(err)
  }

  // Open the output file for writing:
  fho, err := os.Create(os.Args[3])
  // Close the file after we finished writing:
  defer fho.Close()
  if err != nil {
	panic(err)
  }

  pattern := regexp.MustCompile("BARCODE=(?P<r1_barcode>[ACGT]+),(?P<r2_barcode>[ACGT]+)")

  // Create a fasta writer with width 80:
  writer := fastq.NewWriter(fho)

  for {
	// Read the next record:
	seq, err := reader.Read()
	// Break loop if we reached the end of the file:
	if err == io.EOF {
	  break
	}

	description := seq.CloneAnnotation().Desc
	fmt.Println("---", description, "---")

	// -1 means return all found
	findall := pattern.FindAllStringSubmatch(description, -1)[0]

	fmt.Println("findall:", findall)
	fmt.Println("findall[0]:", findall[0])
	fmt.Println("findall[1]:", findall[1])
	fmt.Println("findall[2]:", findall[2])

	replaced := pattern.ReplaceAllString(description, "BARCODE:" + findall[read_number])

	fmt.Println("replaced:", replaced)

	writer.Write(seq)
  }
}
