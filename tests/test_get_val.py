import pytest
from utils import dicts


@pytest.mark.parametrize('collection, key, default, expected', [
    ({"vcs": "mercurial"}, "vcs", None, 'mercurial'),
    ({"vcs": "mercurial"}, "vcs", "git", 'mercurial'),
    ({}, "vcs", "git", 'git'),
    ({}, "vcs", "bazaar", 'bazaar')
])
def test_get_val(collection, key, default, expected):
    assert dicts.get_val(collection, key, default) == expected
