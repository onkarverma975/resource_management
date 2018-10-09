# Resource Management and Relief Measures during Natural Disasters
Providing the right relief measures at the right time is crucial during any natural disaster and also after it occurs. It is even more important that the right amount of resources reach the right place. We describe an idea below for the same.

We assume an airport as a base which will have some given amount of resources. There will be some relief centres where the resources need to be delivered.  Since a natural disaster has occurred, some roads might be damaged. This can lead to several routes being closed. Assuming we know the closed routes, the amount of resources we have, and the amount of resources required by each relief centre, we suggest routes which can be followed to optimally deliver the relief material to the respective centres.

We model our solution as a constraint satisfaction problem. Our assumptions for the same are:

- Resources: Ground vehicles, Aerial Helicopter, list of resources and their quantity

- Input (Information we have): Amount of resource required by each relief centre, the capacity of each vehicle -  ground or aerial, the cost associated with each delivery for each vehicle - ground or aerial, the map of the area with information of closed and open routes.

- Constraints: Can be any combination of the following:
a. Total Cost
b. Time constraint in which the relief materials are to be provided
c. The capacity of aerial vehicles
d. The capacity of ground vehicles
e. Blocked routes, dynamically changing map
f. Speed limitations of the vehicles

- Output: routes to the relief centre satisfying the above constraints

Note: We plan to show the validation of our idea on self-generated maps.

