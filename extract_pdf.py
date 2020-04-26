from PyPDF2 import PdfFileReader, PdfFileWriter

writer = PdfFileWriter()


def main():
    output = "out.pdf"
    with open("pdf_data.txt", 'r') as file:
        cos = file.read().split("\n")

    path = cos.pop(0)
    pdf = PdfFileReader(path, "rb")

    for item in cos:
        for page in range(int(item.split(":")[0]) - 1, int(item.split(":")[1])):
            writer.addPage(pdf.getPage(page))

    with open(output, "wb") as file:
        writer.write(file)


if __name__ == "__main__":
    main()
