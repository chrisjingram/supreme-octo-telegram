# supreme-octo-telegram

As four students we split the work up into different sections that allowed us to work concurrently.
We started off as a team splitting the code into core class interfaces, as inspired by the design document. From here we could then incrementally update the code base, using a shared GitHub repo.

Half the team worked on parsing the input and passing the data into the simulation, the other half worked on the simulation, both on the core implementation, and looking into what basic optimisations could be achieved.

The simulation was written in a fully test-driven manner, allowing us to incrementally build upon our foundations.
Unfortunately we were unable to submit any output data based on input data, but as you can see from the tests in simulation.py, we were starting to generate valid output. By ensuring that each block by itself worked, we were able to compose them into a larger working simulation - e.g. starting with "Can one drone deliver one package to one location", then adding in a warehouse, then more warehouses at different locations.

We touched on optimising finding the closest items by being aware at the size of the map grid was actually irrelevant, and instead using the actual objects (warehouses, orders) to generate the true bounds of the map. From here we could split up the map into smaller sections and check them.

Further optimisations for that would involve making an octree and only checking the nearest blocks for nearby warehouses / orders.
