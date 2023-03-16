# UDP-Hole-Punching
An implementation of UDP Hole Punching using the python programming language

## What is UDP hole punching?
The internet is mainly designed for client-server communication making it difficult for two nodes on different private networks to communicate directly without using a server in the middle.

UDP hole punching allows two clients to set up a direct peer-to-peer UDP session without having to change any settings on their firewall or compromise their network security.

This works by first sending a UDP packet from client A to client B which creates a hole in client A's firewall allowing any future packets that client B sends to client A, to be passed through the firewall and forwarded to client A.

## Getting started

These instructions will get a copy of the project running on your local machine. 

### Prerequisites
The minimum Python version support is version 3.

### Install
You can install the module by running `python setup.py install` or using `pip install git+https://github.com/jdf18/UDP-Hole-Punching.git`

### Usage
WIP

## Acknowledgments
 * Bryan Ford - [Peer-to-Peer Communication Across Network Address Translators](https://bford.info/pub/net/p2pnat/)
 * engineer-man - [UDP Peer-To-Peer Messaging With Python](https://www.youtube.com/watch?v=IbzGL_tjmv4) - [github](https://github.com/engineer-man/youtube/blob/master/141/client.py)
 
