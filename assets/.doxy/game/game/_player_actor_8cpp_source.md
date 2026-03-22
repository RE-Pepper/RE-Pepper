

# File PlayerActor.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**Player**](dir_9f791c72b7e31512581b67600bde1506.md) **>** [**PlayerActor.cpp**](_player_actor_8cpp.md)

[Go to the documentation of this file](_player_actor_8cpp.md)


```C++
#include "Player/PlayerActor.h"

#include "Player/Player.h"
#include "Player/PlayerProperty.h"

PlayerProperty* PlayerActor::getProperty()
{
        return mPlayer->getProperty();
}
```


