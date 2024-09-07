import argparse
import os
import pprint

parser = argparse.ArgumentParser(description='Description: Reduce PDF size')
parser.add_argument("--n", type=str, help="path of the pdf file to be reduced", required=True, )

args = parser.parse_args()
pprint.pprint(vars(args))

# filePath = str(input("Enter path of file: "))
# filename = str(input("File name: "))
filename = args.n

name = filename.replace(".pdf", "")

outputName = f'{name}_reduced.pdf'

setting = "ebook"  # screen, ebook, prepress
cmd = f'gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/{setting} -dNOPAUSE -dQUIET -dBATCH -sOutputFile=' \
      f'\"{outputName}\" \"{name}.pdf\"'
os.system(cmd)  # running the command
# os.system(f'rm {name}.pdf') # removing the file:
os.system(f'mv \"{outputName}\" \"{name}\".pdf')  # renaming the file, "mv": is used to move/renaming file
