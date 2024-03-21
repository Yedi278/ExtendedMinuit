Developed by Yehan Edirisinghe

Extension library for Minuit Class

# Install

On Notebooks (.ipynb):
    
    > pip install iminuit
    
    > pip install sympy
    
    > pip install ExtendedMinuit

# Importing:
    
    > from Minuit_newClass import ExtendedMinuit

    > import sympy as sp

    ## On Notebooks:
    
    > from IPython.display import Latex


# Usage:
    
    instead of : my_minuit = Minuit( args )
    
    use :   my_minuit = ExendedMinuit( args )

# Error Propagation:

    >Latex(my_minuit.prop_cov( args ))
