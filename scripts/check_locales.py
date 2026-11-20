"""Check a built Zola site: python3 scripts/check_locales.py path/to/public."""
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import urljoin, urlsplit, unquote


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.language = ''
        self.alternates = {}
        self.switch = {}
        self.links = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html':
            self.language = a.get('lang')
        if tag == 'link' and 'hreflang' in a:
            self.alternates[a['hreflang']] = a['href']
        if tag == 'a' and 'hreflang' in a:
            self.switch[a['hreflang']] = a['href']
        if tag in ('a', 'link', 'img'):
            self.links.append(a.get('href') or a.get('src'))


root = Path(sys.argv[1])
pages = {('/' + p.parent.relative_to(root).as_posix().strip('.') + '/').replace('//', '/'): Document(p)
         for p in root.rglob('index.html')}
for route, doc in pages.items():
    lang = 'es' if route.startswith('/es/') else 'en'
    assert doc.language == lang, route
    assert set(doc.alternates) == {'en', 'es'} and doc.switch == doc.alternates, route
    assert urlsplit(doc.switch[lang]).path == route, route
    for dest in doc.switch.values():
        assert pages[urlsplit(dest).path].switch == doc.switch, (route, dest)
    for link in filter(None, doc.links):
        u = urlsplit(urljoin(doc.switch[lang], link))
        if u.netloc != urlsplit(doc.switch[lang]).netloc:
            continue
        path = unquote(u.path)
        if path in pages and link not in doc.switch.values():
            assert pages[path].language == lang, (route, link)
        assert (root / path.lstrip('/')).exists(), (route, link)
print(f'Validated {len(pages)} localized routes, reciprocal switchers and internal destinations.')
