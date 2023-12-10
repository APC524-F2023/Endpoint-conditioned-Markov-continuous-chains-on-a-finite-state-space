# Endpoint-conditioned-Markov-continuous-chains-on-a-finite-state-space
Final Project for APC 524 Fall 2023 at Princeton University.

Contributor: Jiayu Li, Chenxiao Tian, Xuyang Xu

## Example
A example of how to use the uniform sampling method to study molecular evolution is included at `example.ipynb`.

## Documentation
To generate documentation for uniformsampling in html format, run
```shell
nox --sessions doc
```

The file is located at `docs/build/html/index.html`.

## Testing
Run
```shell
nox --sessions tests
```

## Contribution
Jiayu Li is responsible for the implementation and testing of uniformsampling method, setup of CI, packaging, and documentation (including the nox session), and demonstration of uniformsampling in molecular evolution.
