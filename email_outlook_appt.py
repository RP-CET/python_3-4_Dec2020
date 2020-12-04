import win32com.client

#Create and send appointment
outlook = win32com.client.Dispatch("Outlook.Application")
appt = outlook.CreateItem(1) # AppointmentItem, 0 - Email
appt.Start = "2020-12-04 17:35" # yyyy-MM-dd hh:mm
appt.Subject = "Subject of the meeting"
appt.Duration = 60 # In minutes (60 Minutes)
appt.Location = "Location Name"

# 1 - olMeeting; Changing the appointment to meeting.
# Only after changing the meeting status recipients can be added
appt.MeetingStatus = 1
  
appt.Recipients.Add("tay_mei_lan@myrp.edu.sg") # Don't end ; as delimiter
appt.Recipients.Add("tayml.at.rp@gmail.com") # Don't end ; as delimiter

# Set Pattern, to recur every day, for the next 5 days
pattern = appt.GetRecurrencePattern()
pattern.RecurrenceType = 0
pattern.Occurrences = "5"

appt.Save()
appt.Send()
print("Sent")
