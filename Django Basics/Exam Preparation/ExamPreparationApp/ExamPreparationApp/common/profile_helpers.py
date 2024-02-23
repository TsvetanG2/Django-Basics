def get_profile():
    return Profile.objects.first()
    # If this profile exists we cannot create it

# Use this helper to import the get_profile() into the files, instead of writing it down