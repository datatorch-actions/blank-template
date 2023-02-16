<h1 align="center">
  Add Action
</h1>

<h4 align="center">Add two inputs together and sets resulting sum as output.</h4>

<p align="center">
  <img alt="DataTorch Action" src="https://img.shields.io/static/v1?label=DataTorch%20Action&message=datatorch/add@v1&color=blueviolet">
  <img alt="Open Issues" src="https://img.shields.io/github/issues/datatorch-actions/add">
</p>

## Quick Start

```yaml
name: 'Add Example'
jobs:
  add:
    steps:
      - name: Add Two Numbers
        action: datatorch/add@v1
        inputs:
          a: 5
          b: 5
```
