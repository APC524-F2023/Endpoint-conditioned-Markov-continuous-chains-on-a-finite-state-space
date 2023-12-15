# Endpoint-conditioned-Markov-continuous-chains-on-a-finite-state-space
Final Project for APC 524 Fall 2023 at Princeton University.

Contributors: Jiayu Li, Chenxiao Tian, Xuyang Xu

## Example
A example of how to use the uniform sampling method to study molecular evolution is included at `example.ipynb`.

## Documentation
To generate documentation for this project in html format and view it, run
```shell
nox --session docs
```

The file is located at `docs/build/html/index.html`.

## Testing
Run
```shell
nox --session tests
```

## Contribution
Jiayu Li is responsible for the implementation and testing of uniformsampling method, setup of CI, packaging, and documentation, and demonstration of uniformsampling in molecular evolution.
             Chenxiao Tian is responsible for adjusting the CI testing
Xuyang Xu mainly contributions to the part of forward sampling and rejection sampling, the testing of rejection sampling method and the changes of computational cost when parameters are changed.
