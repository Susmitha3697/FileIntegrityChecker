# FileIntegrityChecker                                                                                                                                                        


**COMPANY**: CODTECH IT SOLUTIONS                                                                                                                                                 

**NAME**: GOGULA SUSMITHA                                                                                                                                                         

**INTERN ID**: CT12WKPH                                                                                                                                                           

**DOMAIN**: CYBER SECURITY & ETHICAL HACKING                                                                                                                                      

**BATCH DURATION**: January 10th, 2025 to April 10th, 2025                                                                                                                       

**MENTOR**: Neela Santhosh Kumar                                                                                                                                                  

**DESCRIPTION OF THE TASK**:                                                                                                                                                      
The primary goal of this task is to develop a robust and user-friendly Python script that functions as a file integrity checker. This tool will monitor a specified set of files for any modifications by employing the concept of cryptographic hashing. By calculating and comparing hash values of files at different points in time, the script will be able to detect unauthorized or accidental changes to their content. This is crucial for ensuring data integrity, verifying that files remain unaltered over time, and potentially identifying malicious tampering.

The core functionality of the file integrity checker will revolve around the following key steps:

**Initialization and Configuration**: The script will need a mechanism to define the files that it should monitor. This could be achieved through a hardcoded list of file paths within the script itself, or ideally, through a more flexible configuration method such as reading file paths from an external configuration file (e.g., a text file or a JSON file). This allows users to easily specify and modify the set of monitored files without directly altering the script's code.

**Initial Hash Calculation**: Once the list of files to be monitored is established, the script will iterate through each file. For every file, it will calculate a cryptographic hash value of its content. A cryptographic hash function takes an input (in this case, the file's data) and produces a fixed-size output (the hash value) that is highly sensitive to even minor changes in the input. We will be utilizing the hashlib library in Python, which provides implementations of various widely used hashing algorithms such as SHA-256. SHA-256 is a secure and widely adopted algorithm that produces a 256-bit (64 hexadecimal characters) hash. The script will read the file content in chunks to efficiently handle potentially large files without consuming excessive memory. The calculated initial hash value for each monitored file will then be stored, likely in a dictionary where the file path serves as the key and the hash value as the corresponding value. This dictionary will represent the baseline "known good" state of the files.   

**Continuous Monitoring**: After the initial hashes are calculated and stored, the script will enter a continuous monitoring loop. This loop will execute periodically, with a configurable time interval between checks. During each iteration of the loop, the script will again iterate through the list of monitored files. For each file, it will recalculate its current hash value using the same hashing algorithm (SHA-256 in our case).

**Hash Comparison and Change Detection**: The newly calculated hash value for each file will then be compared against the initial hash value that was stored during the initialization phase. If the two hash values are identical, it signifies that the content of the file has remained unchanged since the initial hash was recorded. However, if the current hash value is different from the stored initial hash value, it indicates that the file has been modified in some way. Even a single bit change in the file's content will result in a drastically different hash value with a secure cryptographic hash function like SHA-256.   

**Reporting of Changes**: When a change is detected (i.e., the current hash does not match the initial hash), the script will need to report this event to the user. This could involve printing a message to the console, logging the event to a file, or potentially even sending an alert via email or another notification system for more critical applications. The report should clearly indicate which file has been modified, and ideally, it could also display the old (initial) hash value and the new (current) hash value for comparison.

**Handling New or Deleted Files (Optional Enhancement)**: For a more advanced version, the script could also handle scenarios where files are added to or removed from the monitored set. If a file in the initial list is no longer found during a monitoring cycle, the script could report it as a deletion. If a new file appears in the monitored directory (if monitoring a directory), the script could either ignore it or, optionally, add it to the monitoring list and calculate an initial hash for it.

**User Interface and Configuration**: While the initial deliverable is a Python script, consideration could be given to making it more user-friendly. This could involve using command-line arguments to specify the files to monitor or the configuration file path. A more advanced version might even include a graphical user interface (GUI) for easier interaction.

**Error Handling**: The script should include robust error handling to gracefully manage potential issues such as files not being found, permission errors when trying to read files, or other unexpected exceptions. Meaningful error messages should be provided to the user to help diagnose any problems.

In summary, this task involves designing and implementing a Python script that leverages the hashlib library to create a file integrity checker. The script will take a list of files, calculate their initial cryptographic hashes, periodically recalculate the hashes, and report any discrepancies that indicate a modification has occurred. This tool will be valuable for anyone needing to ensure the integrity and authenticity of their digital files. The focus will be on accuracy, efficiency in handling potentially large files, and clear reporting of any detected changes.                                                                                                                     


**OUTPUT**: <img width="775" alt="Image" src="https://github.com/user-attachments/assets/1cdaf3fc-6ddb-4dcf-a088-5186a74a386c" />
