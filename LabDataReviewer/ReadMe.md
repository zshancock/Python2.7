Lab Data Reviewer
================
##### Author - Zac Hancock (zshancock@gmail.com)

A code I wrote specifically for my laboratory to review data from an instrument (SEAL AQ2 discrete analyzer) and generate a report
that displays to the analyst the performance of the "run". Several criteria are tested against every line in the CSV using a loop 
and if/elif/else statements. Having reviewed this data the old fashioned way, I will admit that sometimes it can take as long as 10-20
minutes to make absolutely sure all the Quality control passed. This script reviews the run's QC in sub-second times. The program will 
generate a .txt file with the report that : 1) Identifies the run information (analyst, date, test), 2) Identifies "Acceptable" Quality 
control and validates that all samples are reportable, and 3) Identifies which QC failed and which samples need reanalyzed at a higher
dilutions. 

Criteria that was considered: Quality control theoretical values, Quality control acceptance criteria (i.e. +/- 10% recovery), Blanks are 
                              less than the reporting limit BUT not more negative than (reporting limit * -1) and all Samples must be less
                              than the maximum detection limit, if samples are over range, they must be diluted back into range - the program
                              checks to make sure that all sample results are less than maximum detection limit * dilution factor. 

**Summary of Contents:**

*InstrumentCSVs folder:*
> Sample data from the laboratory - was used to generate reports.

> 070317_tkn.csv - a run with all acceptable criteria

> 071317_tkn.csv -             "

> 071717_tkn.csv -             "

> 123456_tkn.csv - a run with several failing criteria and samples that need additional dilutions


*OutputReports Folder:*
> The program created text files, denoted with "_reviewed" to easily locate in directory. 
