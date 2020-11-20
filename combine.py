import sys,os
if(sys.platform == "win32"):
    import msvcrt
    msvcrt.setmode(sys.stdout.fileno(),os.O_BINARY)

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

def merge(input_files,output):
    merger = PdfFileMerger(strict=False)

    for item in input_files:
        with open(item,'rb') as file:
            merger.append(file)

    with open(output,'w+') as of:
        merger.write(of)

    merger.close()


if __name__ == '__main__':
    print(sys.argv)
    if(len(sys.argv)==2):
        #print([f for f in os.listdir(".")])
        files = [f for f in os.listdir(".") if f.endswith(".pdf")]
        files = sorted(files,key=len)
        print(files)
        merge(files,sys.argv[1:][0])
    #pdf_cat(sys.argv[1:], sys.stdout)
