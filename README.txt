-------------------------------------
 Conditional Probability Calculator
-------------------------------------

*Main Program Name*: main.py

*Purpose*: Calculate conditional probability to investigate the potential link between the companies software engineers
           have worked for and their programming language skills.

*Prerequisites*: Python 3.12.3

*Python Standard Library Modules Used*: json, subprocess, shutil, collections, and pathlib.

*Custon Python Modules Used*: company_occurrence_module.py, language_company_cooccurrence_module.py, conditional_probability_module.py

*External Packages*: None used

*File Handling*: This program assumes that all specified input files are in JSON format, and that all input files and directories
                 are located in the current working directory. It also produces files in JSON format and places all output 
                 files and directories in the current working directory.  

*User Input*: None required


-------------------------------------------------------------------------------------------------------------------------------

*Program Workflow*: -{ Task(1) }-
                     The program begins by unpacking a compressed tar archive in order to extract the directory
                     containing the LinkedIn profile files.


                    -{ Task(2) }-
                     The program processes the companies listed in profiles that have have at least 1 programming language skill 
                     and experience at 3 or more companies. The companies are extracted from each profile and compiled into a 
                     single list. 


                    -{ Task(3) }-
                     The program uses the extracted list of companies to count the occurrences of each company. All occurrence counts 
                     are then compiled into a dictionary. 
                     Module used for this task: company_occurrence_module.py


                    -{ Task(4) }-
                     The program analyses profiles that have at least 1 programming language skill and experience at 3 or more companies
                     and counts the co-occurrences of each programming language with each company. All co-occurrence counts are then 
                     compiled into a dictionary.
                     Module used for this task: language_company_cooccurrence_module.py


                    -{ Task(5) }-
                     The program calculates 'P(language|company)' which is the conditional probability of each programming 
                     language with each company.
                     The probability for each language-company pair is calculated by dividing their co-occurrence count by 
                     the occurrence count of the company. All calculated probabilities are printed to the screen and compiled
                     into a dictionary, which is subsequently written to an output file.
                     Module used for this task: conditional_probability_module.py


-------------------------------------------------------------------------------------------------------------------------------
