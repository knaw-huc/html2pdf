import argparse
from xhtml2pdf import pisa
import requests

async def url_to_pdf(url, pdf_path):
    # Fetch the HTML content from the URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch URL: {url}")
        return False
    html_content = response.text
    # Generate PDF
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)
    return not pisa_status.err


async def html_to_pdf(html_content, pdf_path):
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)    
    return not pisa_status.err


def arguments():
    ap = argparse.ArgumentParser(description='Uses xhtml2pdf to convert html->pdf')
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
        output_path = invoer.replace('.html','.pdf')
        with open(invoer) as inv:
            if html_to_pdf(html_content, output_path):
                print(f"PDF generated and saved at {output_path}")
            else:
                print("PDF generation failed")
    elif url!='nothing':
        if url_to_pdf(url, output_path):
            print(f"PDF generated and saved at {output_path}")
        else:
            print("PDF generation failed")
 
