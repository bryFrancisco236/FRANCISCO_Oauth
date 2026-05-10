# FRANCISCO_Oauth
Activity for BIT321 SYSTEM INTEGRATION [LAB]

i. What happens when a user accesses /profile without logging in?
When someone tries to visit /profile without logging in, the code checks the session for a user "badge." Since the user haven't logged in, the code finds nothing and blocks the access. It then shows an "Unauthorized" message and a 401 error code. This ensures that only people with the right permission can see the data.

ii. What data is returned after successful login?
After a successful login, GitHub sends back a list of details about my account in JSON format. This usually includes my username, my unique ID number, and a link to my profile picture. It may also show my public bio or email if I allowed it. My app stores this info to remember who I am.

iii. Why is OAuth considered more secure than traditional login?
OAuth is safer because you never have to give your password to the app you are using. Instead, you log in directly through a trusted site like GitHub, which then gives the app a temporary "key" or token. This token can only do specific things and can be canceled at any time. It keeps your main password private and protected from the app creator.

iv. What challenges did you encounter?
The biggest challenge was setting up the virtual environment and making sure all the right tools were installed. I also ran into a "redirect mismatch" error because the website addresses in the code and GitHub settings did not match exactly. Finally, I had to learn how to use Git commands to fix errors when sending my files to GitHub.

v. What did you learn from this activity?
I learned how to let users log in using their existing social media accounts instead of creating new passwords. I also learned how to protect specific parts of a website so only logged-in people can see them. Most importantly, I saw how different websites "talk" to each other securely using tokens and keys.
