model architecture
    Membership
        -- slug
        -- type(free, pro, enterprise)
        -- price
        -- stripe plan id
    UserMembership
        -- user                     (FK default user)
        -- stripe customer id
        -- membership type          (FK to membership)
    Subscription
        -- user membership
        -- stripe subscription id   (FK to UserMembership)
        -- active
    Course
        -- slug
        -- title
        -- description
        -- allowed membership       (FK to Membership)
    Lesson
        -- slug
        -- title
        -- Course                   (FK to Course)
        -- position
        -- video
        -- thumbnail