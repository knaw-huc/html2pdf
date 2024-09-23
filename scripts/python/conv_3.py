import argparse
from weasyprint import HTML

def url_to_pdf(url, output_path):
    HTML(url).write_pdf(output_path)

def html_to_pdf(html_content, output_path):
    HTML(string=html_content).write_pdf(output_path)


def arguments():
    ap = argparse.ArgumentParser(description='Uses WeasyPrint to convert html->pdf')
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
            html_content = inv.read()
            html_to_pdf(html_content, output_path)
    elif url!='nothing':
        output_path = url.replace('.html','.pdf')
        url_to_pdf(url, output_path)
 
