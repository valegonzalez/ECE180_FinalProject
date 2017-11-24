:: Store existing env vars and set to this conda env
:: so other installs don't pollute the environment.

@if defined PROJ_LIB (
    set "_CONDA_SET_PROJ_LIB=%PROJ_LIB%"
)
@set "PROJ_LIB=%CONDA_PREFIX%\Library\share"
