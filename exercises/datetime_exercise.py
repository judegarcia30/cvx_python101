from datetime import datetime
now = datetime.now()

print("{0}/{1}/{2}".format(now.month, now.day, now.year))
print("{0}:{1}:{2}".format(now.hour, now.minute, now.second))

# The example above will print out the date, then on a separate line it will print the time.
# Let’s print them all on the same line in a single print statement!

# Print the date and time together in the form: mm/dd/yyyy hh:mm:ss using f-string method f''