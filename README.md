<h1 align="center">
  github2pypi
</h1>

<h4 align="center">
  Utils to release Python repository on GitHub to PyPi
</h4>

<div align="center">
  <a href="https://github.com/wkentaro/github2pypi/actions"><img src="https://github.com/wkentaro/github2pypi/workflows/ci/badge.svg"></a>
</div>


## Usage

```bash
pip install github2pypi
```


### 2. Edit `setup.py`.

```python
import github2pypi

...
with open('README.md') as f:
    # e.g., ![](examples/image.jpg) ->
    #       ![](https://github.com/wkentaro/imgviz/blob/main/examples/image.jpg)
    long_description = github2pypi.replace_url(
        slug='wkentaro/imgviz', content=f.read(), branch="main"
    )

setup(
    ...
    long_description=long_description,
    long_description_content_type='text/markdown',
)
```


## Examples

- https://github.com/wkentaro/labelme
- https://github.com/wkentaro/imgviz
