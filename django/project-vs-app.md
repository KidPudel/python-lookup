In Django, app is the web app that is going to do something, like:
 - fetching from a database characters and all related info
 - small poll app  
Each app provides a specific peace piece of functionality.  
App should do one thing and do it well
<img width="500" alt="image" src="https://github.com/KidPudel/python-lookup/assets/63263301/327d45d7-fdc6-484b-9fc0-3b5d33e35d70">  
Best design:
- minimal coupling
  - to separate wisely, not (card, order, product, tag), BUT rather (card-order-product, tag), because it makes sense to have some together always (go only together) and some are separately for reuse
- high cnhesion (focus)
  - not to do monolith, but rather higly focused, again, not to put something we do not need


In Django, project is the collection of configurations and apps for the website.  
**Also project is the base, where all of the apps and apps configuration will go. (_All roads lead to... project_)**
