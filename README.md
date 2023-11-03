# BrandonWhite_ITEC4012A_Project_v2

## Refresher
<hr>
For my project, I decided to make a tool that players could use while playing a Fallout Tabletop RPG. The tool acts as basically a digital character sheet. 

## Notes
<hr>
<p>Thank you so much for giving us the grace days system for this class! It’s been a busy month (I have a job and I’m finishing my education part time) and because of the three grace days I used, I was able to complete the backend to the best of my ability instead of submitting it totally unfinished.</p>

### Known Issues
<hr>
<p>These are must fixes.</p>

<p>In general:</p>
<ol>
  <li>I could not get <strong>User Registration</strong> working, so currently, there is no way for a user to make an account. Instead, I have just created a couple of test accounts in the database that you can use.</li>
  <li>I had issues with getting <strong>JSON</strong> to work, so I ended up doing everything with normal form actions. Because of this:
  <ol type="a">
    <li>Inputs are named with the IDs of the character or armor piece or weapon they are updating. This is just the easiest way I found to do those things without JSON.</li>
    <li>When you post a request, it brings to a "Success!" HTTPResponse. You then need to back out of it and refresh the page to see your updates.</li>
  </ol>
  </li>
  <li>The forms and data is all very jumbled and are not styled at all. I didn't pay much attention to usability on the frontend yet since this is just the backend deliverable. Everything is in unordered lists, but will go in tables.</li>
</ol>

<p>On charactersheet.html</p>
<ol start="4">
  <li>Perks display with a bunch of extra characters along with the names. Trust me, it was worse before. I also need to let you see their decscriptions.</li>
  <li>The initial values of the forms should be set to the character's initial values instead of the model default, but I have not figured that out yet (e.g. A character could have 60 HP, but the form to change HP shows 1 instead of 60.</li>
</ol>

<p>On levelup.html</p>
<ol start="6">
  <li>Initial values should be character initial values, not model default.</li>
  <li>Could not figure out the syntax to get perks to update. May change the model in the near future.</li>
  <li>Similar to the character sheet, perks display with extra info around their names.</li>
</ol>

<p>Also, you'll probably notice that tests.py is empty. Honestly, I ran out of time since I had to do a crazy amount of bugfixing, and I couldn't think of any tests to do that felt worthwhile. I even watched the lecture again but just blanked on it.</p>

### Nice to have
<hr>
<p>These would be great to have, but may be past my ability and time constraints.</p>

<p>On newcharacter.html:</p>
<ol>
  <li>An automatic way to add 15 points to a skill, just by clicking a radio button.</li>
  <li>Automatic initial skill calculations based off of your primary statistics.</li>
</ol>

### Not implemented
<hr>
<p>I mentioned these in my backend proposal, but did not implement them:</p>
<ol>
  <li><strong>User Registration:</strong> Mentioned above, I just couldn't figure it out. I want to have it for the final deliverable.</li> 
  <li><strong>Traits:</strong> Traits and perks are basically the same thing and are an optional feature. I decided it wasn't really needed.</li>
  <li><strong>Generate starter inventory based off tagged skills:</strong> Honestly, I just didn't have time and this seems like more of a "nice to have" than a "necessary".</li>
  <li><strong>Delete characters, items, weapons, armor:</strong> Honestly. <a href="https://www.tumblr.com/arthistorydoesntalwayssuck/54084168769/idratherstayin-besturlonhere-june-7th-1942">Just remembered right now...</a> going to try to add it in for the final.</li>
</ol>

## Setup
<hr>
<p>This is how I got it running on my second PC:</p>

<ol>
  <li>Download the repository.</li>
  <li>Unzip, and place in "users/yourname/pycharmProjects" folder.</li>
  <li>Open project in PyCharm.</li>
  <li>When the popup saying the database is not connected (bottom right hand corner) click the link on it.
  <ol type="a">
    <li>Download drivers if prompted.</li>
    <li>Test connection.</li>
    <li>Rejoice.</li>
  </ol>
  </li>
  <li>Back in the main window, in the top right, click the button lablled "Current file" to open the drop down menu, then click "Edit configurations".
  <ol type="a">
    <li>Add Configuration > Django Server</li>
    <li>Add Python Interpreter > Python 3.X.X </li>
  </ol>
  </li>
  <li>Run the server. Use the test accounts listed below.</li>
</ol>

I really hope this works for you, it worked flawless for me so I'm keeping my fingers crossed and knocking on wood and all that.

## Test Accounts
<hr>
<p>I have created a test account for you to use to try out the application. I have pre-created a character associated to this test account, but you can also make more.</p>

<p><strong>Username:</strong> test_user<br>
<strong>Password:</strong> ITEC4012A</p>

<p>If you want to go into admin view, try out the admin account.</p>

<p><strong>Username:</strong> admin<br>
<strong>Password:</strong> admin_lord23</p>
