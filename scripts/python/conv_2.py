import argparse
import pdfkit

def url_to_pdf(url, pdf_path):
    try:
        pdfkit.from_url(url, pdf_path)
        print(f"PDF generated and saved at {pdf_path}")
    except Exception as e:
        print(f"PDF generation failed: {e}")

def html_to_pdf(html_content, pdf_path):
    try:
        pdfkit.from_string(html_content, pdf_path)
        print(f"PDF generated and saved at {pdf_path}")
    except Exception as e:
        print(f"PDF generation failed: {e}")



def arguments():
    ap = argparse.ArgumentParser(description='Uses python-pdfkit to convert html->pdf')
    ap.add_argument('-f', '--file',
                    help="input file",
                    default="nothing"
                    )
    ap.add_argument('-u', '--url',
                    help="url",
                    default="nothing"
                    )
#    ap.add_argument("-o", "--outputfile", help="outputfile",
#                        default="./wwdocuments.xml")
    args = vars(ap.parse_args())
    return args

if __name__ == "__main__":
    args = arguments()
    invoer = args['file']
    url = args['url']
    if invoer!='nothing':
        pdf_path = invoer.replace('.html','.pdf')
        with open(invoer) as inv:
            html_content = inv.read()
            html_to_pdf(html_content, pdf_path)
    elif url!='nothing':
        pdf_path = url.replace('.html','.pdf')
        url_to_pdf(url_to_fetch, pdf_path)
 
