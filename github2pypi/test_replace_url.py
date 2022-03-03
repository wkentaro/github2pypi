from github2pypi.replace_url import replace_url


def test_replace_test():
    slug = "wkentaro/imgviz"
    content = "![](.readme/teaser.jpg)"
    content = replace_url(slug, content, branch="main")

    assert (
        content
        == "![](https://github.com/wkentaro/imgviz/blob/main/.readme/teaser.jpg?raw=true)"
    )
