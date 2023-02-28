<h1 align="center">
  Download YouTube
</h1>

<h4 align="center">Downloads a YouTube video onto the agent.</h4>

<p align="center">
  <img alt="DataTorch Action" src="https://img.shields.io/static/v1?label=DataTorch%20Action&message=datatorch/download-youtube@v1&color=blueviolet">
  <img alt="Open Issues" src="https://img.shields.io/github/issues/datatorch-actions/download-youtube">
</p>

## Quick Start

```yaml
name: 'Download Youtube'
jobs:
  add:
    steps:
      - name: Download Youtube Video
        action: datatorch/download-youtube
        inputs:
          url: https://www.youtube.com/watch?v=Z-zR1SgrM-w
```
