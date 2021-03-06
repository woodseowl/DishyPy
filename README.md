# DishyPy

Simple Python examples for Starlink dish API

## Contents

- gRPC protocol modules for the Starlink dish (in /spacex/api), compiled mid-February 2021
- Very simplistic python scripts to show the two main API calls
- requirements.txt that provides the minimum python libraries for the scripts

## Installation / Usage

This project is meant simply as a starting point. There are two ways you might use it:

1. Just grab the spacex/api files and drop them into your own project (or into one like 
   [starlink-grpc-tools](https://github.com/sparky8512/starlink-grpc-tools)), instead of having
   to generate the gRPC protocol modules for python.

2. Install the project as is (`pip install --upgrade -r requirements.txt`) and then try running
   `status.py` to see if you are able to get data from your dish. If so, you are ready to prototype from
   `dish_get_status.py`. 

## History

I have a [Starlink](https://starlink.com) dish. I saw others had found it uses gRPC to report stats. I wanted to 
be able to get those stats to a RaspberryPi.

There's a tool called [`grpcurl`](https://github.com/fullstorydev/grpcurl) which would have been great, 
but [I couldn't find a binary](https://github.com/fullstorydev/grpcurl/releases) for the Pi's ARM architecture. 
Compiling it on a RaspberryPi was a long path and I was hoping to find a solution that would be fairly quick
and easy for others to use.

I found [starlink-grpc-tools](https://github.com/sparky8512/starlink-grpc-tools) had a collection of tools that 
looked like what I needed. I was hoping it would be able to be installed and just run. However, it requires you
to [generate the gRPC modules](https://github.com/sparky8512/starlink-grpc-tools#generating-the-grpc-protocol-modules),
which sent me back to lots of compiling on the RaspberryPi. That was fine, but I wondered whether I could make it
easier for anyone else.

Once I had the `starlink-grpc-tools` running, I thought it would be interesting to try to make the slimmest 
version of that idea, which is now this respository.

I also bought a [Pimoroni Unicorn HAT Mini](https://www.adafruit.com/product/4637) and wrote a little python
script to have the Unicorn HAT show me a graph of recent usage. Not quite ready for prime time, but it's fun.
That was the real reason I went down this path.

## Credit / Related Projects

Hat tip to the work on [starlink-grpc-tools](https://github.com/sparky8512/starlink-grpc-tools). Everything I
have that is working was basically learned from reviewing that repo.

I like the work on [ChuckTSI/BetterThanNothingWebInterface](https://github.com/ChuckTSI/BetterThanNothingWebInterface).
I thought I was going that direction (since I know PHP well), but getting it onto a RaspberryPi led to a dead
end of not being able to generate the Starlink API protocol modules for PHP. If anyone has a solution for that,
I would gladly make a PHP equivalent of this repository.

