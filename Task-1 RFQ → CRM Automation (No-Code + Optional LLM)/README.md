Project Goal: 
A fully automated pipeline to capture, process, and archive RFQ data.

Workflow Steps:

Capture: 
Triggered by a custom Mailhook (ebra988...).

Extract: 
A JSON Parser structures the email body into usable variables.

Log: 
Data is written to the RFQ Logs Google Sheet.

CRM: 
An HTTP POST request creates a mock opportunity.

Notify: 
Sends a bilingual Gmail confirmation and a Slack alert to the team.

Archive: 
Attachments are iterated and uploaded to a specific Google Drive folder.

Setup Instructions:

Import the provided Blueprint into Make.com.

Configure Google Sheets with the localized time formula: 

formatDate(now ; YYYY-MM-DD hh:mm A ; Asia/Riyadh).

Set the Google Drive upload folder to RFQ Attachments.
