from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC32a3c49700934481addd5ce1659f04d2"
auth_token  = "{{ auth_token }}"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="<span class="skype_c2c_print_container notranslate">+14159352345</span><span id="skype_c2c_container" class="skype_c2c_container notranslate" dir="ltr" tabindex="-1" onmouseover="SkypeClick2Call.MenuInjectionHandler.showMenu(this, event)" onmouseout="SkypeClick2Call.MenuInjectionHandler.hideMenu(this, event)" onclick="SkypeClick2Call.MenuInjectionHandler.makeCall(this, event)" data-numbertocall="+14159352345" data-numbertype="paid" data-isfreecall="false" data-isrtl="false" data-ismobile="false"><span class="skype_c2c_highlighting_inactive_common" dir="ltr" skypeaction="skype_dropdown"><span class="skype_c2c_textarea_span" id="non_free_num_ui"><img width="0" height="0" class="skype_c2c_logo_img" src="chrome-extension://lifbcibllhkdhoafpjfnlhfpfgnpldfl/call_skype_logo.png"><span class="skype_c2c_text_span">+14159352345</span><span class="skype_c2c_free_text_span"></span></span></span></span>",    # Replace with your phone number
    from_="<span class="skype_c2c_print_container notranslate">+14158141829</span><span id="skype_c2c_container" class="skype_c2c_container notranslate" dir="ltr" tabindex="-1" onmouseover="SkypeClick2Call.MenuInjectionHandler.showMenu(this, event)" onmouseout="SkypeClick2Call.MenuInjectionHandler.hideMenu(this, event)" onclick="SkypeClick2Call.MenuInjectionHandler.makeCall(this, event)" data-numbertocall="+14158141829" data-numbertype="paid" data-isfreecall="false" data-isrtl="false" data-ismobile="false"><span class="skype_c2c_highlighting_inactive_common" dir="ltr" skypeaction="skype_dropdown"><span class="skype_c2c_textarea_span" id="non_free_num_ui"><img width="0" height="0" class="skype_c2c_logo_img" src="chrome-extension://lifbcibllhkdhoafpjfnlhfpfgnpldfl/call_skype_logo.png"><span class="skype_c2c_text_span">+14158141829</span><span class="skype_c2c_free_text_span"></span></span></span></span>") # Replace with your Twilio number
print message.sid
