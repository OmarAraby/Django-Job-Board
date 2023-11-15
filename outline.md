Job :
    - title
    - location
    - job type
    - description
    - published at
    - vacancy
    - salary
    - category
    - experience



    - apply job
    - post job


Blog :
    - title
    - description
    - created_at
    - category
    - tags
    - author

    ---> Enable To make An Edit On Post 
    ---> Category Filter
    ---> Comment
    ---> Reply On the comment
    ---> Enable Editing On Comment
    ---> Next & Previos on Blog Posts


    - search
    - comment
    - recent posts


Contact

Home

Login



---------------------------------------------------------------------------------------------

Relationship :
    - One to Many --> (user - posts ) (auther - books)  ForeginKey
    - Many to Many ----> (user - groups) 
    - One to One ----> (user - profile)



---------------------------------------------------------------------------------------------

static files : [all files that are related to frontend (images , css , js)]

media files : [upload files (images , )]
---------------------------------------------------------------------------------------------



API :

    - Function Based Views :
        - simple
        - customize
        - if you have a complex logic and you need to implement it


    - Class Based Views (Genecric Based Views) :
        - fast development
        - not prefered if you have a complex logic 


    - ViewSets :
     - API -- [model + url] [CRUD] ---> it make all operation that you need
     - difficult to customize 


