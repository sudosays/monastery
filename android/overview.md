# Overview of Android Apps #
_By Julius Stopforth_

[source](https://developer.android.com/guide/index.html)

## App Fundamentals ##

The `.apk` extension refers to the compiled 'archive' file used to install the app.

Every app runs in its own virtual machine (VM) that's known as its app sandbox.

![app sandboxes](./images/app_sandbox.png)

These VM processes are self contained and managed by the user account for the app and the system.

This app's user account is given specialised permissions that the app requests, but it is not known by the app itself!

You can view it as the app's guardian or wrangler.
