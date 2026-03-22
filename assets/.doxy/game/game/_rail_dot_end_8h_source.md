

# File RailDotEnd.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**MapObj**](dir_2096800ae80e9b320e335490a6d8aa70.md) **>** [**RailDotEnd.h**](_rail_dot_end_8h.md)

[Go to the documentation of this file](_rail_dot_end_8h.md)


```C++
#pragma once

#include <MapObj/alMapObjActor.h>

class RailDotEnd : public al::MapObjActor
{
public:
        void exeWait();

public:
        virtual void init( const al::ActorInitInfo& info );

public:
        RailDotEnd( const sead::SafeString& name );
};
```


