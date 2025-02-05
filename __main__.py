#Shun Fai Lee Lab1
from pathlib import Path
import argparse
from time import time_ns

from Lab1converter.po2pe import po2pe
from Lab1converter.pe2po import pe2po
from Lab1converter.in2po import in2po

# use the Argument parser to define compulsory and optional arguments
this_parser = argparse.ArgumentParser(description ='convert expression between infix/postfix/prefix')
this_parser.add_argument("in_file", type=str, help="Input File Pathname")
this_parser.add_argument("out_file", type=str, help="Output File Pathname")
this_parser.add_argument('-t', type=str, choices=['po2pe','in2po','in2pe'], default='pe2po', required=False, action='store', help="Optional conversion type (default: prefix to postfix)")
this_parser.add_argument('-tm', type=bool, choices=[True], default=False, required=False, action='store', help="Optional processing timer (default: off)")
args = this_parser.parse_args()

# Set the input and output file path
in_path = Path(args.in_file)
out_path = Path(args.out_file)

if args.tm:
    start_time = time_ns()

if in_path.is_file():
    #proceed if the input file exist
    with (in_path.open('r') as input_file, out_path.open('w') as output_file):
        for line in input_file:
            in_c = line.strip().replace(" ", "")
            if in_c:
                output_file.write("input : " + in_c + "\n")
                if args.t == "pe2po":
                    out_c = pe2po(in_c)
                elif args.t == "po2pe":
                    out_c = po2pe(in_c)
                elif args.t == "in2po":
                    out_c = in2po(in_c)
                elif args.t == "in2pe":
                    out_c = po2pe(in2po(in_c))
                """write the converted string to the output file"""
                output_file.write("output: " + out_c + "\n" + "\n")
            else:
                output_file.write("{an empty line detected}" + "\n" + "\n")
        if args.tm:
            end_time = time_ns()
            output_file.write(f'Start time: {"%.2f" % start_time} ns' + "\n")
            output_file.write(f'process time: {"%.2f" % (end_time - start_time)} ns')
else:
    raise Exception(f'Input file in {in_path.absolute()} do not exist')