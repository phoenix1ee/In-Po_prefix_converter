# Shun Fai Lee Lab1
# Prefix to Postfix Converter

This python package is primarily designed as a converter for the conversion of string expression from prefix format to postfix format.

It accepted user input from a text file and output to the user specified text file.

However, it can also perform optional actions, including conversion from postfix to prefix, infix to postfix/prefix as well, with the appropriate argument input. 

## How to download and run:

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m Lab1converter -h`. This will print the help message.
4. Run the program as a module (with real inputs): `python -m Lab1converter <some_input_file> <some_output_file>`
   a. IE: `python -m Lab1converter file/rinput.txt file/routput.txt`

Output will be written to the specified output file after processing the input file.

### Lab1converter Usage:

```commandline
usage: python -m proj0 [-h] [-t {po2pe,in2po,in2pe} ] in_file out_file

positional arguments:
  in_file     Input File Pathname
  out_file    Output File Pathname

optional arguments:
  -h, --help  show this help message and exit
  -t {po2pe,in2po,in2pe} Optional conversion type (default: prefix to postfix)
```

Usage statements are very formalized

| Symbol   | Meaning                                                                                       |
|----------|-----------------------------------------------------------------------------------------------|
| [h]      | variable h is optional. It display the helper message                                         |
| [t]      | variable t is optional. It allows the converter to do alternate conversion. 3 possible values |
|          | -po2pe means postfix to prefix                                                                |
|          | -in2po means infix to postfix                                                                 |
|          | -in2pe means infix to prefix                                                                  |
| in_file  | This is the path for input txt file. Required Positional argument                             |
| out_file | This is the path for output txt file. Required Positional argument                            |
                                                                        |
## Lab1converter Project Package and Layout

This project have a single module in a single package
Here is Lab1converter package explained.

* [Lab1converter/](.): The parent package folder.
    * [README.md](README-lab1):
      The guide for using this converter
    * [Lab1converter](Lab1Converter): 
      This is the *module* in this *package*.
      * [`__init__.py`](Lab1Converter/__init__.py) 
        
      * [`__main__.py`](Lab1Converter/__main__.py) 
        This file is the entrypoint to the converter when ran as a program. It handles the command line arguments and do all functions calling and output.
      * `helper.py` 
        This the scripts containing functions for some repetitive checking, particularly pecedence and input validation.
      * `Opstack.py` 
        This the Stack Class ADT defined for use in other functions.
      * `in2po.py` 
        This the converter for infix to postfix.
      * `pe2po.py` 
        This the converter for prefix to postfix.
      * `po2pe.py` 
        This the converter for postfix to prefix.

## Input and Output format:

For this converter to function properly, user should supply two legitimate file paths as argument, and by default, without specifying optional [-t] arguments, the converter will presume that string inside input text file are prefix strings and to do conversion from prefix format to postfix format.

The input txt file should be written line by line, with each line corresponding for a single expression string.

It support multiple lines in the input file, and will print out the results to an output file in the sequence of input accordingly.

Any space/tabs/ character inside the input string of each line will be trimmed.
Any empty line/incorrect input will be skipped with error message provided in output file.

> Operators: +, -, *, /, $
> 
> Alphabetical operands: A,B,C... 
> 
> For infix to prefix/postfix only: brackets: ( ),{ },[ ]
> 


### Example input and output

This converter adopt a principle for conversion related with exponential operation: `A$B$C` will be presumed as `(A$(B$C))`

>An example of prefix to postfix 
> 
>From Input file : `$$-ACBC`
> 
>In Output file: 
>
>`input : $$-ACBC`
>
>`output: AC-B$C$`

>An example of prefix to postfix with space between
> 
>From Input file : `$$$+A BCDE`
> 
>In Output file: 
>
>`input : $$$+ABCDE`
>
>`output: AB+C$D$E$`

>An example of Infix to postfix 
> 
>From Input file : `A+(((B-C)*(D-E)+F)/G)$(H-J)$(L-M)$(N-O)`
> 
>In Output file: 
> 
>Input : `A+(((B-C)*(D-E)+F)/G)$(H-J)$(L-M)$(N-O)`
>
>Output:`ABC-DE-*F+G/HJ-LM-NO-$$$+`
