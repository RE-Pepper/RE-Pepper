

# File alLayoutInitInfo.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Layout**](dir_71ac96d9eee999c5231127773bfe6eda.md) **>** [**alLayoutInitInfo.h**](al_layout_init_info_8h.md)

[Go to the documentation of this file](al_layout_init_info_8h.md)


```C++
#pragma once

namespace al
{

class LiveActorKit;
class ExecuteDirector;

class LayoutInitInfo
{
public:
        ExecuteDirector* mExecuteDirector;
        void*            unk[ 2 ];

        LayoutInitInfo();
};

void initLayoutInitInfo( LayoutInitInfo* info, LiveActorKit* ); // why LiveActorKit ?

} // namespace al
```


