# Android components #

Now that we have the building and owner for our app we can look at all the
stuff it is able to offer the customers and community. After all, no app is an
island and correctly understanding the different types of app components will
allow our app to have great synergy with the rest of the Android system.

## Overview ##

There are 4 main types of components namely: activities, services, broadcast
receivers, and content providers.

Each component is defined as an "entry point" into the app and can be viewed as
ways for customers to interact with our coffee shop. The image below will make
more sense as we go into detail about each different type.

![coffee shop](./images/shop.png)

Each component has its own special lifecycle in terms of when they run.

## Activities ##

The activities of an app each define one clear, well, activity.

These are generally used to directly interact with a user and can be used as an
entry point by itself. For example, you can view an activity as a barista that
is specialised to do one thing and do it really well. 

When you first enter the coffee shop you will encounter the "order a coffee"
activity which is followed by the "pay for coffee" activity. In this coffee
shop the ordering and paying for coffee is handled separately so that if a
customer wants to just order a coffee and then dash out for a bit before
paying, they won't have to re-order coffee before paying for it.

### System & User interaction ###

Since activities are only used with user interaction they need to clearly
communicate to the system what they are currently doing so that the system
doesn't kill them when it needs to recover memory.

There are 4 main things the activity relays to the system:

1. What's currently on the screen
2. The user might return to this activity please don't kill it
3. This activity is done, kill it and clean-up
4. Allowing user to flow to other apps

Point #3 is interesting because the activity/app can't terminate itself, but
has to request the system to do so.

These 4 states can be summed up with the following diagram below.
