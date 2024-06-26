# Fuzzing `bytes_to_words` Function in PyCryptodome

## Background

PyCryptodome is a Python library widely used for cryptographic operations like encryption, decryption, digital signatures, hashing, etc. Endianness, a crucial feature in PyCryptodome, supports block ciphers, initialization vectors, and customized data handling protocols.

## Issue

The `bytes_to_words` function in PyCryptodome hasn't been fuzzed before. This function is essential for ensuring and implementing endianness correctly.

## Motivation

- Learn about fuzzing.
- Gain insights into cybersecurity and cryptography.
- Practice coding skills.

## Tools

- PyCryptodome library.
- `test_endianess`, providing a testing structure for the `bytes_to_words` function.
- PyCryptodome implementation.
- VS Code and provided C extensions, "C/C++" and "Code Runner", as well as "Live Share" for authors to pair code. All commits contributed to by all members of team.

## Fuzzer Description

**Idea**: Randomly generate strings of numbers → Convert to bytes → Pass into `bytes_to_words` → Examine output.

**Implementation**:

- Randomly generate strings of various lengths.
- Convert strings to bytes.
- Pass bytes into the `bytes_to_words` function.
- Check if the return value is 0 for success or non-zero for failure.

**How to Implement Locally**:

*Prerequisites*
1. Ensure you have Python and a C compiler installed on your system.
2. Git clone this repo to have copy of the PyCryptodome library that can be accessed and modified.
3. Move to the "test" folder, path "CS340-Final/pycryptodome-master/src/test"
4. Have the test-byte-works executable from the C file you're testing, test-byte-works.c. For our purposes, we ran gcc test-byte-works.c -o test-byte-works, determined by using Code Runner extension to run the test-byte-works.c file and make executable.
5. Ensure Python script entitled fuzzer.py for generating random inputs runs as well. File should be in same folder, "CS340-Final/pycryptodome-master/src/test".

*Implementation Steps*
1. Prepare the Fuzzer Script
2. Write a Python script named fuzzer.py to generate random inputs. This script generates an array of 9 bytes, which will be passed to the function being tested (bytes_to_words).
3. Compile the C file containing the bytes_to_words function to generate the test-byte-works executable.
4. Run the Fuzzer
5. Use the generated random input from fuzzer.py as an argument to test-byte-works. Enter following in terminal:
```./test-byte-works "$(python fuzzer.py)"```
6. Analyze Results. Check the output of test-byte-works. If it returns 0, the fuzzing was successful. Otherwise, there might be an issue with the bytes_to_words function. Results are also printed to file ```output.txt```, located in src/test folder as well, to save and review later.

By following these steps, you can locally implement the fuzzer to test the bytes_to_words function in PyCryptodome. 

## Trade-offs

- C's strict type system limits the ability to ensure entirely random data.
- Consideration of `word_to_byte` vs. `byte_to_word` conversions.; not enough time to do both but would be more robust to test both functions at they do similar things.
- Not fully automated because command line code tests bytes_to_words for a single randomized input. Considered writing script to automate the actual command line call to run multiple times, but constrained by time and worried about cost of running programs 100s+ times in Wellesley's CS server. To attempt to compensate for this, functionality to print test input and its behavior, whether working or unexpected, was implemented, located in the file "CS340-Final/pycryptodome-master/src/test/output.txt", for user to review as data is collected over time.

## Challenges

- Handling data types effectively.
- Managing the length of words in bytes.
- Efficient data transfer between Python and C.
- Refreshing general C language skills.

## Assumptions and Limitations

- The fuzzing scope is limited to the `bytes_to_words` function.
- The quality and randomness of input data might affect fuzzing results.

By fuzzing the `bytes_to_words` function, we aim to ensure its robustness and correctness in handling endianness, thereby enhancing the overall security and reliability of PyCryptodome.
