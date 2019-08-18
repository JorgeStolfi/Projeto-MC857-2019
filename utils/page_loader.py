
def load_page(page_name):
    pageHtmlFile = open('html/%s.html' % page_name, 'r')
    pageHtml = pageHtmlFile.read()
    pageHtmlFile.close()
    pageCssFile = open('css/%s.css' % page_name, 'r')
    pageCss = pageCssFile.read()
    pageCssFile.close()
    return pageHtml % pageCss