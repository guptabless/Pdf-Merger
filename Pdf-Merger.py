import PyPDF2
import bcolors
import sys, argparse

def banner():
    print("""

                ██████╗░██████╗░███████╗░░░░░░███╗░░░███╗███████╗██████╗░░██████╗░███████╗██████╗░
                ██╔══██╗██╔══██╗██╔════╝░░░░░░████╗░████║██╔════╝██╔══██╗██╔════╝░██╔════╝██╔══██╗
                ██████╔╝██║░░██║█████╗░░█████╗██╔████╔██║█████╗░░██████╔╝██║░░██╗░█████╗░░██████╔╝
                ██╔═══╝░██║░░██║██╔══╝░░╚════╝██║╚██╔╝██║██╔══╝░░██╔══██╗██║░░╚██╗██╔══╝░░██╔══██╗
                ██║░░░░░██████╔╝██║░░░░░░░░░░░██║░╚═╝░██║███████╗██║░░██║╚██████╔╝███████╗██║░░██║
                ╚═╝░░░░░╚═════╝░╚═╝░░░░░░░░░░░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝  
                                                                                       Code by NG          
          """)

if len(sys.argv) > 1:
    banner()
    if ((sys.argv[1] == '-l1') | (sys.argv[1] == '-l2') | (sys.argv[1] == '-o')):
        try:
            Myloc1 = sys.argv[2]
            Myloc2 = sys.argv[4]
            Saveloc = sys.argv[6]

            # Open file
            pdf1file = open(Myloc1, 'rb')
            pdf2file = open(Myloc2, 'rb')

            parser = argparse.ArgumentParser()
            parser.add_argument("-l1", required=True)
            parser.add_argument("-l2", required=True)
            parser.add_argument("-o", required=True)
            args = parser.parse_args()

            pdf1Reader = PyPDF2.PdfFileReader(pdf1file)
            pdf2Reader = PyPDF2.PdfFileReader(pdf2file)

            pdfWriter = PyPDF2.PdfFileWriter()

            for pageNum in range(pdf1Reader.numPages):
                pageObj = pdf1Reader.getPage(pageNum)
                pdfWriter.addPage(pageObj)

            for pageNum in range(pdf2Reader.numPages):
                pageObj = pdf2Reader.getPage(pageNum)
                pdfWriter.addPage(pageObj)

            pdfOutFile = open('Pdf-Merger.pdf', 'wb')
            pdfWriter.write(pdfOutFile)
            print(bcolors.OKMSG + 'Merge PDf generated at ', Saveloc)

            pdfOutFile.close()
            pdf1file.close()
            pdf2file.close()

        except:
            print(bcolors.ERR + 'Please provide valid Path ')
            print(bcolors.BOLD + 'Please enter python MergePdf.py -l1 <valid path> -l2 <valid path> -o <output save location>')


    elif (((sys.argv[1] == '-l1') & (sys.argv[1] == '-l2')) | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: Pdf-Merger.py [-h] -l1 1st Location , -l2 2st Location ' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-l1 1 st Location,   --loc1 1st Location ' '\n''-l2 2 st Location,   --loc2 2st Location ' 
                             '\n' '-o output    Output Save location')
    elif (((sys.argv[1] == '-l1') & (sys.argv[1] == '-l2')) | (sys.argv[1] != '-o')):
        print('Please enter -l1 <valid path> -l2 <valid path> -o <output save location>')

else:
    banner()
    print(bcolors.ERR + 'Please select options from ((-l1,-l2) and -o) or -h, with a valid domain name')



