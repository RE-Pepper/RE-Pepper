

# File alActorExecuteInfo.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**LiveActor**](dir_ae80ee5cf9da1054faf149dc2356c7ac.md) **>** [**alActorExecuteInfo.h**](al_actor_execute_info_8h.md)

[Go to the documentation of this file](al_actor_execute_info_8h.md)


```C++
#pragma once

namespace al
{

class ExecuteRequestKeeper;

class ActorExecuteInfo
{
private:
        ExecuteRequestKeeper* mRequestKeeper;

public:
        ExecuteRequestKeeper* getRequestKeeper() const
        {
                return mRequestKeeper;
        }
};

} // namespace al
```


