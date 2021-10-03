# POSTMORTEM: WannaCry Ransomware attack of 2017
![wannacry](https://mybroadband.co.za/news/wp-content/uploads/2017/05/WannaCry.jpg)

## Issue Summary
**Origin**
On May 5th 2017, starting at around 07:44UTC a malicious ransomware cryptoworm was released unto the world. The attackers would seize control of the victim's computer, encrypting files and demanding payment in Bitcoin.
In less that 24h it is estimated that around 200,000 computers across 150 countries were infected with damages estimated in the billions.

## Timeline
* **Start** 
	* ***07:30 UTC 12/05/2017*** @MalwareTechBlog releases info on a new attack called 'WannaCry' on Twitter
	* ***07:43 UTC 12/05/2017*** Cisco Umbrella pushes the kill switch to prevent the virus spreading
	* ***07:44 UTC 12/05/2017*** A vulnerable SMB port in Asia is the first target of the attack.
	* ***09:33 UTC 12/05/2017*** Cisco AMP detects the ransomware.
	* ***10:12 UTC 12/05/2017*** Cisco Umbrella adds attribution of the attack type to ransomware and moves the killswitch domain to malware
	* ***15:03 UTC 12/05/2017*** Attack is halted by killswitch


## Root Cause and Resolution

**Root Cause**
The United States National Security Agency had created a software known as "EternalBlue" which was designed to exploit older Windows OS. The hackers gained access to this when a group called "The Shadow Brokers" stole and distributed EternalBlue. The hackers then took this technology and built a botnet that could operate within it. The attack targetted computers running legacy systems that had not received security updates.

**Attack**
Upon execution WannaCry first checks for the killswitch domain name. If not found then the ransomware encrypts the computer's data, and exploits the SMB vulnerability to spread itself.
Wannacry then displays a ransom note to the user, stating they have 3 days to pay $300 in BTC, after which the cost will raise to $600 in BTC.

**Impact**
The ransomware campaign, though short-lived, was unprecedented in scale. One of the largest agencies affected was the National Health Service in England, which is a network of hospitals and affected 70,000 devices including computers, MRI scanners, blood-storage refrigerators and theatre equipment. Nissan Motor Manufacturing UK halted production during the cyberattack due to infection. Renault also stopped production at several sites. Telefonica, FedEx and Deutsche Bahn in Spain were also among the companies affected.
The attacks impact was limited thanks to the quick discovery of the killswitch built in by it's creators. Cyber-risk-modelling firm Cyence estimates the losses could have reached up to $4BUSD.

## Corrective and Preventative Measures
The day after the attack Windows released out-of-band security updates for their end of life products such as Windows XP, Windows Server 2003 and Windows 8.
Organizations were instructed to patch Windows and plug the vulnerability. Over the next few days new killswitches were developed and distributed, as well as beefing up the security of the site hosting the killswitch domain. Within four days of the initial outbreak new infections had slowed down to a trickle.

