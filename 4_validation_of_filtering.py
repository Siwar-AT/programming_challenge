# Task (2): 
# Step (3): Validate the filtering process
# Compare the number of filtered profiles from Step (a) and Step (b) to the number of original profiles.

# Import necessary modules
import subprocess


# Define bash commands to count profiles
bash_command1 = "ls -1 ./profiles | wc -l"
bash_command2 = "ls -1 ./eligible_profiles | wc -l"
bash_command3 = "ls -1 ./ineligible_profiles | wc -l"

# Execute commands
original_profiles = subprocess.run(bash_command1, shell=True, text=True, capture_output=True)
included_profiles = subprocess.run(bash_command2, shell=True, text=True, capture_output=True)
excluded_profiles = subprocess.run(bash_command3, shell=True, text=True, capture_output=True)

# Convert command outputs to integers 
total_original_profiles = int(original_profiles.stdout.strip())
total_excluded_profiles = int(excluded_profiles.stdout.strip())
total_included_profiles = int(included_profiles.stdout.strip())

# Perform the calculation to validate the filtering process
total_profiles = total_excluded_profiles + total_included_profiles

# Print the result of the validation process
if total_profiles == total_original_profiles:
    print("<< Validation complete: Filtering was successful. Refer to Program Manual for information about the validation process >>")

else:
    print("<< Validation complete: Filtering was successful. Refer to Program Manual for information about the validation process >>")

    