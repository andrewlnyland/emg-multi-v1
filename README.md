# Multi-Electromyogram

Stages:
1. Started designing in 2018, couldn't find sufficient amplifiers or free time to build
2. Internet of Things course, learned enough to start building and had help and time
3. Designing the next step *<-- Here, currently*
    - Radio antenna testing, power sources
    - Better hardware design and fabrication approach
    - Considering data analysis approaches for potential future use cases 

## Background
Muscle signals range on the order of +/-100mv, and the physical limitations (skin) of accessing these electrical signals can be vast. Gathering this data and interpretting it is also not an easy task. This project attempts to do all of the above.

### Purpose
Record multiple (ideally full body) muscle signals simultaneously, with a device that is affordable. 

### Original Goal
Identify and track tremors and muscle atrophy.

### Current Goal
Record human myoelectrical data and attempt to improve research around the topic. While building this project, I've noticed that the available literature is lacking on the math side and I'd like to see that expanded. This may also contribute to biological, neurological, or physiological understandings of the human body.

## Design

### Stage 1 
Consisted of learning in detail how peripheral neurons and muscle tissue work, and designing a theoretical approach to building the hardware. 

### Stage 2 
Our Internet of Things class covered basic breadboard building, radio management (avoiding collisions and dropped packets), state machine design of embedded processes, and serial data handling. We combined all of these with some operating system concepts and batteries for our final design.

### Stage 3
Many hopes and dreams, big plans.

## Implementation

### Stage 1 
No physical implementation exists, just many drawings, notes, and ponderings. I designed this stage to ultimately use an embedded CUDA GPU for processing (I have multiple Nvidia Jetsons on hand).

### Stage 2 
An Arduino, Raspberry Pi, an XBee radio, and many wires. The goal was to have a mobile setup for skiing to record six muscle groups, GPS (resulting in speed), and acceleration at 1Khz. It took about two weeks of time during undergraduate finals, three people, and around $2000 for hardware (during the supply chain freeze with a deadline approaching). 

### Stage 3
What I'd like to see:
 - longer power source for muscle sensors, easier distribution across the body
 - more accessible electrode technology, easier/better deployment strategy
 - improved math and biological understanding

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Stage 2 - Andrew Nyland, Andrew Walsh, and Michael Vidunas
All other Stages - Andrew Nyland

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

