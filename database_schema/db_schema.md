# snAPP Database Schema

## Entity-Relationship Model

### Entities
> user inputted data stored in the database will concern the below entities:

1. **Profile (member)**. snAPP member details.
2. **Bugtickets**. Details of bugs in the application.
3. **Featuretickets**. Details of new features proposed by members.
4. **Comment**. Comments made on Featuretickets and Bugtickets
5. **Upvotes.** 'Likes' made on bugtickets to help prioritise fixing a bug
6. **Orders.** Features receive donations as 'upvotes'



### Relationships
> the relationships between the different entitites are:
* A **Profile (member)** *reports* a **Bugticket**
* A **Profile (member)** *upvotes* a **Bugticket**
* A **Profile (member)** *comments* on a **Bugticket**
* A **Profile (member)** *sponsors* a **Featureticket**
* A **Profile (member)** *upvotes* a **Featureticket**
* A **Profile (member)** *comments* on a **Featureticket**


##### One-to-Many
    A Profile (member) can report MANY Bugtickets 
    A Bugticket can only have ONE reporting Profile (member)    
    
    A Profile (member) can propose MANY Featuretickets 
    A Featureticket can only have ONE proposing Profile (member)

##### Many-to-Many
    A Profile (member) can upvote/comment on MANY Bugtickets/Featuretickets
    A Bugticket/Featureticket can can have MANY upvoting/commenting Profiles (members)


### Attributes:

#### User Stories
> anticipating what members will do when using the application, what their motivations 
are and how they will fulfill their motivations. Nouns (e.g. **Bugtickets**) represent entities. Verbs (e.g. *report*) 
help to express relationships and how the user will interact with the data. 
Adjectives (e.g. `interesting`) suggest the attributes that entities must possess 
to meet users' browsing and functionality expectations  
* As a **member**, I want to *report* **bugs** which frustrate my enjoyment of snAPP
* As a **member**, I want to *propose* `useful` **features** to improve snAPP
* As a **member**, I want to *upvote* and *sponsor* `interesting` **features**
* As a **member**, I want to *upvote* `annoying` **bugs**
* As a **member**, I want to be able to *keep track* of progress of bug fixes/feature development
* As a **member**, I want to be able to *search* and *find* **bugtickets**/**featuretickets which reflect my experience
* As a **member**, I want to be able to *search* and *find* other **members** who I can *support/get support from*


#### Entity Attributes
> using the adjectives identified in the user stories to identify the attributes which the entitites must have to carry out the interactions in the user stories

**Profile:** user, image, trade union, description, alert, deadline for alert

**Bugticket:** title, type of bug, description, created by, date created, date started, date completed, update report, upvotes

**BugUpvote:** bugticket being upvoted, user (member), date created, vote type 

> note that 'vote_type' is currently set to default 'up'. It is planned to expand this functionality in future to enable member to 'down' vote as well

**Comment:** bugticket comment is about, author (member), comment, date created

**Featureticket:** title, description, type of feature, created by, date created, date started, date completed, upvotes, links to similar features, how much money has been donated, target, progress report

**Comment:** featureticket comment is about, author (member), comment, date created

**Orders:** address details, featureticket being purchased, quantity

#### CRUD operations 
> mapping the various user inputs into and interactions with the database


    Profile (members) [CREATE] profiles/bugtickets/featuretickets
    Profile (members) [UPDATE] profiles/bugtickets/featuretickets by upvoting or commenting on them
    Profile (members) [READ] profiles to find to find other members to support/get support from
    Profile (members) [READ] bugtickets to find bugs which they experience as well
    Profile (members) [READ] featuretickets to find features they would like to upvote/sponsor
    Profile (members) [DELETE] their own profiles
    

## Models

> The application's models were designed based on the ERM above.<br><br>The fields correspond to the entity attributes identified above. **Foreign Keys** (e.g created_by) are used to enable the one-to-many relationships, for example between the FeatureTicket and the Profile (member) who created it.<br><br>To capture the many-to-many relationships, for when handling comments, separate tables were created (e.g. 'Comments' or 'BugUpvotes') with foriegn keys pointing towards their respective parent tables. 

nb - *Django's default authentication models (including First Name, Last Name and Email address) were also used in creating the Profile table.* 


|Profile|BugTickets|BugUpvotes|Comments|FeatureTickets|Comment|Order|OrderLineItem     
| --- | --- | --- | --- | --- |--- |--- |--- |
| `user` | `created_by (FK)` | `bug_ticket (FK)` | `bug_ticket (FK)` | `created_by (FK)` | `feature_ticket (FK)` | `full_name` | `order` |
| `image`| `date_created` | `user (FK)` | `author (FK)` | `date_created` | `author (FK)` | `street_address1` | `feature` |
| `trade_union`| `date_started` | `date_created` | `text` | `date_started` | `text` | `street_address2` | `quantity` |
| `description` | `date_completed` | `vote_type` | `date_created` | `date_completed` | `date_created` | `town_or_city` | |
| `alert` | `title` | | | `title` | `county` | |
| `alert_date` | `bug_type` | | | `description` | `postcode` | |
| | `description` | | | `feature_type` | `country` | |
|       | `report` | | | `votes` | `phone_number` | |
|        | `votes` | | | `links` | `date` | |
|        | | | | `contribution` | | |
|        | | | | `target` | | |
|     |    | | | `report` | | |

Final models, with dataypes, can be found in the `models.py` file of the relevant app in the directory.

                        
                        