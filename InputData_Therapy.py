
# simulation settings
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0   # annual discount rate

ADD_BACKGROUND_MORT = True  # if background mortality should be added
DELTA_T = 1      # years

PSA_ON = False      # if probabilistic sensitivity analysis is on

# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15,    0.0,    0.1],   # Well
    [0,     0,    1.0,    0.0],   # Stroke
    [0,     0.1625,      0.6275,   0.21],    # Post-Stroke
    [0,     0,      0,      1.0],  # Dead
    ]

# annual cost of each health state
ANNUAL_STATE_COST = [
    0,   # CD4_200to500
    0,   # CD4_200
    0    # AIDS
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    0,   # CD4_200to500
    0,   # CD4_200
    0    # AIDS
    ]

# annual drug costs
Zidovudine_COST = 0
Lamivudine_COST = 0

# treatment relative risk
TREATMENT_RR = 1
TREATMENT_RR_CI = 1, 1  # lower 95% CI, upper 95% CI

# annual probability of background mortality (number per year per 1,000 population)
ANNUAL_PROB_BACKGROUND_MORT = 0 / 1000

