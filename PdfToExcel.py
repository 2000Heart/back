import tabula


def pdfToExcel():
    df = tabula.read_pdf('/Users/hc-cxk/Desktop/文字文稿1.pdf', pages=1, lattice=True)[1]
    df.columns = df.columns.str.replace('\r', ' ')
    data = df.dropna()
    data.to_excel(r'/User/hc-cxk/desktop/文字文稿1.xlsx')
    return 1