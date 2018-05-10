package main

import (
  "github.com/biogo/biogo/io/seqio/fastq"
  "os"
  "github.com/biogo/biogo/seq/linear"
  "github.com/biogo/biogo/alphabet"
  "regexp"
  "strconv"
  "strings"
  "github.com/biogo/biogo/io/seqio"
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
  sc := seqio.NewScanner(fastq.NewReader(fh, template))

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

  pattern := regexp.MustCompile("BARCODE=(?P<r1_barcode>[ACGTN]+),(?P<r2_barcode>[ACGTN]+)")

  // Create a fasta writer with width 80:
  writer := fastq.NewWriter(fho)

  var i uint8 = 0
  for sc.Next() {
	seq := sc.Seq().(*linear.QSeq)
	// do stuff with seq as a *linear.QSeq

	annotation := seq.CloneAnnotation()
	description := annotation.Desc
	fmt.Println("i:", i,  "\tID:", annotation.ID, "\tdescription:", description)

	// -1 means return all found
	findall := pattern.FindAllStringSubmatch(description, -1)[0]

	replaced := pattern.ReplaceAllString(description, "BARCODE:"+findall[read_number])
	replaced = strings.Replace(replaced, "|", "_", -1)

	// Reassign the description
	annotation.SetDescription(replaced)
	id_parts := []string{annotation.ID, replaced}
	new_id := strings.Join(id_parts, " ")
	seq_replaced := linear.NewQSeq(new_id, seq.Seq, seq.Alphabet(), seq.Encode)

	writer.Write(seq_replaced)
	i++
  }
  err = sc.Error()
  // handle errors
  if err != nil {
	panic(err)
  }

}
