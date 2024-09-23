import argparse
import asyncio
from pyppeteer import launch

async def generate_pdf(url, pdf_path):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.pdf({'path': pdf_path, 'format': 'A4'})
    await browser.close()


async def html_to_pdf(html_content, pdf_path):
    browser = await launch()
    page = await browser.newPage()
    await page.setContent(html_content)
    await page.pdf({'path': pdf_path, 'format': 'A4'})
    await browser.close()


def arguments():
    ap = argparse.ArgumentParser(description='Uses Pyppeteer to convert html->pdf')
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
            asyncio.get_event_loop().run_until_complete(html_to_pdf(html_content, output_path))
    elif url!='nothing':
        output_path = url.replace('.html','.pdf')
        asyncio.get_event_loop().run_until_complete(generate_pdf(url, output_path))
 
