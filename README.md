# github2pypi


## Usage


### 1. Add `github2pypi` as submodule.

See [imgviz](https://github.com/wkentaro/imgviz) as an example.

```bash
git clone https://github.com/wkentaro/imgviz
cd imgviz

git submodule add https://github.com/wkentaro/github2pypi.git
```


### 2. Edit `setup.py`.

```python
import github2pypi

...
with open('README.md') as f:
    # e.g., ![](examples/image.jpg) ->
    #       ![](https://github.com/wkentaro/imgviz/blob/master/examples/image.jpg)
    long_description = github2pypi.replace_url(
        slug='wkentaro/imgviz', content=f.read()
    )

setup(
    ...
    long_description=long_description,
    long_description_content_type='text/markdown',
)
```
