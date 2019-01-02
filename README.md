# github2pypi


## Usage


### 1. Add `github2pypi` as submodule.

See [gdown](https://github.com/wkentaro/gdown) as an example.

```bash
git clone https://github.com/wkentaro/gdown
cd gdown

git submodule add https://github.com/wkentaro/github2pypi.git
```


### 2. Edit `setup.py`.

```python
import github2pypi

...
with open('README.md') as f:
    long_description = github2pypi.replace_url(
        slug='wkentaro/gdown', content=f.read()
    )

setup(
    ...
    long_description=long_description,
    long_description_content_type='text/markdown',
)
```
