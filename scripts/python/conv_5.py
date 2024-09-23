import argparse
import asyncio
from playwright.async_api import async_playwright

async def url_to_pdf(url, output_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.pdf(path=output_path)
        await browser.close()

async def html_to_pdf(html_content, output_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_content(html_content)
        await page.pdf(path=output_path)
        await browser.close()



def arguments():
    ap = argparse.ArgumentParser(description='Uses Playwright to convert html->pdf')
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
            asyncio.run(html_to_pdf(html_content, output_path))
    elif url!='nothing':
        output_path = url.replace('.html','.pdf')
        asyncio.run(url_to_pdf(url, output_path))
 
