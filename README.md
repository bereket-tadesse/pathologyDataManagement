Simplified project outline:

1. Load the main directory containing the patient files ( 'stored_files' )
2. arrange them in directory based on year.
3. Load the directory of the new scanned patient files ( 'incoming_records')
4. Separate the two 'incoming_records'

- one pdf file which goes on top of every stored_files for all patient in query. ( 'pdf_for_all')
- one pdf file which goes to individual stored file based on ID of the patient. ('single_page_patient_record' )

5. Go thorugh every page of the incoming_records and detect each ID

- crop each page which contains the ID part
- use OCR to detect the ID number

package to use:

> PyPDF2

6. export the single page from the incoming records

7. look for the pdf corresponding to the ID from the stored files directory on the computer ( call it 'recordPDF_in_search')

- append single_page_patient_record on to recordPDF_in_search
- append pdf_for_all on to recordPDF_in_search

8. upload the package to TestPyPI

Progect hierarcy: <br>
├── src  
├── test  
├── project.toml  
├── LICENSE <br>
└── README.md

- helper functions:

  > extract_ID(): get single page, and export the ID
  > icoming_record_iterator(): iterate through the incoming_records.
  > find_patient_record(): iterate through the stored files to find the patient record.
  > pdf_file_appender()

- find best way to store those digitalized patient record files into a database.
