

# File alResource.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Resource**](dir_6ad324629ad6e0d47299f2844e376e3d.md) **>** [**alResource.h**](al_resource_8h.md)

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


