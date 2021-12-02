#!/usr/bin/python3
import argparse
from PyPDF2 import PdfFileWriter, PdfFileReader
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", help="source pdf file")
    parser.add_argument("pages", help="pages list file")
    args = parser.parse_args()
    #print(args.pdf)
    #print(args.pages)
    inputpdf = PdfFileReader(open(args.pdf, "rb"))
    with open(args.pages) as file:
        lines = file.readlines()
        pages = [line.rstrip() for line in lines]
        #init_page=int(pages[0]); pages.pop(0)
        print (pages)
    for p in pages:
        page = p.split('-')
        if len(page) == 1: 
            ip_str=page[0]; fp_str=page[0]
        elif len(page)==2: ip_str, fp_str= page 
        else: raise ValueError("Incorrect pages file")
        print(ip_str,fp_str,"\n")
        output = PdfFileWriter()
        for i in range(int(ip_str), int(fp_str)+1):
            output.addPage(inputpdf.getPage(i))
        with open(args.pdf+"%s-%s.pdf" % (ip_str,fp_str), "wb") as outputStream:
            output.write(outputStream)


if __name__ == '__main__':
    main()