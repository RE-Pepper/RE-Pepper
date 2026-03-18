

# File alResource.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Resource**](dir_1d838ce5e4d6c8067670c51f08c15e87.md) **>** [**alResource.h**](al_resource_8h.md)

[Go to the documentation of this file](al_resource_8h.md)


```C++
#pragma once

#include <prim/seadSafeString.h>

namespace al
{

class Resource
{
public:
        const u8* getByml( const sead::SafeString& name ) const;
        u8*       getPa( const sead::SafeString& name ) const;
};

Resource* findOrCreateResource( const sead::SafeString& archive );

} // namespace al
```


