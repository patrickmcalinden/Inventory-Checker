<h1>Newegg Inventory Checker<h1>
<h3>Project Roots</h3>
This project idea came about when the new 30 series graphics cards were released. A few of my friends and I were really interested in purchasing 3070s and 3080s. We unfortunately couldn’t get our hands on them since they were so in-demand. I decided to make a script that would give us a better chance to purchase these cards.
<h3>Setup</h3>
At the time of this projectI,  had a working knowledge of Python and Javascript. I ultimately decided to work with Python due to the simplicity of the language and my natural tendency to create scripts.

After some research, I decided to put the Items that we wanted into a dictionary and split it into a “Full Sku” and  a “Half-Sku” (both are important for scraping the proper data). This was the easiest solution that produced the fastest response.
<h3>Outcome</h3>
I was pleased with how the script worked. It was quick and effective at notifying restocks of the given items compared to other restock monitor services. In the short term, there were no issues with the script. 

At the end of the day, while no one was able to purchase a card solely from this script we were able to cart more cards then before. It ultimately gave us a heads up that Newegg was restocking. 

<h3>Script Limitations</h3>
Unfortunately, Newegg has a different system for storing information for their items. Products that do not follow the typical graphics card sku, like “N82E16814126470”, would not work with script. 
	The only other issue that I have come across is the IP bans that occur after a few hours of using this script. One way to solve this issue would be by implementing a proxy system. I decided not to implement this since we found out Newegg typically restocked at the same times each week.
	<h3>Why Share Project?</h3>
	Although this project is very simple, I choose to share this because it has some level of functionality. It’s not some calculator project that isn’t touched after it is finished. I really like pursuing projects that have at least some level of usefulness.
	<h3>Project In Use</h3>
	[![Newegg Inventory Checker Demo](http://img.youtube.com/vi/4X8lWG-hN/0.jpg)](http://www.youtube.com/watch?v=4X8lWG-hN "Newegg Inventory Checker Demo")

