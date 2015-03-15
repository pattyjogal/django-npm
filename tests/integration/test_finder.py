from ..util import configure_settings
configure_settings()

from django.test.utils import override_settings
from npm.finders import NpmFinder

def test_finder(tmpdir):
    pjson = tmpdir.join('package.json') \
    .write('''{
    "name": "test",
    "dependencies": {"mocha": "*"}
    }''')
    with override_settings(NPM_PREFIX_PATH=str(tmpdir)):
        f = NpmFinder()
        print list(f.list([]))
